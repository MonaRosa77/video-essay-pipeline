# Equipping Agents for the Real World with Agent Skills

**Source:** https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
**Author:** Anthropic Engineering Team
**Type:** Official design rationale

---

## Progressive Disclosure Pattern (Core Design Insight)

Three levels to manage context window:

**Level 1 -- Metadata:** Names + descriptions loaded at startup. Minimal tokens. Enables relevance decisions without loading full context.

**Level 2 -- Core Instructions:** Full SKILL.md loaded when Claude determines skill applies. Moderate tokens.

**Level 3+ -- Supplementary Files:** `reference.md`, scripts, etc. Loaded ONLY when contextually appropriate. Tokens scale with actual need.

Analogy: table of contents → chapters → appendices.

---

## Code Execution Integration

Skills bundle pre-written code (Python) that Claude executes as discrete tools. Traditional computation (sorting, extraction, math) is more reliable and cost-effective than token generation. Unlike instructions, executable code is **deterministic and repeatable**.

---

## Development Guidelines

1. **Start with evaluation:** Run agents on representative tasks, identify capability gaps BEFORE building skills
2. **Structure for scale:** When SKILL.md gets unwieldy, split into separate files. Keep mutually exclusive contexts separate.
3. **Think from Claude's perspective:** Monitor real-world usage. Pay attention to `name` and `description` -- they drive triggering.
4. **Iterate with Claude:** Collaborate with the agent to capture successful approaches into reusable skills.

---

## Platform Support

Agent Skills work across: Claude.ai, Claude Code, Claude Agent SDK, Claude Developer Platform. Cross-platform standard.

**Open standard:** Published at agentskills.io (December 2025). Adopted by GitHub Copilot, Cursor, OpenAI Codex.
