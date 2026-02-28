# Mastering Claude Skills: The 33-Page Blueprint for AI Infrastructure

**Source:** https://techbytes.app/posts/anthropic-claude-skills-guide-breakdown-feb-2026/
**Author:** Dillip Chowdary (breakdown of Anthropic's official 33-page guide)
**Published:** February 15, 2026

---

## Directory Structure (kebab-case required)
```
your-skill-name/
  SKILL.md          (Required, Case-Sensitive)
  scripts/          (Optional: .py, .sh for validation)
  references/       (Optional: API docs, guides)
  assets/           (Optional: Templates, icons)
```

## YAML Spec
- **name:** Must match folder name exactly
- **description:** Max 1,024 chars. Explicitly state trigger conditions.
- **allowed-tools:** Security-first whitelist

## Progressive Disclosure (3 Levels) -- 50% Token Reduction

**Level 1 (Global):** YAML metadata always in context. Minimal footprint.
**Level 2 (Active):** Full SKILL.md body on trigger.
**Level 3 (On-Demand):** Referenced files loaded only when needed.

**Benchmark:** Complex project: clarifications 15→2, tokens 12,000→6,000.

---

## Five Orchestration Patterns

### 1. Sequential Workflow
Multi-step processes. Key: "Rollback Instructions" -- if step 3 fails after step 2 succeeds, define revert actions.

### 2. Multi-MCP Coordination
Workflows spanning services (Figma → Drive → Linear → Slack). Key: "Phase Separation" markers -- validate data from one MCP before passing to another.

### 3. Iterative Refinement
High-stakes outputs (legal docs, code reviews). Key: "Stopping Conditions" -- e.g., "Stop after 3 iterations or when validation returns 0 errors."

### 4. Context-Aware Tool Selection
Dynamic decisions by file type/size. Key: Decision Matrices -- "If file > 5MB, use S3; otherwise, local storage."

### 5. Domain-Specific Intelligence
Compliance logic (financial, HIPAA). Key: "Pre-flight Compliance Checks" -- run script before authorizing sensitive operations.

---

## The 90/0 Rule -- Success Metrics

1. **Skill Trigger Rate:** 90%+ accuracy on relevant queries
2. **API Call Success Rate:** 0 failed calls per workflow
3. **Token Efficiency:** Measure reduction vs. putting everything in CLAUDE.md

---

## Key Insight

Skills = paradigm shift from "prompt engineering" to **"AI Infrastructure"** design.
