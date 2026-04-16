# Evidence hierarchy

The conflict-resolution engine of DRP. Top tier wins. Consensus across tiers doesn't override a single tier-1 source.

---

## The tiers

| Tier | Source type | Examples | Typical use |
|---:|---|---|---|
| **1** | Meta-analyses / official bodies / primary legal texts | BOE, EUR-Lex, FDA, ICH guidelines, WHO, ISO published standards, Cochrane reviews, UN conventions | Gold standard. One tier-1 source can overturn any number of lower-tier sources. |
| **2** | Peer-reviewed papers | Nature, Science, domain journals, arXiv preprints with strong track records | High quality. Check funding and venue. |
| **3** | Technical reports, whitepapers, standards bodies | NIST, IETF RFCs, W3C, OWASP, MITRE, industry standards bodies | Strong for technical truth. |
| **4** | Vendor / first-party official docs | Docs.openai.com, docs.anthropic.com, docs.<product>.com, GitHub org-official READMEs, release notes | Authoritative for the vendor's own product. |
| **5** | Reputable journalism and industry analysts | WSJ, FT, NYT, Reuters, Bloomberg, Gartner, Forrester, IDC reports | Good for context, weak for precision. |
| **6** | General press | Mainstream outlets, trade press, explainer blogs | Directional only. |
| **7** | Community signals | Forums, X/Twitter, Reddit, Discord, blog posts from unidentified authors | Leading indicators, not evidence. |

---

## Conflict-resolution rules

### Rule 1 — Top tier wins
If a tier-1 source says X and a tier-3 source says not-X, X wins. Period. Note the disagreement but do not down-weight the tier-1 source because more lower-tier sources agree with not-X.

### Rule 2 — Within a tier: count sources, but not by volume
If two tier-2 sources disagree, do not pick the majority. Look at methodology, funding, venue. State both and pick one with explicit reasoning.

### Rule 3 — Echo-chamber detection
If N lower-tier sources all trace back to a single originating source, they count as **one** source of that originating tier — not N sources.

Example: five tier-6 blog posts that all cite the same tier-5 analyst report count as one tier-5 source, not five tier-6 sources.

### Rule 4 — Counter-example has asymmetric weight
A single tier-1 or tier-2 counter-example to a claim that is otherwise "industry consensus" deserves more scrutiny than the consensus itself. The DRP source quota (Step D) requires ≥ 1 counter-example source for this reason.

### Rule 5 — Age is a tier modifier
A tier-2 paper from 2019 may be functionally tier-3 in 2026 for a fast-moving domain. Age-adjust when the topic's half-life is short (AI research, security, regulation in flux).

### Rule 6 — Conflict of interest is a tier modifier
A tier-4 vendor doc with a strong financial incentive to make claim X can be demoted to tier-5 for claim X. Note the CoI explicitly in the sources audit.

---

## Worked examples

### Example 1 — The vendor says X, the CVE says Y

- **Claim:** "Product P is secure by default."
- **Source A** (tier 4): product docs say "secure by default".
- **Source B** (tier 1): CVE-2026-XXXXX, CVSS 8.5, affecting default config.

**Resolution:** tier 1 wins. Finding: "Product P has a known CVE in default config; vendor docs claim secure by default but contradicted by [CVE-2026-XXXXX]. Confidence: 0.95. Why high: primary advisory overrides vendor claim."

### Example 2 — Five blogs vs. one peer-reviewed paper

- **Claim:** "Technique T improves performance 40%."
- **Sources A–E** (tier 6): five explainer blogs, all citing "recent research".
- **Source F** (tier 2): the peer-reviewed paper they all cite, showing 12% improvement in a narrow benchmark.

**Resolution:** blogs amplified the number. Record F's 12% figure, tag the blogs as echo-chamber distortion. Confidence: 0.82. Why: single tier-2 source, but no contradicting evidence; consensus amplification does not add evidence weight.

### Example 3 — Two tier-1 sources disagree

- **Claim:** "Compound C is a carcinogen."
- **Source G** (tier 1): IARC classifies as Group 2B ("possibly carcinogenic").
- **Source H** (tier 1): EFSA opinion finds insufficient evidence to classify.

**Resolution:** both are tier 1, different jurisdictions, different methodological standards. Surface both. Pick one with explicit reasoning based on the brief's declared TERRITORY. If TERRITORY = EU, EFSA may carry operational weight; if TERRITORY = global risk, IARC's precautionary framing may dominate. Confidence: 0.65. Why low: tier-1 disagreement, depends on decision framing.

---

## How to flag evidence in a brief

Use compact inline tags after every factual claim:

- `[tier:1]` — direct tier indicator.
- `[consensus:N/M]` — N of M engines confirmed it.
- `[conf:0.XX]` — confidence score.

Full example:

```markdown
Technique T improves performance by 12% on benchmark B [tier:2, consensus:3/5, conf:0.82].
The 40% figure circulating in industry press [tier:6] traces back to the same study
and is a distortion.
```

This format also parses cleanly for the machine-readable `_meta` block and the citation verifier.

---

## When evidence-hierarchy fails

Honest limitations:

- **New domain, no tier-1 sources exist yet.** Sometimes a topic is too new for official bodies to have weighed in. State this explicitly and flag the brief as "interim; re-run when tier-1 sources emerge".
- **Adversarial domains** (politically charged, geopolitical, rapidly evolving). Tiers can be captured. Multiple tier-1 sources may exist from opposing jurisdictions. Surface all, pick explicitly, do not pretend neutrality you don't have.
- **Purely tacit knowledge** (craft, operational know-how). Tier-7 community signals may be the only source of truth. Accept it, flag it, and document how the engine verified across multiple independent voices.
