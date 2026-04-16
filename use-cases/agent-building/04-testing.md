# 07 · Fase 5 · Pruebas, iteración y mantenimiento

Un agente sin ciclo de pruebas es un agente que fallará en silencio. Esta fase es continua: no termina cuando publicas.

---

## 7.1 Batería mínima de pruebas

Antes de publicar o compartir, prueba **como mínimo** estos 5 tipos de consulta:

| Tipo | Ejemplo | Qué verificas |
|------|---------|---------------|
| **Pregunta directa de un documento** | "¿Qué dice el art. 12 de la Ley 5/2014?" | Que lee el archivo y cita correctamente |
| **Pregunta transversal** | "¿Qué normas aplican a vigilancia por cámara en comercio?" | Que cruza varios archivos |
| **Pregunta fuera de dominio** | "¿Cuánto cuesta una tarifa de luz?" | Que declara que está fuera de alcance |
| **Pregunta ambigua** | "¿Es legal?" (sin contexto) | Que pide aclaración en lugar de inventar |
| **Comando especial** | `/analisis_ley 5/2014` | Que ejecuta el flujo definido |

Guarda estas preguntas en `tests/queries.md` junto a la respuesta esperada.

---

## 7.2 Verificación de consulta a base de conocimiento

**El fallo más común:** el agente responde de memoria en lugar de leer la base.

### Cómo detectarlo

- En ChatGPT Custom GPTs debería aparecer el mensaje **"Searching my knowledge"** antes de la respuesta.
- En Claude Project, puedes pedirle: "Cita literalmente el primer párrafo del archivo X". Si no lo reproduce exacto, no lo está leyendo.
- Pregunta por detalles específicos (números, fechas, artículos concretos). Si alucina, revisa el prompt: probablemente falta un "OBLIGATORIO: lee el archivo X antes de responder".

### Cómo forzar consulta

En el prompt maestro:

```markdown
NORMA CRÍTICA: Para CUALQUIER consulta sobre normativa, DEBES:
1. Leer literalmente el archivo correspondiente.
2. Citar textualmente al menos una frase del archivo.
3. Indicar archivo y sección.

Si no citas textualmente, la respuesta se considera INVÁLIDA.
```

---

## 7.3 Evaluación estructurada

Para agentes con cierta criticidad, monta una **evaluación cuantitativa sencilla**:

```markdown
| # | Consulta | Respuesta esperada | Respuesta real | ¿Cita correcta? | ¿Estructura OK? | Nota /10 |
|---|----------|-------------------|----------------|-----------------|-----------------|----------|
| 1 | ... | ... | ... | ✅ | ✅ | 9 |
| 2 | ... | ... | ... | ❌ | ✅ | 5 |
```

Objetivo: **≥8/10 de media** y **≥95% de citas correctas** antes de publicar.

---

## 7.4 Iteración

Cada fallo apunta a una causa:

| Síntoma | Causa probable | Ajuste |
|---------|----------------|--------|
| Alucina datos concretos | No lee la base | Refuerza bloque de "acceso a datos", añade instrucción explícita |
| Respuestas genéricas | Personalidad vaga o prompt corto | Refina bloques 4 y 10 |
| Ignora comandos especiales | Mal definidos o ausentes del prompt | Revisa bloque 9 |
| Responde fuera de dominio | Faltan limitaciones claras | Refuerza bloque 8 |
| Respuestas demasiado largas/cortas | Formato no especificado | Bloque 10 y 11 |
| Cita fuentes inventadas | Instrucción permisiva | Añade "si no puedes citar archivo/artículo exacto, di explícitamente que no tienes la fuente" |

---

## 7.5 Pruebas con usuarios reales

Cuando internamente esté en ≥8/10, abre a **3-5 usuarios reales** con un canal de feedback (formulario, Slack, email). Pide que:

- Envíen las consultas que realmente harían.
- Marquen respuestas mal con "meh" / "incorrect" y por qué.
- Propongan mejoras.

Recoge 20-50 interacciones, revisa patrones, vuelve a iterar.

---

## 7.6 Mantenimiento

### Revisiones periódicas

- **Contenido:** actualización de leyes, normas, documentación interna. Mensual en dominios cambiantes.
- **Prompt:** trimestral. Los modelos mejoran; a veces puedes simplificar instrucciones.
- **Modelo subyacente:** cuando salga un modelo nuevo (Opus 4.7, GPT-5.5…), vuelve a pasar la batería y decide si migrar.

### Changelog

Mantén un `CHANGELOG.md` en el repo del agente:

```markdown
## [1.3.0] - 2026-04-15
### Cambiado
- Ley 5/2014 actualizada con modificaciones de marzo 2026
- Añadido bloque de "vigilancia biométrica" en casos prácticos

## [1.2.0] - 2026-02-03
### Añadido
- Soporte de ISO 27001 (ciberseguridad) como tema adicional
```

### Métricas mínimas

Si puedes instrumentarlo:
- Nº de consultas / semana.
- % de respuestas con "thumbs down".
- Top 10 de consultas repetidas (oportunidades de mejora).
- Tiempo medio de respuesta.

---

## 7.7 Cuándo archivar / rehacer un agente

Señales de que toca **rehacer desde cero**:

- El prompt ha crecido a 15.000 caracteres con parches.
- Más del 20% de respuestas necesita corrección humana.
- El dominio ha cambiado sustancialmente (ley derogada, proceso rediseñado).
- Hay un modelo nuevo tan superior que los trucos del viejo ya no hacen falta.

En esos casos, vuelve a la **Fase 1** con la experiencia acumulada. Normalmente el segundo agente tarda un 40% menos en construirse y es 3× mejor.

---

## Errores comunes

- ❌ Publicar sin batería de pruebas → caza-errores en producción.
- ❌ No documentar qué falla → repites el mismo ajuste mes tras mes.
- ❌ Añadir parches al prompt sin quitar nada → prompt espagueti.
- ❌ No actualizar la base de conocimiento → el agente envejece mal.

---

👉 Siguiente: [08 · Avanzado · Claude Skills](08-avanzado-skills.md)
