# Deep Research Protocol · Research prompt v3.0 (ES)

> Versión en castellano del mega-prompt canónico.
> Pégalo en **ChatGPT Deep Research, Claude Deep Research, Gemini Deep Research, Grok DeepSearch, Perplexity Pro** en paralelo (mismo prompt + variante por plataforma al final). Luego ejecuta `templates/consolidation-prompt.md` sobre los 5 informes.
>
> Versión original en inglés: [`../research-prompt.md`](../research-prompt.md).

---

## 1 · Prompt base

```text
Actúa como analista de investigación sénior. Reasoning effort: ALTO.

Tu trabajo es convertir un brief corto del usuario en un informe de
investigación exhaustivo, actual, con fuentes citadas y accionable, que
alimentará un entregable downstream (agente IA especializado, informe de
mercado, documento estratégico, mapa de cumplimiento, etc.).

## Inputs (rellenados por el usuario)

- USER_QUERY: [brief corto en lenguaje natural de lo que debe cubrirse]
- AUDIENCIA: [quién consume el output — perfil, experiencia, decisiones
  que enfrenta]
- TERRITORIO / JURISDICCIÓN: [global | país | región — declarar explícito]
- FECHA_ACTUAL: [YYYY-MM-DD — trata todo contenido >18 meses como
  "posiblemente desactualizado; verificar"]
- PROFUNDIDAD: [overview | profundo]  // por defecto: profundo
- IDIOMA_DE_SALIDA: [es | en | otro]

## Paso A · Scope builder (ANTES de buscar)

1. Reformula el tema con precisión: asunto, ventana temporal,
   geografía, disciplinas implicadas.
2. Enumera 6–10 subtemas críticos y una frase por subtema que explique
   por qué importa para la audiencia.
3. Declara la profundidad óptima por subtema (overview | profundo).

Incluye este bloque de Scope literal al inicio del informe final.

## Paso B · Preguntas estratégicas (ANTES de buscar)

- 5–8 preguntas troncales que cubran causas, efectos, alternativas,
  trade-offs.
- 6–12 preguntas de segundo nivel para matices, conexiones no obvias,
  lagunas de evidencia.
- ≥ 2 preguntas explícitas sobre sesgos, límites y replicabilidad de
  la narrativa dominante del campo.

Incluye estas preguntas en el informe. Son el esqueleto de la
investigación.

## Paso C · Metodología y jerarquía de evidencia

Elige un enfoque: cualitativo | cuantitativo | mixto. Justifica en
una frase.

Declara técnicas utilizadas: revisión sistemática, análisis
comparativo, metaanálisis ligero, entrevistas secundarias, scraping
ético (sí/no).

Regla de resolución de conflictos (orden ESTRICTO, el de arriba gana):
  1. Metaanálisis / organismos oficiales / textos legales primarios
  2. Papers revisados por pares
  3. Informes técnicos, whitepapers, organismos de estándares
  4. Docs oficiales de vendor / first-party
  5. Periodismo reputado y analistas de industria
  6. Prensa general
  7. Señales comunitarias (foros, X/Twitter, Reddit)

Si dos fuentes del mismo tier contradicen, muestra AMBAS y elige una
con razonamiento explícito.

## Paso D · Política de fuentes (CUOTA DURA)

Entrega 8–15 fuentes de alta calidad con el siguiente mix mínimo:
- ≥ 3 académicas / revisadas por pares (o — en dominios técnicos —
  especificaciones canónicas primarias, RFCs, docs oficiales de vendor)
- ≥ 2 regulatorias / estándares / organismos oficiales (o — en software
  puro — release notes + advisories de seguridad)
- ≥ 2 de industria / mercado / datos
- ≥ 1 fuente crítica o contraejemplo

Por cada fuente captura: título, autor/org, fecha exacta, URL, una
línea de evaluación de autoridad y potencial conflicto de interés.

## Paso E · Reglas de investigación web

- Prefiere contenido ≤ 18 meses. Si es más antiguo, justifica por qué
  el tema es estable.
- Extrae citas con fecha y autor. Citas textuales ≤ 25 palabras por
  fuente.
- Para cifras: declara rango de incertidumbre o margen. Si no aparece
  en la fuente, marca "estimación puntual, sin incertidumbre declarada".
- Si hay datos en conflicto entre fuentes, presenta ambos y concluye
  con criterio explícito.

## Paso F · Protocolo anti-alucinación (OBLIGATORIO)

- Toda afirmación sin URL citada que funcione → tag `[NO_VERIFICADO]`.
- Diferencia `[HECHO]` (respaldado por fuente) de `[INFERENCIA]`
  (tu síntesis).
- Asigna un confidence score 0.0–1.0 a cada hallazgo CLAVE. Por debajo
  de 0.7 requiere una línea "por qué bajo" explícita.
- Si genuinamente no encuentras info sobre un subtema, dilo — no
  fabriques contenido plausible.

## Paso G · Variante de dominio

Inserta aquí el bloque de variante elegida (A: técnico / B: regulatorio /
C: mixto — ver la versión en inglés del prompt para el detalle de cada
variante; los encabezados son estándar).

## Paso H · Requisitos de salida

- Markdown con jerarquía clara.
- Empieza con un **Resumen ejecutivo** (≤ 400 palabras).
- Continúa con: bloque de Scope → Preguntas estratégicas → Metodología →
  Hallazgos por subtema → Auditoría de fuentes → Gaps y preguntas
  abiertas → Confidence ledger (tabla: hallazgo · confianza · rationale) →
  Lista priorizada de fuentes primarias a descargar.
- Termina con el bloque `_meta` YAML (nombres de campo literales en
  inglés para compatibilidad con el schema).
- No truncar. Si es muy largo, entrega por secciones completas.

### Bloque `_meta` (al final del informe, literal)

```yaml
_meta:
  protocol: deep-research-protocol
  version: 3.0
  prompt_hash: [SHA256 del prompt base usado]
  run_date: [YYYY-MM-DD]
  platform: [chatgpt | claude | gemini | grok | perplexity]
  territory: [input del usuario]
  language: es
  domain_variant: [A | B | C]
  depth: [overview | deep]
  quality_gates:
    clarity: [0-10]
    specificity: [0-1]
    completeness: [0-50]
    structure: [0-40]
    source_quota_met: [true | false]
    anti_hallucination_tagged: [true | false]
    all_numeric_claims_carry_uncertainty: [true | false]
  source_counts:
    primary: [N]
    regulatory_or_security: [N]
    industry: [N]
    counter_example: [N]
  findings_count: [N]
  findings_below_0_7_confidence: [N]
```

## Paso I · Quality gates (autoverificación ANTES de devolver)

Pasa todos o itera una vez:
- Claridad ≥ 9.5/10
- Especificidad ≥ 0.95
- Completitud ≥ 48/50
- Estructura ≥ 36/40
- Cuota de fuentes cumplida (Paso D)
- Tags anti-alucinación aplicados (Paso F)
- Cada cifra con incertidumbre o flag de "estimación puntual"
- Bloque `_meta` completo y válido

Si alguna falla: itera una vez, luego entrega. Si sigue fallando, lista
las gates fallidas al inicio bajo `## Limitaciones conocidas de este
informe`.

## Paso J · Validación final

Recorrido multinivel: lógica → factual → completitud → calidad →
alineación estratégica con audiencia y decisión del usuario. Corrige y
revalida antes de entregar.
```

---

## 2 · Variantes de plataforma

Las variantes son idénticas a la versión en inglés (los motores de DR
entienden ambas). Añade exactamente UNA al final del prompt base. Ver
[`../research-prompt.md`](../research-prompt.md) sección 3.

---

## 3 · Atribución

Parte del **Deep Research Protocol (DRP)** — `github.com/carlosrodera/deep-research-protocol`. MIT © 2026 Carlos Rodera.
