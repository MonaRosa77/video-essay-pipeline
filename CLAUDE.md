# Video → Essay Pipeline

A knowledge system that fetches video transcripts, analyzes arguments with domain-specific rigor, and develops them into essays.

## Domains

| Domain | Topic slug | Channels |
|--------|-----------|----------|
| Philosophy & Ethics | `philosophy` | `michael-sugrue`, `johnathan-bi` |
| Trading & Order Flow | `trading` | `axia-futures`, `ict` |
| Tech & AI Agents | `ai-agents` | `claude-code` |

## File Conventions

- **Folders:** lowercase-kebab-case everywhere
- **Structure:** `research-topics/<topic>/<type>/` (e.g. `research-topics/trading/transcripts/`)
- **No channel subdirectories** — channel is encoded in filenames
- **Transcripts:** `transcript_<channel>_<video_id>.md` or `NN_<channel>_<slug>.md` for ordered series
- **Analyses:** `analysis_<channel>_<keyword>_<video_id>.md`
- **Essays:** `essay_<channel>_<keyword>_<date>.md`
- **Research:** keep as-is (already descriptive)

## Quality Standards

- **Factcheck claims** before presenting them. Do not make assertions that require the user to correct you.
- When the transcript is in Chinese, provide analysis in both Chinese and English unless told otherwise.
- Distinguish between the video creator's original arguments vs. ideas they're citing from other thinkers.
- Flag any claims that seem factually questionable and note them for verification.

## Storage Model

Content (transcripts, analyses, essays, research) lives on **GitHub only** — not in the local working tree. Only pipeline files (scripts, `.claude/`, config) are kept locally via `git sparse-checkout`.

- **After creating content:** `git add` → `git commit` → auto-pushed by post-commit hook → `git sparse-checkout reapply` removes local copies
- **To read content:** `git checkout origin/main -- <path>` to pull temporarily, or `git show origin/main:<path>` to read without checkout
- **To list remote content:** `git ls-tree -r --name-only origin/main research-topics/<topic>/<type>/`

## Scripts

```bash
python3 yt-fetch.py <url_or_id> [--lang zh en] [--no-timestamps] [--topic philosophy] [--channel michael-sugrue]
python3 yt-channel.py <@handle_or_url> [--sort popular] [--limit 20] [--fetch] [--topic trading] [--channel axia-futures]
```

## Slash Commands

- `/fetch` — Fetch transcript + auto-analyze with domain skill
- `/status` — Pipeline overview: counts, gaps, naming issues
- `/research` — Multi-video research project with synthesis
- `/essay` — Generate essay draft from analyses
- `/domain` — Create new domain directory tree
