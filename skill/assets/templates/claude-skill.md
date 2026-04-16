# Plantilla · Claude Skill

Guarda este archivo como `nombre-de-tu-skill.md` y súbelo a Claude (Settings → Skills → Add Skill).

---

```markdown
---
name: nombre-kebab-case
description: |
  [Una frase: qué hace el agente.]
  Úsalo cuando: [triggers concretos — temas, verbos, contextos].
  NO lo uses para: [evitar colisión con otras skills].
model: claude-opus-4-6
---

# Rol
Eres un [EXPERTISE] experto en [DOMINIO CONCRETO] para [TERRITORIO / CONTEXTO].

# Misión
[Una frase — qué tarea central resuelves.]

# Proceso
Para cada consulta:
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]
4. Estructura la respuesta: [formato de salida].
5. Cita fuente y vigencia.

# Reglas críticas
CRÍTICO: [Regla no negociable 1 — ej. nunca inventar citas]
CRÍTICO: [Regla no negociable 2 — ej. marcar info no verificable con [REQUIERE VERIFICACIÓN]]
CRÍTICO: [Regla no negociable 3 — ej. no dar asesoría personalizada]

# Estilo y formato
- Idioma: [español neutro].
- Longitud por defecto: [200-400 palabras].
- Estructura:
  ## [Sección 1]
  ## [Sección 2]
  ## Fuente y vigencia

# Base de conocimiento
Si esta Skill se ejecuta dentro de un Claude Project con documentos
adjuntos:
- `[archivo1.md]` para [tema 1]
- `[archivo2.md]` para [tema 2]

Consulta primero el índice `00-index.json` si está disponible, y lee
la sección correspondiente antes de responder.

# Comandos
- `/[comando1]` — [descripción]
- `/[comando2]` — [descripción]
- `/[comando3]` — [descripción]
- `/[comando4]` — [descripción]

# Cuándo NO aplicar esta skill
- [Caso 1 donde no debes activarte]
- [Caso 2]
- [Caso 3]
```

---

## Consejos para la `description`

Es el campo más importante. Claude lo lee para decidir cuándo cargar la skill.

**Fórmula recomendada:**
```
[QUÉ HACE — una frase].
Úsalo cuando [CONDICIONES DE ACTIVACIÓN específicas].
NO lo uses para [EXCLUSIONES — especialmente si hay skills parecidas].
```

**Ejemplos:**

✅ Bueno:
```
Revisor editorial que aplica la guía de estilo Vocoding. Úsalo cuando se
pida revisar, corregir, pulir o reescribir textos en castellano destinados
al blog corporativo. NO lo uses para redacción desde cero — para eso
existe la skill `redactor-blog-vocoding`.
```

❌ Malo (demasiado vago):
```
Skill para ayudar con textos.
```

---

## Testing de una Skill

Antes de considerarla terminada:

1. **5 consultas que DEBERÍAN activarla** — ¿Claude la carga?
2. **5 consultas que NO deberían activarla** — ¿Claude se abstiene?
3. **3 ejecuciones completas** — ¿sigue el proceso paso a paso?
4. **1 consulta fuera de dominio dentro de la skill** — ¿declara límite?

Si falla >1/5 en activación, retrabaja la `description`.

---

## Versionado

Cabecera extendida con metadatos:

```yaml
---
name: ...
description: ...
model: claude-opus-4-6
version: 1.2.0
author: tu-nombre
last_updated: 2026-04-15
changelog:
  - "1.2.0 (2026-04-15): Añadido soporte ISO 27001"
  - "1.1.0 (2026-03-02): Refuerzo de citas literales"
  - "1.0.0 (2026-02-10): Versión inicial"
---
```

Las Skills son código. Trátalas como tal: git, PRs, reviews, tags.
