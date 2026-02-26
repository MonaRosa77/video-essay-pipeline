# /status — Pipeline status report

Scan the entire pipeline and report on current state.

## Workflow

### 1. Scan directories
Scan these directories recursively:
- `~/video-essay-pipeline/transcripts/`
- `~/video-essay-pipeline/analyses/`
- `~/video-essay-pipeline/essays/`
- `~/video-essay-pipeline/research/`

Also check the project root for any legacy files (transcript_*.md, analysis_*.md).

### 2. Count files per domain
For each `<topic>/<channel>/` combination found, count:
- Transcripts
- Analyses
- Essays
- Research documents

### 3. Identify gaps
For each domain:
- List transcripts that have NO matching analysis
- List analyses that have NO matching essay
- Flag any files in the root directory that should be in subfolders

### 4. Check naming conventions
Flag any violations:
- Folders not in lowercase-kebab-case
- Files not matching expected patterns (`transcript_*.md`, `analysis_*.md`, `essay_*.md`)
- Empty directories that can be cleaned up

### 5. Report
Format the output as a clean table:

```
## Pipeline Status — <date>

### Overview
| Domain | Channel | Transcripts | Analyses | Essays | Coverage |
|--------|---------|-------------|----------|--------|----------|
| ...    | ...     | N           | N        | N      | N%       |

### Gaps
- <topic>/<channel>: N transcripts missing analysis
  - transcript_XXXX.md (no analysis)
  ...

### Naming Issues
- (any violations found)

### Legacy Files
- (any root-level files that need moving)
```
