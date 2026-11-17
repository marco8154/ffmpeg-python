# Security Policy

## Supported versions

Security fixes are provided for the latest release of `ffmpeg-python-ng` only.
The original `ffmpeg-python` 0.2.0 is not maintained here.

## Reporting a vulnerability

Report vulnerabilities privately via
https://github.com/marco8154/ffmpeg-python/security/advisories/new. Do not
open a public issue. Your report should include: package version, Python
version, ffmpeg version, the smallest reproducer, and the expected impact.
Reports are handled on a best-effort basis; there is no committed timeline.

## Scope

In scope are bugs in this package, for example when building the argument
list, handling temporary files, or starting the `ffmpeg`/`ffprobe`
processes. Out of scope are vulnerabilities in ffmpeg itself; report those to
the FFmpeg project at https://ffmpeg.org/security.html. This package builds
an argument list and launches ffmpeg and ffprobe via `subprocess` without a
shell; it does not process media data itself.
