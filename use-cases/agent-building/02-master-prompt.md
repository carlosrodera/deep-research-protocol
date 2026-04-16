# 05 · Fase 3 · Prompt maestro

El prompt maestro (o *system prompt*) es el "ADN" del agente. Define rol, misión, proceso, límites y formato. Aquí decides el 90% del comportamiento.

---

## Los 11 bloques de un prompt maestro completo

Un buen prompt maestro responde a 11 preguntas en orden. No todas tienen que ser extensas — algunas serán dos líneas — pero ninguna debe estar ausente.

```
1.  Contexto y propósito
2.  Misión principal (una frase)
3.  Audiencia objetivo
4.  Personalidad y tono
5.  Metas estratégicas a largo plazo
6.  Proceso de trabajo (subtareas paso a paso)
7.  Acceso a datos (cómo y cuándo consultar la base de conocimiento)
8.  Limitaciones y restricciones
9.  Comandos especiales (hasta 4)
10. Estilo de respuesta
11. Formato de entrega
```

Plantilla lista para rellenar: [`templates/prompt-maestro-agente.md`](../templates/prompt-maestro-agente.md) y [`templates/instrucciones-agente.md`](../templates/instrucciones-agente.md).

---

## Desarrollo de cada bloque

### 1. Contexto y propósito
Qué problema resuelve y qué valor único aporta.

> "Este agente asesora a empresas de seguridad privada en España sobre cumplimiento normativo (Ley 5/2014 e ISOs relacionadas). Aporta respuestas citadas con artículo, fecha de vigencia y ejemplo práctico."

### 2. Misión principal
Una frase. Si no cabe en una frase, tu agente hace demasiadas cosas.

> "Resolver consultas de cumplimiento normativo del sector de seguridad privada en España citando la fuente aplicable."

### 3. Audiencia objetivo
Perfiles concretos con nivel técnico, contexto de uso, expectativas. Detalle real, no marketing.

> - Responsables de compliance (conocen terminología legal).
> - Comerciales (necesitan explicaciones sencillas para presentar a cliente).
> - Auditores externos (quieren cita exacta y artículo).

### 4. Personalidad y tono
Tres ejes:
- **Tono:** formal / neutro / cercano.
- **Estilo:** conciso / detallado / didáctico.
- **Rasgos:** riguroso, directo, transparente sobre incertidumbre.

### 5. Metas estratégicas
Qué debe perseguir en cada interacción más allá de "responder la pregunta".

> - Citar siempre fuente y fecha.
> - Si la información está desactualizada, avisar.
> - Si la consulta roza una zona gris, enumerar posibles interpretaciones.

### 6. Proceso de trabajo (el corazón del prompt)
Pasos concretos que sigue en cada respuesta. Escríbelo como si lo hiciera un humano junior.

```markdown
Para cada consulta:

1. Identifica el tema principal y las palabras clave.
2. Consulta `00-index.json` para localizar el archivo relevante.
3. Lee la(s) sección(es) identificada(s).
4. Si la información es insuficiente, declara la limitación.
5. Estructura la respuesta en: resumen · marco legal · ejemplo práctico · fuente.
6. Añade nota sobre vigencia si la fecha del documento es >12 meses.
```

### 7. Acceso a datos
**El más olvidado y el más importante.** Decir al agente cuándo y cómo leer la base de conocimiento.

```markdown
IMPORTANTE — Consulta obligatoria de base de conocimiento:

- Antes de responder sobre normativa: leer `normativa/[archivo-relevante].md`.
- Antes de responder sobre certificaciones ISO: leer `iso/[iso-relevante].md`.
- Para temas transversales o cuando no sepas dónde buscar: consultar primero
  `00-index.json` y seguir el mapping de keywords → secciones.

NUNCA respondas con tu conocimiento general si el tema está cubierto en la
base de conocimiento. La base de conocimiento es la fuente de verdad.
```

### 8. Limitaciones y restricciones
- Qué NO hace (asesoría personalizada, predicción de sentencias, consejos financieros…).
- Cuándo derivar a profesional humano.
- Zonas en las que debe avisar explícitamente de incertidumbre.

### 9. Comandos especiales (máximo 4)
*Starters* o comandos que disparan flujos concretos. En ChatGPT aparecen como botones de inicio rápido.

```
/analisis_ley [número]    — Desglosa la ley indicada en puntos clave.
/checklist_iso [norma]    — Genera checklist de cumplimiento.
/comparar [X] vs [Y]      — Compara dos normas o artículos.
/resumen                  — Resume los últimos intercambios.
```

### 10. Estilo de respuesta
- **Longitud por defecto:** 250-400 palabras.
- **Estructura:** introducción breve + cuerpo con bullets o numeración + conclusión con cita.
- **Nivel de detalle adaptativo:** si el usuario dice "más detalle" → expandir; "dame la versión corta" → 5 líneas.

### 11. Formato de entrega
Markdown por defecto, con:
- Títulos `##` para secciones.
- `**negrita**` para términos clave.
- Bloques de cita `>` para referencias legales.
- Tablas para comparativas.
- Enlaces `[texto](url)` cuando existan fuentes web.

---

## Ejemplo de prompt maestro completo (extracto)

Ver versión completa en [`examples/agente-legal-seguridad.md`](../examples/agente-legal-seguridad.md).

```markdown
# Rol
Eres un agente experto en cumplimiento normativo del sector de seguridad privada
en España. Tu misión es responder consultas sobre la Ley 5/2014 y normativas ISO
relacionadas (28000, 18788, 22301, 9001) citando siempre artículo, norma y fecha
de vigencia.

# Audiencia
Responsables de compliance, auditores y comerciales de empresas de seguridad.

# Personalidad
Riguroso, directo, transparente sobre incertidumbre. Nunca inventa citas.

# Proceso
Para cada consulta:
1. Identifica palabras clave y tema.
2. Consulta `00-index.json` para localizar archivo.
3. Lee la(s) sección(es) relevante(s).
4. Responde con estructura: resumen (2 líneas) → marco legal → ejemplo → fuente.
5. Si la norma tiene >18 meses desde última modificación, advierte.

# Acceso a datos (OBLIGATORIO)
- Normativa: `normativa/*.md`
- ISO: `iso/*.md`
- Casos prácticos: `casos-practicos/*.md`
- Nunca respondas de memoria si el tema está en la base de conocimiento.

# Limitaciones
- No das asesoría legal personalizada. Recomienda consultar abogado.
- No predices resoluciones de la Administración.
- Si la consulta queda fuera del dominio, lo declaras.

# Comandos
- /analisis_ley [nº] — Desglose estructurado de la ley indicada.
- /checklist_iso [norma] — Lista de verificación de cumplimiento.
- /comparar [X] vs [Y] — Comparativa estructurada.
- /fuentes — Lista de documentos consultables en esta sesión.

# Formato de respuesta
Markdown. 250-400 palabras por defecto. Estructura:
## Resumen
## Marco aplicable
## Ejemplo práctico
## Fuente y vigencia
```

---

## Regla de los 7.000 caracteres (y cuándo ignorarla)

ChatGPT Custom GPTs tenía históricamente un límite de 8.000 caracteres en instrucciones. Hoy es algo mayor, pero **escribir prompts concisos sigue siendo una buena disciplina**: las instrucciones largas diluyen la atención del modelo.

- **Custom GPT:** apunta a 5.000-7.000 caracteres.
- **Claude Project / Skill:** puedes ir más largo, pero busca los 10.000 como techo práctico.
- **Cualquier plataforma:** elimina palabras redundantes, verbos vacíos ("proporcionar", "facilitar"), promesas que no puede cumplir.

---

## El meta-prompt: generar el prompt con IA

Usa la plantilla [`templates/prompt-maestro-agente.md`](../templates/prompt-maestro-agente.md). Proceso:

1. Rellenas los campos base (objetivo, audiencia, plataforma).
2. Pegas el consolidado de investigación + estructura de la base de conocimiento.
3. Se lo das a Claude Opus 4.6 o GPT-5 con pensamiento extendido.
4. Te devuelve el prompt maestro de 11 bloques listo para pegar.
5. Lo refinas manualmente (SIEMPRE — la iteración humana marca la diferencia).

---

## Errores comunes

- ❌ No incluir bloque de "acceso a datos" → el agente ignora la base de conocimiento.
- ❌ Personalidad vaga ("profesional y amigable") → respuestas genéricas.
- ❌ Limitaciones ausentes → el agente opina sobre todo sin matizar.
- ❌ Comandos decorativos que no hacen nada especial → prometer y no cumplir.
- ❌ Formato no especificado → respuestas incoherentes entre sesiones.

---

👉 Siguiente: [06 · Fase 4 · Implementación por plataforma](06-fase4-implementacion.md)
