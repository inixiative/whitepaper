#!/usr/bin/env python3
"""Fetch a YouTube video's transcript as plain text.

Usage:
    fetch_transcript.py URL_OR_ID [--out PATH] [--stdout] [--timestamps] [--lang en]

Two backends, tried in order:

1. youtube-transcript-api  -- clean, fast, works from residential IPs.
2. yt-dlp with the `web_embedded` player client -- what actually works from
   cloud/datacenter IPs (Claude Code on the web, CI runners, VPS), where
   YouTube blocks the first backend with RequestBlocked / "Sign in to confirm
   you're not a bot".

Output is one paragraph of text with a metadata header (title, channel, URL,
duration, which backend served it). By default it is written to
notes/transcripts/<video-id>.txt at the repo root, which is gitignored, so
transcripts stay personal working material unless you move them.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def video_id(s: str) -> str:
    """Accept a bare id or any of the usual YouTube URL shapes."""
    if ID_RE.match(s):
        return s
    u = urllib.parse.urlparse(s)
    if u.netloc.endswith("youtu.be"):
        return u.path.strip("/").split("/")[0]
    q = urllib.parse.parse_qs(u.query)
    if "v" in q:
        return q["v"][0]
    m = re.search(r"/(shorts|embed|live)/([A-Za-z0-9_-]{11})", u.path)
    if m:
        return m.group(2)
    sys.exit(f"could not find a video id in: {s}")


def oembed(vid: str) -> dict:
    """Title and channel. oEmbed is not bot-gated, so this works anywhere."""
    url = ("https://www.youtube.com/oembed?format=json&url="
           + urllib.parse.quote(f"https://www.youtube.com/watch?v={vid}", safe=""))
    try:
        with urllib.request.urlopen(url, timeout=20) as r:
            return json.load(r)
    except Exception:
        return {}


def via_transcript_api(vid: str, lang: str):
    """Returns list of (start_seconds, text) or raises."""
    from youtube_transcript_api import YouTubeTranscriptApi  # noqa: WPS433
    api = YouTubeTranscriptApi()
    fetched = api.fetch(vid, languages=[lang])
    return [(s.start, s.text) for s in fetched]


def via_ytdlp(vid: str, lang: str):
    """yt-dlp, embedded-player client, subtitles only. Returns list of (start, text)."""
    if not shutil.which("yt-dlp"):
        raise RuntimeError("yt-dlp not on PATH")
    with tempfile.TemporaryDirectory() as td:
        cmd = [
            "yt-dlp", "--skip-download", "--ignore-no-formats-error",
            "--write-subs", "--write-auto-subs",
            "--sub-langs", lang, "--sub-format", "json3",
            "--extractor-args", "youtube:player_client=web_embedded",
            "-o", os.path.join(td, "v.%(ext)s"),
            f"https://www.youtube.com/watch?v={vid}",
        ]
        # YouTube intermittently returns the player data without the caption
        # track; a second or third try a few seconds later usually gets it.
        for attempt in range(3):
            p = subprocess.run(cmd, capture_output=True, text=True)
            files = [f for f in os.listdir(td) if f.endswith(".json3")]
            if files:
                break
            time.sleep(4 * (attempt + 1))
        if not files:
            tail = (p.stderr or p.stdout).strip().splitlines()[-3:]
            raise RuntimeError("yt-dlp produced no subtitles after 3 tries: " + " | ".join(tail))
        with open(os.path.join(td, files[0]), encoding="utf-8") as f:
            data = json.load(f)
    out = []
    for ev in data.get("events", []):
        segs = ev.get("segs") or []
        text = "".join(" " if s.get("utf8") == "\n" else s.get("utf8", "") for s in segs)
        text = " ".join(text.split())
        if text:
            out.append((ev.get("tStartMs", 0) / 1000.0, text))
    return out


def hms(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def render(segs, timestamps: bool) -> str:
    if timestamps:
        return "\n".join(f"[{hms(t)}] {txt}" for t, txt in segs)
    return " ".join(" ".join(txt.split()) for _, txt in segs)


def repo_root() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], text=True,
            stderr=subprocess.DEVNULL).strip()
    except Exception:
        return os.getcwd()


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("video", help="YouTube URL or 11-character video id")
    ap.add_argument("--out", help="output path (default notes/transcripts/<id>.txt)")
    ap.add_argument("--stdout", action="store_true", help="print instead of writing")
    ap.add_argument("--timestamps", action="store_true",
                    help="one caption per line with [h:mm:ss] prefix")
    ap.add_argument("--lang", default="en")
    args = ap.parse_args()

    vid = video_id(args.video)
    meta = oembed(vid)

    segs, backend, errors = None, None, []
    for name, fn in (("youtube-transcript-api", via_transcript_api), ("yt-dlp/web_embedded", via_ytdlp)):
        try:
            segs = fn(vid, args.lang)
            backend = name
            break
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: {type(e).__name__}: {str(e).splitlines()[0][:200]}")
    if not segs:
        sys.exit("all backends failed:\n  " + "\n  ".join(errors))

    header = "\n".join(filter(None, [
        f"title: {meta.get('title', '?')}",
        f"channel: {meta.get('author_name', '?')}",
        f"url: https://www.youtube.com/watch?v={vid}",
        f"duration: ~{hms(segs[-1][0])}",
        f"backend: {backend}",
        f"words: {sum(len(t.split()) for _, t in segs)}",
        "note: auto-generated captions; proper nouns are often mangled",
    ]))
    body = render(segs, args.timestamps)
    doc = header + "\n\n" + body + "\n"

    if args.stdout:
        sys.stdout.write(doc)
        return
    out = args.out or os.path.join(repo_root(), "notes", "transcripts", f"{vid}.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"{out}  ({backend}, {header.splitlines()[5]})")


if __name__ == "__main__":
    main()
