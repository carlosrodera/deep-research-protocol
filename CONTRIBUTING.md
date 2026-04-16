# Contributing to the Deep Research Protocol

Thanks for considering a contribution. The goal is to keep this method **honest, reproducible, and genuinely useful** — not to accumulate features. Small, focused PRs win.

---

## 🇬🇧 English

### What we want

- **New use cases.** Document them against [`templates/use-case-template.md`](./templates/use-case-template.md). Must include source-cited inputs, a worked consolidation excerpt, and the confidence ledger.
- **Domain variants** for the mega-prompt — biomedical, foreign-jurisdiction legal, hardware, fintech, cybersecurity, DevOps.
- **Platform variants** for new Deep Research engines as they appear.
- **Localizations** of the mega-prompt for non-English markets (`templates/research-prompt.<lang>.md`).
- **Walked examples** using [`examples/walked-example-scaffold.md`](./examples/walked-example-scaffold.md). Every numeric claim and citation must resolve. Run [`scripts/verify-citations.py`](./scripts/verify-citations.py) before submitting. **Fabricated examples are rejected.**
- **Integrations** — new export targets in [`docs/integrations.md`](./docs/integrations.md).
- **Bug fixes** and reference clarifications.

### What we do NOT want

- Features the method does not need. "Design for hypothetical future requirements" is a defect in this repo.
- Content written from parametric memory without source citations.
- Provider-specific branding beyond what already exists. DRP is platform-agnostic by design.
- "Why don't we also build a full DR agent?" — No. DRP is a meta-protocol. That's the point.

### How to submit

1. **Fork** and branch from `main` with a descriptive name (`feat/domain-variant-biomedical`, `fix/citation-verifier-regex`, `docs/integration-notion`).
2. **Keep PRs small and focused.** One concern per PR.
3. **Cross-update the docs.** If you change a template, update the matching reference. If you add a use case, link it from the README matrix.
4. **Verify citations.** If your PR introduces any claim with a URL, run `python scripts/verify-citations.py <your-file>` and paste the result in the PR description.
5. **Open the PR** with a clear "what + why". Screenshots or excerpts help.

### Review standards

- **Clarity.** No vague filler, no hype, no marketing words.
- **Specificity.** Concrete commands, real URLs, real data.
- **Reproducibility.** If I re-run your example with the stated inputs, I should get substantially the same output.
- **Scope discipline.** If the PR grows beyond its title, split it.

### Style

- Markdown with `##` for top-level sections inside each doc. `#` reserved for the doc title.
- Code blocks with language hints (```python, ```bash, ```yaml…).
- Tables for comparisons.
- `kebab-case.md` for filenames.
- Sentence-case headings.
- English is primary. Non-English content goes in parallel files (`research-prompt.es.md`, not English with inline Spanish).
- Cite every source with full URL and date.

### License

By submitting a PR you agree your contribution is released under the MIT License.

---

## 🇪🇸 Español

### Qué aceptamos

- **Use cases nuevos.** Documentados contra [`templates/use-case-template.md`](./templates/use-case-template.md). Con inputs citados, ejemplo real de consolidación y tabla de confidence.
- **Variantes de dominio** del mega-prompt — biomédico, legal de otra jurisdicción, hardware, fintech, ciberseguridad, DevOps.
- **Variantes de plataforma** para nuevos motores de Deep Research.
- **Localizaciones** del mega-prompt (`templates/research-prompt.<idioma>.md`).
- **Walked examples** usando el scaffold. Cada URL debe resolver — pasa `scripts/verify-citations.py` antes de enviar. **Los ejemplos inventados se rechazan.**
- **Integraciones** — nuevos destinos de export en `docs/integrations.md`.
- **Fixes** y clarificaciones.

### Qué NO aceptamos

- Features que el método no necesita.
- Contenido de memoria paramétrica sin fuente.
- Branding de un proveedor concreto. DRP es platform-agnostic.
- "Construyamos también nuestro propio DR agent" — No. DRP es un meta-protocolo, ese es el punto.

### Cómo enviar

1. **Fork** + rama descriptiva (`feat/variante-biomedica`, `fix/verificador-urls`, `docs/integracion-notion`).
2. **PRs pequeños y enfocados.** Una preocupación por PR.
3. **Actualiza docs cruzados.** Si tocas un template, actualiza su reference. Si añades un use case, enlázalo desde el README.
4. **Verifica citas.** Si tu PR introduce URLs, ejecuta `python scripts/verify-citations.py <tu-archivo>` y pega el resultado en el PR.
5. **Abre el PR** con un "qué + por qué" claro.

### Estándares de review

- **Claridad.** Sin relleno vago, sin hype, sin marketing.
- **Especificidad.** Comandos concretos, URLs reales, datos reales.
- **Reproducibilidad.** Si re-ejecuto tu ejemplo con tus inputs, debo obtener sustancialmente el mismo output.
- **Disciplina de scope.** Si el PR crece más allá de su título, divídelo.

### Estilo

- Markdown con `##` para secciones. `#` reservado para el título del doc.
- Bloques de código con lenguaje.
- Tablas para comparativas.
- `kebab-case.md`.
- Mayúscula solo al inicio de los títulos.
- Inglés primario. Contenido en otro idioma en archivos paralelos, no mezclado.
- Cada fuente con URL y fecha completas.

### Licencia

Al enviar un PR aceptas publicación bajo MIT.

---

## Contact

Open an issue. Or reach out on X [@carlosrodera_](https://x.com/carlosrodera_).
