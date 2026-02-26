# How to Use Claude Code Like the People Who Built It

**Source:** https://every.to/podcast/transcript-how-to-use-claude-code-like-the-people-who-built-it
**Speakers:** Boris Cherny (Head of Claude Code), Cat Wu (PM), Dan Shipper (host)
**Format:** Podcast transcript (Every.to / AI & I)

---

## Origin Story

Claude Code evolved from "Clide" (C-L-I-D-E), a heavy Python research project. Boris hand-wrote a PR and Adam Wolf rejected it: "you wrote this by hand. What are you doing?" The prototype was a terminal chat app using the Anthropic API. Breakthrough: "The biggest revolution was when we gave the model tools -- they just started using them" -- bash, AppleScript, spontaneously.

## Design Philosophy: Terminal-First, No Text Editor

Not intentional. Models demonstrated natural tool usage with bash access. Engineers could compose workflows locally. Everything became "dual use" -- humans AND models use the same interface.

## Tool Architecture: Agentic RAG, Not Vector Search

Why no embeddings: maintenance requires continuous re-indexing, local changes cause stale data, security risks for enterprise. "Claude models are really good at agentic search." Same accuracy without deployment complexity.

About a dozen tools, added/removed most weeks. Recently unshipped the LS tool.

## Dual-Use Tool Design

"Tools were built for engineers, but now it's equal parts engineers and models." Slash commands accessible to both. `/commit` -- humans run manually OR Claude invokes automatically. Bash mode with `!` prefix. "Elegant design for humans translates really well to the models."

---

## Internal Anthropic Slash Commands

**Cat uses:** `/slash PR commit` -- exact bash commands for commits

**Boris uses:**
- `/commit`, `/PR` -- standard workflows
- `/feature dev` -- structured: asks what you want → generates spec → detailed plan → todo list (created by team member Sid)
- `/security review` -- security review of PRs
- `/code review` -- **All Anthropic PRs are reviewed by Claude first; a human then approves.**

**Features:** Templating runs bash ahead of time, embeds commands, pre-allows tool invocations, uses Haiku (cheaper/faster model).

---

## Subagent Patterns

**Map-Reduce Pattern:** Main agent creates big todo list → spawns 10+ subagents simultaneously → each handles portion → deduping quality step. Found all real issues without false positives.

**Opponent Processor Pattern:** Boris's expense system: "auditor subagent" and "pro-Dan subagent" battle to determine categorization. Uncorrelated context windows produce better results.

**Cat's experiments:** Front-end testing subagent using Playwright. "Not totally there yet, but signs of life."

**High-credit users:** Some Anthropic employees spend $1,000+/month on tokens, primarily for code migrations.

---

## Boris's Three Working Modes

1. **Prototyping:** Build simplest thing touching all systems, trace unknowns, throw away and retry. `Esc Esc` to checkpoint.
2. **One-shot tasks:** Tell Claude, go to different tab, `Shift+Tab` to auto-accept, tend other Claudes.
3. **Harder features:** Shift into plan mode. Align on plan before code. **Plan mode gives 2-3X success rate improvement.**

---

## Memory and Knowledge Accumulation

**Compounding Engineering (Every's approach):** Codify learnings → document plan changes → encode into prompts/subagents/slash commands → next person catches issues automatically → new person productive immediately on unknown codebase.

**Anthropic's memory experiments:** Power users maintain "diary entries" -- what Claude tried, why it failed, lessons. Synthesizing agents extract patterns from past memory.

**Natural behavior:** Sonnet 4.5 naturally looks through git history when stuck.

---

## Power User Setup

**Common mistakes:** Not using plan mode enough. Neglecting settings.json.

**settings.json:** Pre-allows commands (no prompts), blocks restricted files, check into codebase, share with team.

**Stop hooks:** Run when turn completes. "If tests don't pass, keep going." Deterministic outcomes from stochastic models.

**Cat's tip:** Tell Claude: "We're just brainstorming. Please ask me questions if anything is unclear." Claude doesn't naturally ask questions -- you have to prompt it.

---

## Internal Anthropic Use Cases

**Issue tracker (built by Ingo):** Dedupes incoming issues, finds duplicates (extremely accurate), performs first-pass resolution, proactively generates PRs.

**On-call log aggregation:** Collates Sentry, queue logs, other sources. "Really good because it's all just bash in the end."

---

## Future Form Factors

1. **Longer autonomy:** Current: double-digit hours. Last model: ~30 hours. Next: "going to be days."
2. **Container needs:** "What is the container, because you don't want to close your laptop."
3. **Claude monitoring Claude:** Multi-model hierarchies. Claude-to-Claude communication optimized for bandwidth.

Boris: "The terminal is not the final form factor."

---

## Key Numbers

| Metric | Value |
|---|---|
| Boris manual code since Nov 2025 | 0% (100% AI-written) |
| GitHub commits by Claude Code | 4% (predicted 20% by end 2026) |
| Anthropic productivity increase | 200% per engineer |
| Daily active users | Doubled recently |
| Some devs ship | 10-30+ PRs daily |
| Internal adoption | 70-80% of technical Anthropic employees daily |
| Claude Cowork build time | 10 days |
