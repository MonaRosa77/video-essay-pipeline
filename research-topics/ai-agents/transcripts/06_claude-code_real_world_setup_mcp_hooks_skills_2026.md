# My Claude Code Setup: MCP, Hooks, Skills -- Real Usage 2026

**Source:** https://okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/
**Author:** Daniil Okhlopkov (Head of Analytics, TON Foundation)
**Published:** February 23, 2026

---

## MCP Servers (configured in .mcp.json)

1. **Coolify MCP:** App deployment, service restart, log checking, database management
2. **Telegram MCP:** Full Telegram access -- read, reply, channel management
3. **Codex MCP:** Dual-model review system. Claude proposes → OpenAI Codex reviews. Second opinion before execution.

## Skills (in ~/.claude/skills/)

Pure markdown, no SDK, no build process.

1. **ton-analyst** (~200 lines): Writes Dune SQL for blockchain analysis. SQL templates, API endpoints, documented gotchas.
2. **ton-profiler:** Investigates wallet connections via internal APIs.
3. **crosspost:** Publishes across Telegram, Ghost blog, Twitter/X in three languages simultaneously.

## Hooks

**Pre-commit hook:** Blocks commits containing `.env`, `.key`, `.pem`, `creds.md`. Safety guardrail for unattended agents.

## Subagents and Teams

- **Data Agent:** SQL queries on Dune Analytics
- **Profiling Agent:** Internal wallet databases
- **Report Agent:** Synthesizes outputs from other agents

## Daily Workflow

1. Records voice notes via Telegram throughout the day
2. 24/7 server agent retrieves and processes voice notes
3. Analytics: agent writes SQL, retrieves data, generates visualizations, compiles reports -- 3-4 hours → ~20 minutes
4. Coding: describe requirements → agent reads, writes, tests, commits

## Claude Code vs Cursor

- Cursor: quick inline edits, exploring unfamiliar codebases, precise location-specific changes
- Claude Code: multi-step workflows, autonomous background ops, large refactoring, external system integration
- **Author's ratio:** 90% Claude Code, 10% Cursor

## Second Brain Architecture

Operates within an **Obsidian vault** containing personal notes, project files, task lists, voice transcripts. CLAUDE.md bridges Obsidian's knowledge base and Claude Code.

## Cost

$100/month Max Plan. Saves ~2 hours daily. 30-page blockchain report with 15 charts and 40+ SQL queries: one evening vs one full work week.
