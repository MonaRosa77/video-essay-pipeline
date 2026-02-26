# Video → Essay Pipeline

A knowledge system that fetches video transcripts, analyzes arguments with domain-specific rigor, and develops them into essays.

## Domains

| Domain | Topic slug | Channels |
|--------|-----------|----------|
| Philosophy & Ethics | `western-philosophy` | `michael-sugrue` |
| Trading & Order Flow | `trading` | `axia-futures`, `ict` |
| Tech & AI Agents | `ai-agents` | `claude-code` |

## File Conventions

- **Folders:** lowercase-kebab-case everywhere (`western-philosophy/michael-sugrue/`)
- **Transcripts:** `transcript_<video_id>.md` or `NN_<slug>.md` for ordered series
- **Analyses:** `analysis_<keyword>_<video_id>.md`
- **Essays:** `essay_<keyword>_<date>.md`
- **Paths:** `<type>/<topic>/<channel>/` (e.g. `transcripts/trading/axia-futures/`)

## Quality Standards

- **Factcheck claims** before presenting them. Do not make assertions that require the user to correct you.
- When the transcript is in Chinese, provide analysis in both Chinese and English unless told otherwise.
- Distinguish between the video creator's original arguments vs. ideas they're citing from other thinkers.
- Flag any claims that seem factually questionable and note them for verification.

## Scripts

```bash
python3 yt-fetch.py <url_or_id> [--lang zh en] [--no-timestamps] [--topic western-philosophy] [--channel michael-sugrue]
python3 yt-channel.py <@handle_or_url> [--sort popular] [--limit 20] [--fetch]
```

## Slash Commands

- `/fetch` — Fetch transcript + auto-analyze with domain skill
- `/status` — Pipeline overview: counts, gaps, naming issues
- `/research` — Multi-video research project with synthesis
- `/essay` — Generate essay draft from analyses
- `/domain` — Create new domain directory tree
