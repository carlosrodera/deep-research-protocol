# Plantilla · Generador de índice vectorial JSON

Para bases de conocimiento grandes (>50 páginas), un índice vectorial permite que el agente localice la sección exacta sin leer el documento completo. Este prompt genera ese índice a partir de tu archivo fuente.

---

## Cuándo usarlo

- Documentos Markdown o PDF con >50 páginas.
- Leyes extensas, manuales técnicos, codex normativos.
- Corpus con decenas de miles de palabras.

Para documentos pequeños (<30 páginas) normalmente no hace falta: el modelo lee el archivo entero sin problema.

---

## Prompt

```text
Tengo un documento sobre [TEMA] que voy a usar como base de conocimiento
de un agente IA. El documento tiene [N páginas / N palabras] y está
estructurado en [capítulos / artículos / secciones].

Analízalo y genera un **índice vectorial** en formato JSON con la
estructura siguiente:

{
  "document": "nombre_archivo.md",
  "version": "YYYY-MM-DD",
  "summary": "1-2 frases describiendo el documento",
  "sections": [
    {
      "id": "S1",
      "title": "Título de la sección",
      "location": "Artículo/sección/página exacta",
      "summary": "1-2 frases resumiendo el contenido",
      "keywords": ["palabra1", "palabra2", "sinónimo1", "concepto_relacionado"]
    }
  ],
  "keyword_index": {
    "palabra_clave_1": ["S1", "S4"],
    "palabra_clave_2": ["S2"],
    "concepto_compuesto": ["S3", "S7"]
  },
  "usage_instructions": "Texto en lenguaje natural explicando al agente
   cómo usar este índice."
}

## Requisitos

1. Cubre el 100% del documento — no dejes secciones sin indexar.
2. En `keywords` incluye: términos literales del texto, sinónimos
   comunes, conceptos relacionados, y variantes (plural/singular,
   con/sin artículo).
3. `keyword_index` debe contener al menos 30 palabras clave distintas
   mapeadas a las secciones correspondientes.
4. Cada sección debe ser localizable de forma inequívoca con su `location`.
5. El campo `usage_instructions` explica al agente el procedimiento:
   identificar palabras clave de la consulta → buscar en `keyword_index`
   → leer las secciones referenciadas.

Devuelve SOLO el JSON, válido y bien formateado, en un bloque de código.

---

[ADJUNTA O PEGA EL DOCUMENTO AQUÍ]
```

---

## Qué hacer con el JSON resultante

1. Guárdalo como `00-index.json` en la raíz de tu base de conocimiento.
2. Súbelo al agente junto a los documentos.
3. En el prompt maestro del agente, en el bloque 7 (Acceso a datos), añade:

```markdown
## Consulta de la base de conocimiento

OBLIGATORIO. Para cualquier consulta sobre [DOMINIO]:

1. Identifica las palabras clave de la consulta del usuario.
2. Consulta `00-index.json` → `keyword_index`.
3. Para cada match, lee la sección referenciada en el archivo correspondiente.
4. Formula la respuesta citando archivo y sección.

Si ninguna keyword del índice coincide con la consulta, declara
explícitamente: "No encuentro información verificada sobre esto en mi
base de conocimiento."
```

---

## Variante para documento en PDF sin convertir

Si el archivo sigue en PDF:

```text
Adjunto un PDF de [N páginas]. Primero extrae su contenido sección a
sección (página por página si no hay encabezados claros) y luego genera
el índice JSON vectorial siguiendo el esquema indicado.

Si el contexto del modelo no permite procesar todo el PDF de una vez,
divídelo en bloques de 20 páginas y genera un JSON parcial por bloque;
luego fusiónalos en un único índice final consistente.
```

---

## Validación del índice

- [ ] El JSON es válido (usa [jsonlint.com](https://jsonlint.com) o `jq`).
- [ ] Cada `id` de `keyword_index` existe en `sections`.
- [ ] `keyword_index` tiene ≥30 entradas.
- [ ] No hay secciones sin ninguna keyword asociada.
- [ ] `location` permite localizar la sección sin ambigüedad.
- [ ] Pruebas: eliges 5 preguntas reales → el índice apunta a la sección correcta en ≥4/5.
