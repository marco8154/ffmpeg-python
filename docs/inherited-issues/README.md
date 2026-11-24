# Inherited issues and pull requests (raw export)

Open issues and pull requests of the original project `kkroening/ffmpeg-python`, exported 2026-11-24 (cut-off date for triage) so agents without network access can triage them.

| File | Content |
|---|---|
| `raw-issues.json` | 478 open issues with 835 comments |
| `raw-pulls.json` | 46 open pull requests with 45 comments, plus `isDraft`, `headRefName`, `baseRefName`, `url` |

Each entry has the fields of `gh issue list --json number,title,author,createdAt,updatedAt,labels,body,comments`; `comments` holds the full comments (`author.login`, `body`, `createdAt`). Exported through the public GitHub REST API (`/issues?state=open`, `/issues/comments`, `/pulls?state=open`) instead of `gh`, sorted by issue number. Read-only snapshot: do not edit, re-export instead.
