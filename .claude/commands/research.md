# /research — Multi-video research project

Fetch, analyze, and synthesize multiple videos on a topic into a research document.

## Arguments
- `$ARGUMENTS` — Topic description, optionally followed by `--channel <channel_url_or_handle>` and `--limit <N>`

Examples:
```
/research stoic ethics in Marcus Aurelius --channel @SusanRigetti --limit 5
/research order flow scalping strategies --channel @AxiaFutures --limit 10
/research Claude Code agent architecture
```

## Workflow

### 1. Parse arguments
Extract:
- **Topic description**: the free-text part before any flags
- **Channel** (optional): YouTube channel handle or URL
- **Limit** (optional, default: 5): max videos to process

### 2. Identify or collect videos
If a channel is provided:
```bash
python3 ~/video-essay-pipeline/yt-channel.py <channel> --sort popular --limit <N>
```

If no channel, check what transcripts already exist on GitHub for this topic area:
```bash
git ls-tree -r --name-only origin/main transcripts/<topic>/
```
List them and ask the user which to include, or if they want to provide URLs.

### 3. Fetch transcripts
For each video that doesn't already have a transcript:
```bash
python3 ~/video-essay-pipeline/yt-fetch.py <url> --no-timestamps --topic <topic> --channel <channel>
```

Use subagents to parallelize: launch up to 3 fetch+analyze tasks simultaneously using the Task tool.

### 4. Analyze each video
For each transcript, generate an analysis using the appropriate domain skill. Save analyses to the standard location.

### 5. Generate synthesis document
After all individual analyses are complete, read them all and generate a synthesis document that:

**Cross-Video Synthesis Structure:**

```markdown
# Research: <Topic Title>

- **Videos analyzed**: N
- **Channel(s)**: <list>
- **Date**: <YYYY-MM-DD>

---

## Executive Summary
2-3 paragraphs synthesizing the key findings across all videos.

## Thesis Comparison
| Video | Central Claim | Evidence Strength | Key Insight |
|-------|--------------|-------------------|-------------|
| ...   | ...          | Strong/Medium/Weak | ...         |

## Convergent Claims
Ideas that appear in 2+ videos — these are the most robust findings.

## Divergent Claims
Where sources disagree — these are the most interesting for essay development.

## Evidence Gaps
What none of the sources address but should.

## Essay Candidates
3-5 essay topics that emerge from this research, each with:
- Proposed thesis
- Which sources support/challenge it
- What additional research would strengthen it

## Individual Analyses
Links to each analysis file.
```

### 6. Save synthesis
Save to `research/<topic>/synthesis_<keyword>_<date>.md`

Create the directory if it doesn't exist.

### 7. Commit and clean up
Commit all new content to GitHub:
```bash
git add transcripts/ analyses/ research/
git commit -m "Research: <topic> (<N> videos)"
```
The post-commit hook auto-pushes. Then clean up local content:
```bash
git sparse-checkout reapply
```

### 8. Report
Tell the user:
- How many videos were fetched and analyzed
- Where the synthesis document was saved (GitHub path)
- Top 3 essay candidates identified
