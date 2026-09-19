# YouTube transcript fetcher

Pulls a video's captions as plain text so a long talk or podcast can be read,
searched, and quoted instead of listened to.

## Install

```sh
pip install -r tools/youtube-transcript/requirements.txt
```

## Use

```sh
# writes notes/transcripts/<video-id>.txt (gitignored) and prints the path
tools/youtube-transcript/fetch_transcript.py "https://youtu.be/zqKvm3Ry8vs"

# print to the terminal instead
tools/youtube-transcript/fetch_transcript.py zqKvm3Ry8vs --stdout | less

# one caption per line with [h:mm:ss] prefixes, for finding a passage to quote
tools/youtube-transcript/fetch_transcript.py zqKvm3Ry8vs --timestamps --out /tmp/t.txt

# another language, if the video has it
tools/youtube-transcript/fetch_transcript.py zqKvm3Ry8vs --lang de
```

The file opens with a short header: title, channel, URL, approximate
duration, which backend served the captions, and the word count.

## What it does, and why it has two backends

1. **`youtube-transcript-api`** is tried first. It is the well-known package for
   this job and works from a normal home or office connection.
2. **`yt-dlp` with the `web_embedded` player client** is the fallback. YouTube
   blocks the first package from cloud and datacenter IPs (Claude Code on the
   web, CI runners, any VPS) with `RequestBlocked` or "Sign in to confirm
   you're not a bot". The embedded-player endpoint is the one that still serves
   captions without a login from those IPs, as of September 2026. It also needs
   `--ignore-no-formats-error`, because that client returns captions but no
   video streams, and yt-dlp otherwise treats that as a failure. The script
   passes that flag for you.

If both fail, the script prints one line per backend saying why. The usual
fixes are, in order: try again in a minute (429 rate limit), try from a
different network, or pass browser cookies to yt-dlp per its FAQ. Cookies risk
the account they came from, so treat that as the last resort.

The video's title and channel come from YouTube's oEmbed endpoint, which is not
bot-gated, so the header is filled in even when captions are blocked.

## Caveats on the text

- These are usually **auto-generated captions**. Proper nouns get mangled
  (Pareto becomes "paro", Mucha becomes "Musha", Canetti becomes "Ketti").
  Check any name before citing it.
- There is no speaker labelling. On two-person podcasts the captioner inserts
  `>>` at some speaker changes, but not reliably.
- Numbers, dates, and book titles in a transcript are the speaker's
  recollection. Verify them against a written source before they go into
  `docs/`.

## Where output goes

`notes/` is gitignored, so `notes/transcripts/` is the right home for raw
transcripts: working material, not part of the paper. If a transcript earns a
place in the record, summarise it into `research/` with the URL and a
verification note, rather than committing the raw text.
