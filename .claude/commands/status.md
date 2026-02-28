# /status — Pipeline status report

Scan the entire pipeline and report on current state.

## Workflow

### 1. Scan directories
All content lives on GitHub under `research-topics/`. List remote files:
```bash
git ls-tree -r --name-only origin/main research-topics/
```

Also check the project root for any legacy files (transcript_*.md, analysis_*.md).

### 2. Count files per domain
For each `research-topics/<topic>/` directory, count files by type:
- Transcripts (in `transcripts/`)
- Analyses (in `analyses/`)
- Essays (in `essays/`)
- Research documents (in `research/`)

Parse channel from filename (e.g., `transcript_michael-sugrue_...` → channel `michael-sugrue`).

### 3. Identify gaps
For each domain:
- List transcripts that have NO matching analysis (match by video ID in filename)
- List analyses that have NO matching essay
- Flag any files outside of `research-topics/` that should be moved

### 4. Check naming conventions
Flag any violations:
- Files not matching expected patterns (`transcript_<channel>_*.md`, `analysis_<channel>_*.md`, `essay_<channel>_*.md`)
- Unexpected subdirectories under `research-topics/<topic>/<type>/`

### 5. Report
Format the output as a clean table:

```
## Pipeline Status — <date>

### Overview
| Topic | Channel | Transcripts | Analyses | Essays | Coverage |
|-------|---------|-------------|----------|--------|----------|
| ...   | ...     | N           | N        | N      | N%       |

### Gaps
- <topic>/<channel>: N transcripts missing analysis
  - transcript_<channel>_XXXX.md (no analysis)
  ...

### Naming Issues
- (any violations found)

### Legacy Files
- (any root-level files that need moving)
```
