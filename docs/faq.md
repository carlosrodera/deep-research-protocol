# FAQ

Common questions about the Deep Research Protocol.

---

## General

### Is this just a prompt?

No. The mega-prompt is the **headline artifact** but the protocol includes:

- Cross-platform consolidation mechanics.
- Citation-verifier script.
- Machine-readable output schema.
- Anti-echo variant.
- Use-case library (agent building, market report, strategic brief, compliance audit).
- Localizations.

The prompt alone is ~15% of the value. The protocol around it is the rest.

### How long does a full DRP pass take?

- **Setup:** 5 minutes (filling inputs, selecting domain variant).
- **Parallel launch:** 5 minutes (pasting into 5 tabs).
- **Engine runtime:** 5–20 minutes per engine, but they run in parallel — so ~20 minutes elapsed.
- **Consolidation:** 5–10 minutes of reading + running the consolidation prompt.
- **Citation verification:** 1–3 minutes (automated).
- **Primary-source download:** 10–30 minutes depending on scope.

**Total:** ~45–90 minutes of elapsed time, ~20–30 minutes of active attention.

Compared to "one engine, one prompt, copy-paste the output": DRP costs 3–5× more time and delivers an order-of-magnitude better artifact.

### Do I really need 5 engines?

No. **2 is the minimum viable**, 3 is the threshold where consensus emerges, 4–5 is ideal. Below 2, there is no cross-validation.

### What if I only have free tiers?

You can run DRP across free / minimal tiers of multiple engines. The total monthly cost for 4–5 engines at the lowest paid tier as of April 2026 is ~$60–100 — cheaper than a single enterprise DR tool, and you own the output.

### What if I don't have Grok?

Skip it. Grok contributes real-time X/Twitter signal; for most briefs, the other four are sufficient. The protocol is designed to degrade gracefully. Mark `engines_used` in the `_meta` block accordingly.

### Is it bilingual?

The primary prompt is English. A canonical Spanish version ships at [`templates/research-prompt.es.md`](../templates/research-prompt.es.md). Community localizations to other languages are welcome — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---

## Methodology

### Why not just use one engine with a better prompt?

Because single-engine bias is not a prompt problem. It is a **training data** and **retrieval stack** problem. No prompt fixes a retrieval stack that never indexed the source you need.

### Why five, not three, not ten?

See [`methodology.md`](./methodology.md#2--why-five-engines-not-one-not-ten). Summary: 4–5 is the sweet spot between robustness and coordination cost.

### The engines disagree a lot — what do I do?

That is the protocol working. Disagreement is evidence that your topic has genuine uncertainty. Run the [`consolidation-prompt.md`](../templates/consolidation-prompt.md) — it surfaces discrepancies with explicit evidence-hierarchy resolution. For strategic decisions, chain with [`anti-echo-prompt.md`](../templates/anti-echo-prompt.md).

### The engines all agree — am I done?

Maybe. Maybe not. Consensus across 5 engines is meaningful only if they cite **different primary sources**. If all 5 cite the same Wikipedia article, you have an echo chamber, not consensus. Run the anti-echo pass to surface this.

### Where does "confidence 0.7" come from?

Empirical heuristic from consulting work: below 0.7, the claim has failed at least one of (cross-validation, high-tier source, uncertainty disclosure). Above 0.7, the claim is safe to use in a decision. See [`confidence-scoring.md`](./confidence-scoring.md) for the full rubric.

---

## Tooling

### What does `scripts/verify-citations.py` actually do?

It extracts every URL from your Markdown brief, sends HEAD (fallback GET) requests, and classifies each as:

- **resolved** — HTTP 2xx or 3xx. Exists.
- **broken** — HTTP 4xx. Likely hallucinated.
- **transient** — timeout or 5xx. Retry later.

It is a **cheap filter, not a semantic checker**. A resolving URL may still cite the wrong page. Human verification of tier-1 claims is non-negotiable.

### Can it verify that a cited URL supports the claim made about it?

Not yet. That is planned for v1.1 (LLM-as-a-judge step that reads the URL and checks claim-source alignment). For now: the verifier only confirms the URL exists.

### Can I run verify-citations.py in CI?

Yes. Exit code `0` if all citations resolve; `1` if any are broken. Add it as a GitHub Actions check on PRs.

### What's in the `_meta` block for?

Machine consumption. Automated QA, longitudinal diffing, portfolio dashboards, agent integration. See [`methodology.md`](./methodology.md#8--the-machine-readable-_meta-block).

---

## Use cases

### I want to build a custom GPT / Claude Project — where do I start?

Run the full DRP to produce a consolidated brief, then go to [`use-cases/agent-building/`](../use-cases/agent-building/) for the 5-phase agent method (knowledge base → master prompt → platform implementation → testing).

### Can I use DRP for non-research work?

DRP is specifically a **research-method**. Its outputs feed any deliverable that depends on verified evidence: agent KBs, reports, strategy briefs, compliance maps. For non-research work (content generation, creative writing, general chat) it's overkill.

### Is there a use case for me?

See [`use-cases/README.md`](../use-cases/README.md). If none fit, open a use-case submission issue.

---

## Enterprise / security

### Can I run DRP on confidential material?

Depends on the engines' enterprise tiers. Most vendors offer zero-retention / no-training-on-data options at enterprise tiers. The DRP methodology does not itself leak data — you control which engines you paste into.

For genuinely sensitive work, consider a **private-mode DRP**: run 2–3 passes on an on-prem / Azure-OpenAI / AWS-Bedrock setup with enterprise DPAs, and use the consolidation prompt in your own controlled environment. Variant coming in a future release.

### Is there a data-processing agreement?

No — DRP is a method, not a hosted service. The repo does not collect or transmit anything.

### How do I cite DRP in a published report?

```
"Evidence synthesized via the Deep Research Protocol v1.0 (Rodera, 2026),
github.com/carlosrodera/deep-research-protocol."
```

Or however your house style prefers. MIT license — no permission required.

---

## Contributing

### I built an agent / report / audit with DRP — can I share it?

Yes, please. Open a **📑 Use case submission** issue and follow [`templates/use-case-template.md`](../templates/use-case-template.md). All citations must resolve (run the verifier).

### Can I commercialize DRP?

Yes. MIT license. Fork it, remix it, sell derivative products or consulting. Attribution appreciated but not required.

### Where do I report bugs or suggest improvements?

GitHub Issues with the relevant template (🐛 bug report / ✨ feature request / 📑 use case submission).

### Community chat?

Not yet. If demand justifies it, we'll stand up a GitHub Discussion board first, Discord later. For now: Issues + DMs on [@carlosrodera_](https://x.com/carlosrodera_).
