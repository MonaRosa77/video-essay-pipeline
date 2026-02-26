# Understanding Claude Code's Full Stack: MCP, Skills, Subagents, and Hooks

**Source:** https://alexop.dev/posts/understanding-claude-code-full-stack/
**Author:** Alex Op (alexop.dev)
**Type:** Architectural overview

---

## Four-Layer Architecture

1. **Foundation:** Model Context Protocol (MCP)
2. **Core Features:** CLAUDE.md, Slash Commands, Subagents, Hooks
3. **Plugins** (bundle components from layers 1-2)
4. **Agent Skills** (activate automatically)

---

## Component Breakdown

### CLAUDE.md -- Project Memory
Hierarchical markdown. Loading order: Enterprise → User (`~/.claude/`) → Project root → Directory-specific. Persistent across sessions.

### Slash Commands
User-triggered workflows in `.claude/commands/`. Support arguments, pre-execution bash, XML-tagged prompts.

### Subagents
Isolated contexts, individual system prompts, restricted tool access, parallel execution. Prevent context pollution.

### Hooks
Event-driven handlers in `.claude/settings.json`:

| Event | When |
|---|---|
| PreToolUse | Before any tool call |
| PostToolUse | After tool completes |
| UserPromptSubmit | User sends message |
| Notification | Claude generates notification |
| Stop | Claude finishes response |
| SubagentStop | Subagent finishes |
| SessionStart | New session begins |

Two modes: shell commands (deterministic) or prompt-based (Claude decides).

### Plugins
Distributable packages bundling commands, hooks, skills, metadata.

### MCP
Universal adapter for external tools/databases/APIs. Servers expose tools, resources, and prompts. MCP servers do NOT inherit Claude's native capabilities.

### Agent Skills
`.claude/skills/` with SKILL.md. Auto-matched to task context. No manual invocation needed.

---

## Decision Framework

| Component | Use When |
|---|---|
| CLAUDE.md | Static knowledge persisting across sessions |
| Slash Commands | Explicit, repeatable workflows |
| Subagents | Parallel or isolated specialized work |
| Hooks | Automatic quality enforcement |
| Plugins | Team-wide configuration distribution |
| MCP | External system integration |
| Skills | Context-driven automatic behaviors |
