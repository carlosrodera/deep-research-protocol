# Use-case contribution template

> Use this when you want to submit a new use case to DRP (`use-cases/<slug>/README.md`). The goal: show how DRP's output feeds your specific deliverable, with real commands and source-cited outputs.

---

## File & folder convention

- Folder: `use-cases/<slug>/` (kebab-case, singular — e.g. `vendor-due-diligence`, `policy-briefing`, not `due-diligences`).
- Minimum files:
  - `README.md` — this template filled.
  - `brief-skeleton.md` — the shape of the final deliverable (not a real one — that goes in `examples/`).
  - optional `example-brief.md` — a real, source-cited example, **URLs verified with `scripts/verify-citations.py`**.

---

## `README.md` skeleton — fill every placeholder

```markdown
# `<Use case name>`

> One-sentence pitch. What does DRP let you ship in this use case that single-engine DR does not?

## When to pick this

Three bullets describing the situation where this use case is the right fit. Be concrete — who uses it, what decisions it unblocks, what goes wrong without it.

## Inputs

- **USER_QUERY shape:** describe the class of question this use case answers.
- **AUDIENCE:** who consumes the deliverable.
- **TERRITORY:** typical jurisdiction constraints.
- **DEPTH:** overview or deep.
- **DOMAIN_VARIANT:** A / B / C (see [`research-prompt.md`](../../research-prompt.md)).

## Pipeline

Describe step-by-step how a DRP run maps onto this deliverable.

1. **Phase 1 — Research.** Any specific platform variants or source quotas that differ from the canonical?
2. **Phase 2 — Consolidation.** Vanilla or chained with [`anti-echo-prompt.md`](../../templates/anti-echo-prompt.md)?
3. **Phase 3 — Transform.** How do you turn the consolidated brief into this deliverable's format? Scripts? Templates?
4. **Phase 4 — Delivery.** What does the final output look like? Markdown? PDF? A Custom GPT? A Notion page?

## Deliverable shape

Describe the shape of the final artifact. Link the skeleton file.

## Quality gates specific to this use case

List any additional gates beyond the canonical DRP Step I — e.g. "every regulatory citation must include article number + date of most recent amendment".

## Common failure modes

What goes wrong in practice? What has the community learned from applying DRP here?

## Example

Link to an example under `use-cases/<slug>/example-brief.md`. **The example must pass `scripts/verify-citations.py` or it gets removed.**

## Related use cases

Cross-link to other use cases that chain with this one.
```

---

## Honesty rules

1. **No fabricated examples.** If you cannot publish a real one (confidentiality), say so and leave the example slot empty. Shipping fake examples damages the protocol's credibility.
2. **URLs must resolve.** Run `python scripts/verify-citations.py <your-file>` on every file you contribute.
3. **Scope discipline.** One use case = one deliverable. If your pipeline produces two different deliverables, that's two use cases.

## Submission

Open an issue with template `📑 Use case submission` first, then a PR. Small, focused.
