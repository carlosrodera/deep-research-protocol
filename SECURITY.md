# Security policy

## Supported versions

| Version | Supported |
|---|---|
| 1.0.x   | ✅ |
| < 1.0   | ❌ (pre-release iterations, archived) |

## Reporting a vulnerability

If you discover a security issue — for example, a prompt that can be weaponized to exfiltrate secrets through a DR agent, a citation-verification bypass, or a supply-chain risk in the `scripts/` helpers — **please do not open a public issue**.

Instead:

1. Email **c@carlosrodera.com** with subject `DRP SECURITY: <short title>`.
2. Include:
   - A clear description of the issue and its impact.
   - Reproduction steps — prompt, input file, or command.
   - Any proposed mitigation.
   - Your preferred contact and disclosure timeline.
3. You will receive an acknowledgement within **72 hours**.
4. A fix and an advisory will be prepared within **14 days** for critical issues, **30 days** for non-critical.
5. Credit will be given in the advisory unless you prefer to remain anonymous.

## Out of scope

- Behavior of the underlying Deep Research engines themselves (ChatGPT, Claude, Gemini, Grok, Perplexity). Report those to the respective vendors.
- Hallucinated content in example briefs where the user's responsibility is to run `scripts/verify-citations.py`.

## Supply chain

- No third-party runtime dependencies in the protocol itself; everything is markdown and short Python scripts using the standard library.
- If you fork and add dependencies, use `pip-audit` or `npm audit` in CI and pin versions.

## Data handling

DRP is a **prompt-based protocol**. It does not collect, transmit, or store user data. When you paste the mega-prompt into a Deep Research engine, standard vendor data-handling policies apply. For confidential material, use an enterprise tier of each vendor and consider the guidance in [`docs/integrations.md`](./docs/integrations.md).
