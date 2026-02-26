# /essay — Generate essay draft from analyses

Read analyses for a topic and generate a structured essay draft.

## Arguments
- `$ARGUMENTS` — Topic slug (e.g., `western-philosophy`) optionally followed by `--thesis "<thesis statement>"` and `--channel <channel>`

Examples:
```
/essay western-philosophy --channel michael-sugrue
/essay western-philosophy --thesis "Stoic virtue ethics provides a more practical moral framework than Kantian deontology"
/essay trading --channel axia-futures
```

## Workflow

### 1. Gather source material
Read all analyses in `analyses/<topic>/<channel>/`. If no channel specified, read all analyses under the topic.

Also check `research/<topic>/` for any synthesis documents.

List what was found and confirm with the user before proceeding.

### 2. Generate thesis candidates
If no `--thesis` was provided, propose **3 thesis candidates** based on the analyses:

For each candidate:
- **Thesis statement** (1-2 sentences)
- **Supporting sources** (which analyses back this up)
- **Strength** (how well-evidenced is this across the sources?)
- **Originality** (how much does this go beyond what the video creators already said?)

Ask the user to pick one, modify one, or provide their own.

### 3. Generate essay draft

**For philosophy topics**, use the opponent processor approach:
- First pass: Build the strongest case FOR the thesis, drawing on all supporting evidence
- Second pass: Build the strongest case AGAINST the thesis, drawing on counter-arguments from analyses
- Third pass: Synthesize — address the strongest objections, refine the thesis if needed

**For all topics**, use this structure:

```markdown
# <Essay Title>

*Draft — <date>*

## Abstract
150-250 words summarizing the argument.

## I. Introduction
- Hook: start with the most compelling quote, paradox, or question from the sources
- Context: what conversation is this essay entering?
- Thesis: state it clearly
- Roadmap: what the essay will argue and in what order

## II-V. Body Sections
Each section should:
- Make one clear sub-argument that supports the thesis
- Draw on specific evidence from the analyses (cite video sources)
- Acknowledge and respond to the strongest counter-argument to this point
- Transition logically to the next section

## VI. Counter-Arguments
Dedicate a full section to the strongest objections:
- Present them fairly (steelman, don't strawman)
- Respond to each
- Acknowledge any that remain partially unresolved

## VII. Conclusion
- Restate the thesis in light of the argument made
- Identify what this argument implies beyond its immediate scope
- End with a question or provocation, not a summary

## Sources
List all analyses and transcripts used.

## Development Notes
- What additional research would strengthen this essay
- Which arguments are weakest and need more evidence
- Suggested next steps for revision
```

### 4. Save essay draft
Save to `essays/<topic>/<channel>/essay_<keyword>_<date>.md`

Use today's date in YYYY-MM-DD format for `<date>`.

### 5. Report
Tell the user:
- Where the essay was saved
- Word count
- Which arguments feel strongest and weakest
- Suggested next steps (additional sources, counterarguments to research, sections to expand)
