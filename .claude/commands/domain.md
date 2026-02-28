# /domain — Create or inspect a domain

Set up a new topic domain with the full directory tree, or inspect an existing one.

## Arguments
- `$ARGUMENTS` — Topic name, optionally followed by `--url <channel_url>`

Examples:
```
/domain psychology
/domain eastern-philosophy --url @AcademyOfIdeas
/domain trading
```

## Workflow

### 1. Parse arguments
Extract:
- **Topic**: first argument (will be kebab-cased)
- **URL** (optional): YouTube channel URL or handle for listing videos

### 2. Normalize names
Convert to lowercase-kebab-case:
- Spaces → hyphens
- Uppercase → lowercase
- Remove special characters

### 3. Create directory tree
```
research-topics/<topic>/transcripts/
research-topics/<topic>/analyses/
research-topics/<topic>/essays/
research-topics/<topic>/research/
```

No channel subdirectories — channels are encoded in filenames.

### 4. List available videos (if URL provided)
Run:
```bash
python3 ~/video-essay-pipeline/yt-channel.py <url> --sort popular --limit 20
```

Show the user the top 20 videos by views and ask if they want to start fetching any.

### 5. Update domain table
Read the current CLAUDE.md and check if this domain is already listed in the domains table. If not, suggest adding it (but don't modify CLAUDE.md automatically — show the user what line to add and ask for confirmation).

### 6. Report
Tell the user:
- What directories were created
- Current file counts (should be 0 for new domains)
- Next steps: "Use `/fetch <url> --topic <topic> --channel <channel>` to start adding content"
