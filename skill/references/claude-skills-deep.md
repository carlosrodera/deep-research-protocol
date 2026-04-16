# 08 · Avanzado · Claude Skills

Las **Skills** son el formato de agente más portable y potente para quien vive en el ecosistema Anthropic. Este capítulo va a fondo.

---

## Qué es una Skill (en serio)

Una Skill es un archivo `.md` con dos partes:

1. **Cabecera YAML (frontmatter)** — nombre, descripción, y opcionalmente modelo recomendado.
2. **Cuerpo** — instrucciones en lenguaje natural.

Claude carga la Skill automáticamente cuando detecta, en cualquier conversación o proyecto, que la consulta encaja con la `description`. También se pueden invocar con `/skill nombre`.

```markdown
---
name: revisor-editorial
description: Revisor editorial que aplica guía de estilo [nombre]. Úsalo cuando se pida revisar, corregir o mejorar textos siguiendo el manual de estilo de [nombre].
model: claude-opus-4-6
---

# Rol
Eres un revisor editorial experto aplicando el manual de estilo...
```

---

## Diferencia clave con un Custom GPT

| | Custom GPT | Claude Skill |
|---|------------|--------------|
| Alcance | Una conversación nueva aislada | Cualquier conversación o proyecto existente |
| Contexto | Se pierde al cerrar | Se carga encima del contexto actual |
| Base de conocimiento | Se adjunta al GPT | La provees en el proyecto/conversación |
| Activación | Abres el GPT manualmente | Claude la carga sola por `description` |
| Compartir | Link público | Archivo `.md` (o marketplace privado de tu org) |

**La mejor metáfora:** un GPT es un **aula** (entras y sales); una Skill es una **habilidad** que Claude añade a lo que ya estaba haciendo.

---

## Anatomía de una Skill excelente

### 1. Nombre
Kebab-case, descriptivo, sin "ai" ni "gpt" al final.

```
revisor-editorial-castellano
analista-legal-seguridad-privada-es
generador-propuestas-comerciales
```

### 2. Description (la parte que Claude lee para decidir cuándo cargarla)
Tres elementos:

1. **Qué hace** en una frase.
2. **Cuándo usarla** con triggers concretos (qué verbos, qué temas, qué contextos).
3. **Cuándo NO usarla** si hay ambigüedad con otra Skill.

❌ **Mala:** "Asistente de redacción."
✅ **Buena:** "Revisor editorial que aplica la guía de estilo [X]. Úsalo cuando se pida revisar, corregir, pulir o mejorar textos en castellano que vayan a publicarse en el blog corporativo. NO lo uses para redacción desde cero — para eso existe `redactor-blog`."

### 3. Cuerpo de la Skill
Aquí va el prompt maestro de 11 bloques (ver [capítulo 5](05-fase3-prompt-maestro.md)). Recomendación extra:

- **Empezar con "Rol + Misión"** muy corto y afirmativo.
- **Proceso de trabajo en pasos numerados.**
- **Reglas "duras"** en mayúsculas o con prefijo CRÍTICO:
  ```markdown
  CRÍTICO: Nunca inventes una cita. Si no dispones del texto literal del artículo, escribe [REQUIERE VERIFICACIÓN].
  ```

---

## Patrones útiles

### Skills encadenables
Skills pequeñas y enfocadas se combinan mejor que una monolítica. Prefiere:

- `extractor-requisitos-ley` (extrae obligaciones de un texto legal)
- `checklist-cumplimiento` (convierte requisitos en checklist)
- `redactor-informe-compliance` (escribe informe a partir de checklist)

…a una sola Skill de 4.000 palabras que hace todo.

### Skill + Project
**Patrón estrella:**

- **Project** con la base de conocimiento dura (leyes, normas, documentos internos).
- **Skills** sueltas con procesos reutilizables (revisar, comparar, generar informe).

Cuando trabajas dentro del Project, cualquier Skill queda disponible y tiene acceso al conocimiento del Project.

### Skill con "herramientas" vía MCP
Puedes combinar Skills con servidores MCP (ver [capítulo 9](09-avanzado-mcp.md)): una Skill describe el proceso, y dentro del proceso invoca MCPs (Brave Search, Linear, Gmail…).

---

## Ejemplo comentado

```markdown
---
name: analista-ley-seguridad-privada-es
description: |
  Analiza consultas sobre la Ley 5/2014 de Seguridad Privada y normativa ISO
  asociada (28000, 18788, 22301) en España. Úsalo cuando la consulta mencione
  seguridad privada, vigilantes, cámaras de videovigilancia en comercios,
  empresas de seguridad, o cumplimiento ISO del sector. NO lo uses para
  protección de datos genérica (RGPD) — para eso existe `analista-rgpd-es`.
model: claude-opus-4-6
---

# Rol
Eres un analista experto en cumplimiento normativo del sector de seguridad
privada en España.

# Proceso
Para cada consulta:
1. Identifica tema y palabras clave.
2. Consulta `00-index.json` si está disponible en el Project.
3. Lee la(s) sección(es) relevante(s).
4. Responde con estructura: Resumen · Marco legal · Ejemplo · Fuente.
5. Si la norma se actualizó hace >12 meses, advierte.

# Reglas críticas
- CRÍTICO: Cita siempre artículo/norma + fecha de vigencia.
- CRÍTICO: Si no puedes verificar con fuente, marca [REQUIERE VERIFICACIÓN].
- No das asesoría legal personalizada — recomienda consultar abogado.

# Formato
Markdown, 250–400 palabras por defecto.

## Resumen
## Marco aplicable
## Ejemplo práctico
## Fuente y vigencia
```

---

## Distribución de Skills

- **Individual:** compartir el `.md` por email, Slack o git.
- **Equipo:** repositorio git con `/skills/`, que cada miembro clona y carga.
- **Empresa:** algunas organizaciones montan *skill marketplaces* internos (un repo con naming convention y `description` estandarizadas para evitar colisiones).

Versiona siempre con git. Las Skills son código en forma de texto.

---

## Buenas prácticas

- Una Skill = un propósito. Si duda, divide.
- `description` testable: lee la description y pregúntate "¿el modelo sabrá decidir cuándo cargarme?".
- Escribe tests: 3-5 consultas que DEBERÍAN disparar la skill y 3-5 que NO. Verifica.
- Mantén un `CHANGELOG.md` por skill.
- Actualiza la `description` cuando cambie el alcance.

---

## Anti-patrones

- ❌ Skill genérica: "Asistente general para mi empresa" → Claude no sabe cuándo cargarla.
- ❌ Skill gigante que hace 15 cosas → imposible mantener.
- ❌ Duplicar base de conocimiento dentro de la skill: la skill es instrucciones, no datos.
- ❌ Colisiones: dos Skills con `description` parecidas → Claude se confunde.

---

👉 Siguiente: [09 · Avanzado · MCP y sistemas agénticos](09-avanzado-mcp.md)
