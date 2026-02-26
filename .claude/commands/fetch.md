# /fetch — Fetch transcript and analyze

Fetch a YouTube video transcript and automatically generate a domain-specific analysis.

## Arguments
- `$ARGUMENTS` — YouTube URL or video ID, optionally followed by `--topic <topic> --channel <channel>`

## Workflow

### 1. Parse arguments
Extract the URL/video ID from `$ARGUMENTS`. If `--topic` and `--channel` are provided, use them. If not, try to infer from the video content after fetching.

### 2. Fetch transcript
Run:
```bash
python3 ~/video-essay-pipeline/yt-fetch.py <url> --no-timestamps --topic <topic> --channel <channel>
```
Read the output to find the saved file path.

### 3. Read the transcript
Read the saved transcript file in full.

### 4. Determine the domain
Based on the transcript content, determine which domain this falls into:
- **Philosophy/Ethics:** lectures on philosophers, moral theory, metaphysics, epistemology → `western-philosophy`
- **Trading/Order Flow:** scalping, futures, order flow, footprint charts, volume profile → `trading`
- **Tech/AI:** software architecture, AI agents, developer tools, LLMs → `ai-agents`

If the domain is unclear, ask the user.

### 5. Generate analysis
Apply the matching domain analysis skill to produce a structured analysis. The analysis MUST include:
- Central Claim
- Supporting Arguments (numbered)
- Evidence Quality Assessment
- Counter-Arguments (minimum 3, aim for 5+)
- Notable Quotes or Concepts
- Original vs. Cited Ideas distinction

### 6. Save analysis
Save to `analyses/<topic>/<channel>/analysis_<keyword>_<video_id>.md`

The `<keyword>` should be a short (1-3 word) lowercase slug identifying the video's subject (e.g., `aurelius`, `scalping-reversal`, `mcp-architecture`).

### 7. Commit and push to GitHub
Content is stored on GitHub, not locally. After saving both files:
```bash
git add transcripts/ analyses/
git commit -m "Add transcript + analysis: <keyword> (<video_id>)"
```
The post-commit hook auto-pushes. Then clean up local content:
```bash
git sparse-checkout reapply
```
This removes the transcript and analysis from the working tree (they're safely on GitHub).

### 8. Report
Tell the user:
- Where the transcript was saved (GitHub path)
- Where the analysis was saved (GitHub path)
- A 2-3 sentence summary of the video's central claim
- Any factual claims that need verification
