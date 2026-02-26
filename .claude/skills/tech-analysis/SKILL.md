# Tech & AI Architecture Analysis

Generates structured analyses of software architecture, AI agent systems, developer tools, and technical infrastructure content.

## Activation

Use this skill when analyzing transcripts about:
- Software architecture and system design
- AI agents, LLMs, prompt engineering, agent infrastructure
- Developer tools, CLIs, IDEs, productivity systems
- Cloud infrastructure, DevOps, platform engineering
- Technical product launches, engineering blog posts

Topic slugs: `ai-agents`, or any tech/software-related topic.

## Source Credibility Tiers

Assess every source against this hierarchy:

| Tier | Description | Weight |
|------|-------------|--------|
| **Builder/Insider** | Built or works on the system being discussed | Highest — but watch for promotional bias |
| **Independent Analyst** | Reverse-engineered, benchmarked, or audited independently | High — lowest bias risk |
| **Practitioner** | Uses the system in production and reports results | Medium-High — real but single-perspective |
| **Secondary Source** | Summarizes, interprets, or repackages primary sources | Medium — check what they add vs. parrot |

State the tier for each source/speaker in the analysis.

## Analysis Template

### Header
```markdown
# Analysis: <Descriptive Title>

- **Video**: <youtube_url>
- **Channel**: <channel_name>
- **Source Credibility**: <tier from table above>
- **Analyzed**: <YYYY-MM-DD>

---
```

### Central Claim
One substantial paragraph identifying:
- The **core technical thesis** — what is being claimed about this technology/architecture
- Whether this is a new capability claim, a best-practice recommendation, an architectural pattern, or a product announcement
- The scope: does this apply broadly or to a specific niche?

### Architecture Map
Describe the system's structure:

**Components**
- List each major component/layer with its role

**Data Flow**
- How data/requests move through the system
- What triggers what

**Boundaries**
- Where are the trust boundaries?
- What's internal vs. external?
- Where does the system make assumptions?

Use a text diagram if the architecture has 3+ interacting components:
```
[Component A] → [Component B] → [Component C]
                      ↓
              [Component D]
```

### Evidence Quality Assessment
Per-claim evaluation:

| Claim | Evidence Type | Strength | Notes |
|-------|-------------|----------|-------|
| ... | Benchmark / Anecdote / Internal metric / None | Strong/Medium/Weak | ... |

For quantitative claims (performance numbers, adoption metrics, cost savings):
- Is the methodology described?
- Are comparisons fair (apples-to-apples)?
- Could the numbers be replicated independently?

### Cross-Source Position Map
If this topic has been covered by multiple sources, map where this source stands:

| Topic | This Source | Consensus | Dissent |
|-------|-----------|-----------|---------|
| ... | ... | ... | ... |

This is especially important for fast-moving topics (AI agents, LLMs) where claims evolve weekly.

### Counter-Arguments
**Minimum 5.** Each should:
- Name the specific technical claim being challenged
- Provide a counter-argument or alternative approach
- Assess practical impact — would this matter for someone building on these ideas?

Look specifically for:
- Promotional framing disguised as technical assessment
- Missing failure modes or edge cases
- Scalability claims without evidence at scale
- Vendor lock-in or ecosystem dependencies not acknowledged
- "Works for us" generalized to "works for everyone"

### Actionable Insights
What a developer/architect could actually apply:

**Immediately applicable** — Patterns or techniques that work now
**Worth investigating** — Promising but needs validation in your context
**Wait and see** — Interesting but too early, too niche, or too dependent on specific conditions

### Notable Concepts Worth Developing
Numbered list of ideas, patterns, or architectural insights worth writing about:
- The concept and why it matters
- Where it connects to broader trends
- What essay or technical post could develop it

### Distinction: Original vs. Standard Practice
- What is genuinely novel in this presentation?
- What is established practice with good framing?
- What is claimed as novel but is standard?

## Quality Criteria

- Apply the credibility tier to every claim — insiders are informative but biased; independent analysts are most reliable
- Never accept performance numbers without noting methodology and reproducibility
- The architecture map should be precise enough for someone to build a prototype from
- Cross-source positioning is critical for AI topics where hype cycles distort claims
- The analysis should help the reader decide whether to adopt, investigate, or ignore this approach
