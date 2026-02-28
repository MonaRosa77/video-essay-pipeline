# Code Execution with MCP: Building More Efficient Agents

**Source:** https://www.anthropic.com/engineering/code-execution-with-mcp
**Authors:** Adam Jones, Conor Kelly (Anthropic Engineering)
**Published:** November 4, 2025

---

## The Problem

Traditional MCP: tool definitions occupy context, increasing cost. Large documents flow through model multiple times.

## The Solution: Filesystem-Based Tool Discovery

Present MCP servers as code APIs in a file tree:
```
servers/
  google-drive/
    getDocument.ts
    index.ts
  salesforce/
    updateRecord.ts
    index.ts
```

Agent navigates filesystem, discovers and loads ONLY needed tool definitions.

**Token reduction:** 150,000 → 2,000 tokens = **98.7% saving**.

## Three Key Benefits

1. **Progressive Disclosure:** Agents explore filesystem structure instead of receiving all definitions upfront
2. **Data Filtering at Execution Layer:** Filter 10,000 rows locally before returning results. Intermediate data never touches context.
3. **Control Flow Efficiency:** Loops/conditionals execute natively in code sandbox, not via model round-trips.

## Security Architecture

- **Intermediate Result Isolation:** Only explicitly returned data reaches model
- **PII Tokenization:** Auto-converts emails/phones to `[EMAIL_1]` tokens before model visibility
- **Deterministic Data Routing:** Security rules enforce which data flows between systems, model cannot override

## State Management

Persist data across operations via filesystem: CSV exports, reusable skill functions in `./skills/`, SKILL.md documentation. Enables long-running workflows surviving context resets.
