# Trading & Order Flow Analysis

Generates structured analyses of trading education content, with particular rigor around evidence quality and risk assessment.

## Activation

Use this skill when analyzing transcripts about:
- Scalping, day trading, swing trading
- Order flow, footprint charts, volume profile, delta
- Price action, market structure, liquidity
- Futures, forex, CFDs, options execution
- Trading psychology and risk management

Topic slugs: `trading`. Channels: `axia-futures`, `ict`, or any trading educator.

## Analysis Template

### Header
```markdown
# Analysis: <Descriptive Title>

- **Video**: <youtube_url>
- **Channel**: <channel_name>
- **Analyzed**: <YYYY-MM-DD>

---
```

### Core Edge Claimed
One substantial paragraph identifying:
- What specific **trading edge** the video claims to teach
- **Edge type classification**: Informational (knows something others don't), Structural (exploits market mechanics), Behavioral (exploits common trader mistakes), Statistical (pattern with positive expectancy), or None Claimed (educational/motivational only)
- How the edge is framed — as universal, conditional, or situational

### Setup Identification
For each distinct trade setup presented:

**Setup N: <Name>**
- **Market context**: When does this setup apply? (trend, range, reversal, specific session)
- **Entry trigger**: Exact conditions for entry
- **Stop placement**: Where and why
- **Target**: How profit is taken (fixed, trailing, structural)
- **Timeframe**: Chart timeframe(s) used
- **Instruments**: What markets this is demonstrated on

If no concrete setups are presented, state this explicitly.

### Evidence Quality Assessment
Evaluate with extreme rigor:

**Sample Size**
- How many trade examples are shown?
- Are they cherry-picked winners or representative samples?
- Is there any mention of win rate, expectancy, or statistical backing?

**Survivorship Bias**
- Does the presenter show losses? How are they framed?
- Are student results cited? With what specificity and verification?
- Is there a survivorship bias in the examples chosen?

**Verifiability**
- Live account vs. demo account vs. replay/hindsight?
- Regulated broker with auditable records, or unverifiable platform?
- Are specific dates, prices, and instruments identifiable and checkable?

**Quantitative Claims**
- Any P&L numbers, handle targets, or return claims?
- Are these substantiated with data or just asserted?
- What's the claimed risk/reward? Is it realistic?

### Risk Parameters
What is discussed (and what's missing) regarding:
- Position sizing and account management
- Maximum drawdown tolerance
- Risk of ruin considerations
- Correlation risk (multiple positions in same direction)
- The statistical reality that 70-80% of retail traders lose money (per SEC/CFTC data)

If risk management is absent or superficial, flag this prominently.

### Cross-Reference to Standard Concepts
Map the presenter's terminology to established trading concepts:

| Presenter's Term | Standard Equivalent | Notes |
|-----------------|---------------------|-------|
| ... | ... | ... |

This is critical for ICT and other educators who use proprietary terminology for common concepts.

### Counter-Arguments
**Minimum 5.** Each should:
- Name the specific claim being challenged
- Provide counter-evidence from market microstructure research, regulatory data, or competing approaches
- Assess severity for someone actually trading this

Look specifically for:
- Unfalsifiable claims (if win → method works; if lose → your fault)
- Missing risk disclosure
- Vague claims about "institutional" knowledge without evidence
- Math that doesn't add up (claimed returns vs. stated risk parameters)
- Selection bias in examples

### Actionable Takeaways
What a trader could *actually use* from this video, separated into:

**High confidence** — Observations that are well-supported or standard practice
**Medium confidence** — Plausible but unverified claims
**Low confidence / Caution** — Claims that require significant additional validation

### Distinction: Original vs. Standard Concepts
Separate the presenter's original contributions from established trading knowledge:
- What is genuinely novel in their approach?
- What is standard repackaged with new terminology?
- What is claimed as original but has clear antecedents?

---

### Overall Assessment
A candid 1-paragraph assessment of:
- The video's educational value (what percentage is education vs. promotion vs. motivation?)
- Who this video is actually useful for
- The single biggest red flag (if any) and the single most valuable insight (if any)

## Quality Criteria

- **Never assume a trading method works** — the analysis must evaluate evidence, not repeat claims
- The evidence quality section is the most important part. Be forensic.
- Cross-reference proprietary terminology to standard concepts — do not let jargon pass unexamined
- Always note the absence of risk disclosure, statistical evidence, or verified track records
- The analysis should help the reader decide whether to invest further time in this educator's content
