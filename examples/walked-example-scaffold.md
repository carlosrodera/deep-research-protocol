# Walked example scaffold · Esqueleto de ejemplo trabajado

> **This file is a STRUCTURAL SCAFFOLD only.** It shows the shape a completed Deep Agent Protocol walk-through should take, so you can follow the same structure when documenting your own real case. **Do not treat any content here as factual reference.** Replace every `[BRACKETED]` placeholder with your verified, source-cited content.
>
> **Este archivo es un ESQUELETO ESTRUCTURAL.** Muestra la forma que debe tener un caso completo del Deep Agent Protocol, para que sigas la misma estructura al documentar tu propio caso real. **No tomes nada de aquí como referencia fáctica.** Sustituye cada marcador `[ENTRE CORCHETES]` con contenido verificado y citado de tu caso.

---

## Meta

| Field | Value |
|---|---|
| Agent name | `[name of your agent]` |
| Domain | `[domain / sector]` |
| Target users | `[profile, expertise, territory]` |
| Target platform(s) | `[Custom GPT | Claude Project | Claude Skill | Gemini Gem]` |
| Start date → ship date | `[YYYY-MM-DD → YYYY-MM-DD]` |
| Author | `[your name + handle]` |

---

## Phase 1 · Deep research (handoff → consolidation)

**Objective statement:** `[one paragraph restating what the agent must do and for whom]`

**Engines launched in parallel:**
- [ ] ChatGPT Deep Research
- [ ] Claude Deep Research / Claude + web search
- [ ] Gemini Deep Research
- [ ] Grok DeepSearch
- [ ] Perplexity Pro

**Raw reports saved at:** `workspace/research/raw/research-<platform>.md`

**Consolidation output:** `workspace/research/consolidated.md`

**Key findings (high-confidence, ≥ 3 engines agree):**
1. `[finding]` — confidence `[0.0–1.0]` — sources `[N]`
2. `[finding]` — confidence — sources
3. `[finding]` — confidence — sources

**Discrepancies surfaced & how resolved:**
- `[discrepancy]` → resolved via `[primary source URL]`.

**Gaps filled manually with primary sources:**
- `[source name, URL, date downloaded]`
- `[source name, URL, date downloaded]`

---

## Phase 2 · Knowledge base

**Layout used:**
```
knowledge-base/
├── 00-index.md
├── 00-index.json        (optional — vector lookup hints)
├── [topic-1].md
├── [topic-2].md
└── [primary-sources]/
```

**Indexing choice:** `[single monolithic index | per-topic index | hybrid]` — why: `[rationale]`

**Largest file:** `[size in words, why this size]`

**Naming convention:** `[e.g. snake_case with jurisdiction suffix]` — why: `[rationale]`

---

## Phase 3 · Master prompt (11-block structure)

Final master prompt lives at: `workspace/master-prompt.md`

Block-by-block notes on design decisions:

1. **Role & identity** — `[what you declared and why]`
2. **Primary objective** — `[one-sentence mandate]`
3. **Audience profile** — `[assumed knowledge, tone]`
4. **Knowledge-base protocol** — `[exact rule forcing file consultation]`
5. **Output format** — `[markdown structure, citation rules]`
6. **Reasoning rules** — `[chain-of-thought, step-by-step, etc.]`
7. **Guardrails & refusals** — `[out-of-scope handling]`
8. **Escalation paths** — `[when to defer to a human / primary source]`
9. **Self-check** — `[pre-response verification]`
10. **Few-shot examples** — `[how many, why these]`
11. **Language policy** — `[fixed language | auto-match user]`

---

## Phase 4 · Implementation

**Platform chosen:** `[…]` — why: `[…]`

**Uploaded files / configured instructions:**
- `[file → role]`

**Platform-specific quirks encountered:**
- `[quirk]` → `[workaround]`

**Deployment notes in:** `workspace/deployment.md`

---

## Phase 5 · Testing & iteration

**Test battery size:** `[N]` realistic queries.

**Results summary:**
| # | Query | Expected behavior | Result | Pass/Fail | Fix applied |
|---|---|---|---|---|---|
| 1 | `[…]` | `[…]` | `[…]` | ✅/❌ | `[…]` |

**Iteration triggers hit:**
- `[e.g. hallucinated citation → tightened KB-consultation rule]`

**Post-ship maintenance cadence:** `[weekly | monthly | quarterly]`

---

## Lessons learned

- `[what you'd do differently next time]`
- `[unexpected platform limitation]`
- `[surprising win]`

---

## License & attribution

If you publish your walked example back to the community, default to MIT or CC-BY-4.0, and credit the **Deep Agent Protocol** — `github.com/carlosrodera/deep-agent-protocol`.
