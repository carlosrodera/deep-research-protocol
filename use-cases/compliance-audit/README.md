# Use case: Compliance audit

> **Jurisdiction-aware compliance map with primary-source citations. DRP + Variant B (Regulatory) + manual primary-source verification.**

---

## When to pick this

- You need to demonstrate **compliance** against a specific regulatory framework in a specific jurisdiction.
- Auditors, legal, or regulators will read the output. Every claim must trace to a primary legal text.
- Parametric-memory claims about regulation are **categorically unacceptable** — you need the actual articles, dates, and amendments.

---

## Inputs

- `workspace/research/consolidated.md` — DRP run with **Variant B (Regulatory / Legal / Standards)**.
- `workspace/research/primary-sources/` — downloaded official texts (BOE / EUR-Lex / Federal Register / ISO / vendor compliance docs).
- A clear declaration of **applicable jurisdiction** and **as-of date**.

---

## Deliverable shape

```
## Executive summary            (compliance posture at a date, key risks)
## Scope                        (what is in and out of scope + jurisdiction)
## Applicable framework(s)      (primary legal texts cited with article + date)
## Requirements map             (each requirement → current state → evidence → gap)
## Findings                     (per requirement: compliant / partial / non-compliant)
## Remediation plan             (prioritized, with ownership and deadline)
## Open interpretive questions  (grey zones with acknowledged ambiguity)
## Appendix: primary sources    (full texts archived with retrieval date)
```

A compliance audit's single strongest feature is the **requirements map** table — every regulatory requirement listed, with the current state of compliance and the evidence.

---

## Pipeline

1. Run DRP with Variant B (Regulatory). Specify the jurisdiction explicitly in `TERRITORY`.
2. **Download every cited primary source** — do not rely on engine quotes. The legal text itself must be in `primary-sources/`.
3. Manually verify each cited article number and amendment date against the primary source. Engines are known to confuse article numbers, especially across amendments.
4. Build the requirements map. One row per requirement. One or more rows per cited article.
5. Classify each row: compliant / partial / non-compliant / not-applicable.
6. Every "compliant" row requires **positive evidence** — not "we assume we comply".
7. Generate remediation plan from non-compliant and partial rows.
8. Submit to legal counsel for review. DRP is input to their work, not a substitute.

---

## Specific quality gates (beyond DRP Step I)

- Every cited article has: **official text URL** + **retrieval date** + **specific article / section number** + **most-recent amendment date**.
- Every "compliant" row has a pointer to concrete evidence (policy, contract, system config, training record).
- Every "partial / non-compliant" row has an **owner** and a **target date** for remediation.
- Jurisdiction declared in `_meta.territory`. Brief invalidated if reader operates in a different jurisdiction.
- Flagged "as-of date"; brief requires re-run if regulation changed after that date.

---

## Common failure modes

- **Paraphrased regulation.** Engine says "Article 5 requires risk assessment". Primary text says "risk analysis". These are not the same word with the same legal meaning. Always quote the primary text verbatim.
- **Stale amendments.** Engine cites the regulation as of its training cutoff. Regulation has been amended. Always check the official consolidated version.
- **Cross-jurisdictional confusion.** Engine mixes EU and US provisions. Variant B plus explicit `TERRITORY` counteracts; still verify every article has the right flag.
- **"We are compliant" without evidence.** Shift the burden: every compliant row must link to evidence.
- **Confusing DRP with legal advice.** DRP produces an evidentiary base. A qualified lawyer in the jurisdiction signs off. Keep that line bright.

---

## Chain with other use cases

- **compliance-audit → agent-building** — findings become the KB for a compliance-specialist agent that answers "are we compliant on X?" with primary-source citations.
- **compliance-audit → strategic-brief** — major non-compliance findings feed strategic decisions (market exit, product redesign, acquisition risk).

---

## Example

Contribute a real, anonymized example via PR. The example must include the requirements-map table and pass `verify-citations.py`.
