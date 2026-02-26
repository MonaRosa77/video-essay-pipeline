# Claude Agent Skills: A First Principles Deep Dive

**Source:** https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/
**Author:** Lee Han Chung
**Type:** Reverse-engineering / architecture analysis

---

## Core Architecture

Skills are NOT executable code. They are a "declarative, prompt-based system" -- specialized prompt templates that inject domain-specific instructions into conversation context. They modify what Claude knows and what it's permitted to do.

**Selection mechanism:** NO algorithmic routing, no AI intent detection at code level, no regex, no keyword matching. Claude's native language understanding matches intent against skill descriptions through pure LLM reasoning.

---

## SKILL.md Structure

### YAML Frontmatter

**Required:** `name`, `description`
**Optional:** `allowed-tools`, `model`, `version`, `license`, `disable-model-invocation`

### Prompt Content (Recommended Sections)
1. Purpose statement (1-2 sentences)
2. Overview
3. Prerequisites
4. Instructions (numbered steps)
5. Output Format
6. Error Handling
7. Examples
8. Resources (bundled file references using `{baseDir}`)

### Directory Structure
```
skill-name/
  SKILL.md          # Core instructions
  scripts/          # Python/Bash for deterministic ops
  references/       # Text docs loaded into context on demand
  assets/           # Templates, CSS, images (referenced by path, NOT loaded)
```

---

## Two-Message Injection System

When invoked, TWO messages are injected:

**Message 1 (visible to user):** Metadata showing what skill activated
**Message 2 (hidden, `isMeta: true`):** Full skill prompt + context modifier

**Why two messages?** Combining creates impossible UX: visible full prompts overwhelm users; hidden metadata provides zero transparency. Two-message split = user sees WHAT, Claude sees FULL instructions.

**Context Modifier:** Pre-approves specific tools, overrides model selection, scopes permissions to skill execution duration only.

---

## Discovery and Loading

**Sources scanned (priority order):**
1. User settings: `~/.config/claude/skills/`
2. Project settings: `.claude/skills/`
3. Plugin-provided skills
4. Built-in skills

**Token budget:** Available skills listing = 15,000 character budget by default.

**API placement:** Skills live in the `tools` array, NOT system prompts.

---

## Full Execution Lifecycle (PDF Example)

1. **Discovery:** Scan directories, load SKILL.md, extract frontmatter
2. **Selection:** Claude reads `<available_skills>` list, matches intent through reasoning
3. **Validation:** Check existence, permissions, load file, generate context modification
4. **Injection:** Create visible metadata message + hidden skill prompt message
5. **API Request:** Full messages array + permission modifications sent to API
6. **Execution:** Claude follows workflow, uses pre-approved tools without user prompt

---

## Best Practices

- Keep SKILL.md under 5,000 words
- Include only necessary tools in `allowed-tools`
- Use imperative language ("Analyze code for...")
- Always use `{baseDir}` placeholder for portability
- Load detailed content from `references/` on demand (progressive disclosure)
