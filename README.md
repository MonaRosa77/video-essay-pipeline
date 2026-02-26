# Video → Essay Pipeline

A streamlined workflow for turning video content into structured essays using Claude Code + Claude.ai.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐
│  YouTube /  │     │  Claude Code  │     │   Claude.ai     │
│  Video URL  │────▶│  (terminal)   │────▶│  (conversation) │
│             │     │               │     │                 │
│             │     │  • fetch      │     │  • discuss      │
│             │     │  • structure  │     │  • challenge    │
│             │     │  • analyze    │     │  • draft essay  │
└─────────────┘     └──────────────┘     └─────────────────┘
```

## Prerequisites

- **Claude Code** installed ([docs](https://docs.claude.com/en/docs/claude-code/overview))
  ```bash
  # Native install (recommended, no Node.js needed)
  curl -fsSL https://claude.ai/install.sh | bash
  
  # Or via npm (requires Node.js 18+)
  npm install -g @anthropic-ai/claude-code
  ```
- **Python 3.8+** (for the transcript fetcher)
- **Claude Pro/Max subscription** or API key for Claude Code

## Quick Start

```bash
# 1. Clone/download and run setup
chmod +x setup.sh
./setup.sh

# 2. Navigate to pipeline directory
cd ~/video-essay-pipeline

# 3. Fetch a transcript
python yt-fetch.py "https://www.youtube.com/watch?v=2Kda3NtlNUg"

# 4. Launch Claude Code for analysis
claude
> Read transcript_2Kda3NtlNUg.md and give me a structured analysis 
> of the core arguments about the nature of political power.

# 5. Take the analysis to Claude.ai for essay development
# Upload both transcript + analysis files to a Project conversation
```

## Using with Claude Code

Once you `cd ~/video-essay-pipeline && claude`, Claude Code reads the CLAUDE.md
file and understands the full workflow. You can use natural language:

```
> Fetch and analyze: https://youtube.com/watch?v=2Kda3NtlNUg

> The video's argument about X seems weak because Y. 
> Can you find counterexamples?

> Draft an essay outline that combines insights from the last 
> 3 transcripts we analyzed.

> Write the introduction section. Tone: analytical but accessible. 
> Audience: educated general reader.
```

## Workflow Tips

### For Chinese-language content
The fetcher automatically tries zh-Hans → zh-Hant → zh before English.
Analyses will be bilingual unless you specify otherwise.

### Batch processing
```bash
# Fetch multiple videos
for url in "url1" "url2" "url3"; do
  python yt-fetch.py "$url" -o "transcripts/$(date +%Y%m%d)_$RANDOM.md"
done
```

### Integration with Claude.ai Projects
1. Create a Project called "Video Essays" (or whatever you like)
2. Set Project instructions to guide the essay style and analysis depth
3. Upload transcript + analysis files as context
4. Discuss, iterate, and develop the essay in conversation

## File Structure

```
~/video-essay-pipeline/
├── CLAUDE.md              # Claude Code instructions
├── yt-fetch.py            # Transcript fetcher
├── setup.sh               # One-time setup
├── transcripts/           # Raw transcripts
│   └── transcript_xxxxx.md
├── analyses/              # Structured analyses
│   └── analysis_xxxxx.md
└── essays/                # Essay drafts
    └── draft_xxxxx.md
```
