# Tools

Small scripts that support the research behind the whitepaper. Each lives in
its own directory with a README that says how to install and run it and what
its output is good for.

| Tool | What it does |
|------|--------------|
| [youtube-transcript](youtube-transcript/) | Fetch a YouTube video's captions as plain text, with a fallback that works from cloud IPs where the usual package is blocked. |

Conventions:

- Raw output goes to `notes/` (gitignored). Only summarised, verified material
  goes to `research/` or `docs/`.
- A tool's README states the failure modes we have actually hit and what fixed
  them, dated, so the next person does not rediscover them.
