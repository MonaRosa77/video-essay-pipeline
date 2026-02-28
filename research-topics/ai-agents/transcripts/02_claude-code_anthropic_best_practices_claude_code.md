# Claude Code: Best Practices for Agentic Coding

**Source:** https://www.anthropic.com/engineering/claude-code-best-practices
**Author:** Anthropic Engineering Team
**Type:** Official documentation

---

## Core Constraint

"Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills."

---

## Practice 1: Give Claude a Way to Verify Its Work

**The single highest-leverage thing you can do.**

- Provide test cases, expected outputs, screenshots for comparison
- Use Chrome extension for UI verification
- Address root causes: "fix this error" → "fix and verify the build succeeds. Address the root cause, don't suppress the error"

## Practice 2: Explore First, Then Plan, Then Code

Four phases:
1. **Explore:** Plan Mode (`Ctrl+G`). Read files, answer questions, no changes.
2. **Plan:** Create detailed implementation plan.
3. **Implement:** Switch to Normal Mode. Code against the plan.
4. **Commit:** Descriptive message + PR.

Skip planning when: fix is small, describable as one diff sentence.

## Practice 3: Specific Context in Prompts

- Reference files with `@` instead of describing locations
- Paste images directly
- Give URLs for docs; `/permissions` to allowlist domains
- Pipe data: `cat error.log | claude`
- Point to existing patterns: "look at HotDogWidget.php and follow the pattern"

## Practice 4: Configure Your Environment

### CLAUDE.md
- `/init` to generate starter
- Keep short and human-readable
- For each line ask: "Would removing this cause mistakes?" If not, cut it
- Bloated files cause Claude to ignore instructions
- Use emphasis ("IMPORTANT", "YOU MUST") for adherence
- Check into git; compounds over time
- Supports `@path/to/import` syntax

### Locations
- `~/.claude/CLAUDE.md` -- all sessions
- `./CLAUDE.md` -- project (git-shared)
- `CLAUDE.local.md` -- personal (.gitignore)
- Parent/child directories for monorepos

### Hooks
Unlike CLAUDE.md (advisory), hooks are **deterministic and guaranteed**.
- "Write a hook that runs eslint after every file edit"
- "Write a hook that blocks writes to the migrations folder"

### Skills
`.claude/skills/` with `SKILL.md` files. Auto-applied when relevant. `disable-model-invocation: true` for manual-only workflows.

### Custom Subagents
`.claude/agents/` with own context and tools. For tasks needing specialized focus or heavy file reading.

## Practice 5: Communicate Effectively

**Let Claude interview you:**
```
I want to build [description]. Interview me using AskUserQuestion.
Ask about implementation, UI/UX, edge cases, tradeoffs.
Don't ask obvious questions -- dig into the hard parts.
Keep going until covered, then write spec to SPEC.md.
```
Then start a fresh session to execute the spec.

## Practice 6: Manage Your Session

- `Esc`: Stop mid-action, context preserved
- `Esc + Esc` or `/rewind`: Restore previous state
- `/clear`: Reset between unrelated tasks
- **Rule:** If corrected Claude 2+ times on same issue, `/clear` and start fresh
- `/compact <instructions>`: Controlled context reduction
- Use subagents for investigation (keeps main context clean)
- `claude --continue`: Resume recent conversation
- `/rename`: Give sessions descriptive names

## Practice 7: Automate and Scale

**Headless:** `claude -p "prompt"` for CI/scripts. `--output-format stream-json`.

**Writer/Reviewer pattern:** Session A implements, Session B reviews, Session A addresses feedback.

**Fan out:** List files → loop with `claude -p "Migrate $file"` → test → refine → run at scale.

---

## Common Failure Patterns

1. **Kitchen sink session:** Mixing unrelated tasks. Fix: `/clear` between tasks.
2. **Correcting repeatedly:** Same error loop. Fix: `/clear`, better initial prompt.
3. **Over-specified CLAUDE.md:** Too long, ignored. Fix: Prune ruthlessly. Convert to hooks if must be guaranteed.
4. **Trust-then-verify gap:** Plausible but wrong. Fix: Always provide verification.
5. **Infinite exploration:** Unscoped "investigate." Fix: Scope narrowly or use subagents.
