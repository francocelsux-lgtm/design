# CELSUX 360 — Brand Identity System

Archivo maestro de identidad visual. Todo output gráfico debe respetar este documento.
Este archivo refleja el Design System v3 (ZIP: Celsux_360_Design_System_3).

---

## IDENTIDAD CENTRAL

**Nombre:** Celsux 360
**Tagline:** "El número clave para tu evento" / "All-in-one agency"
**Posicionamiento:** Productora integral de eventos corporativos. Premium, experiencial, confiable.
**Personalidad visual:** Energía corporativa de alto impacto. No institucional genérico —
sino agencia que produce emociones reales.

---

## PALETA DE COLORES

| Nombre        | Hex       | Uso                                                       |
|---------------|-----------|-----------------------------------------------------------|
| Rojo Celsux   | #E8001D   | Único acento. Bloques, highlights, énfasis tipográfico. Máx 20% de la pieza. |
| Rojo hover    | #B8001A   | Estado hover de botones y elementos interactivos          |
| Negro         | #0A0A0A   | Fondos, texto pesado, contraste total                     |
| Blanco        | #F5F5F5   | Fondos limpios, texto sobre oscuro                        |
| Gris medio    | #6B6B6B   | Texto secundario, datos, labels                           |

**Colores contextuales (NUNCA como base del sistema):**
- `#003F8A` — piezas de incentive travel únicamente
- `#1C2B3A` — galas de noche únicamente
- `#C4873A` — galas de premios únicamente

**Reglas:**
- Máximo 3 colores por pieza (generalmente: negro + blanco + rojo)
- El rojo nunca es fondo de página completa — es acento, bloque parcial, elemento gráfico
- Área roja: 15–25% del visual total
- **NUNCA usar verde** (color anterior de la marca, retirado)
- **NUNCA usar dorado como base**

---

## TIPOGRAFÍA

| Nivel    | Fuente           | Estilo                                              |
|----------|------------------|-----------------------------------------------------|
| DISPLAY  | **Anton**        | UPPERCASE, -0.01em tracking, lh 0.88, mínimo 72px  |
| HEADLINE | **Oswald 700**   | UPPERCASE, 0.02em tracking, lh 1.05                |
| BODY     | **Open Sans 300**| 15–17px, lh 1.65                                    |
| LABEL    | **DM Mono**      | 8–10px, 0.20em tracking, UPPERCASE                 |

**Google Fonts import:**
```
https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@400;600;700&family=Open+Sans:wght@300;400&family=DM+Mono:wght@400;500&display=swap
```

**Principios:**
- La tipografía ES un elemento de diseño, no solo texto
- Títulos display (Anton) pueden romperse, apilarse, sangrar fuera del frame
- Números grandes (años, cantidad de eventos) son elementos visuales en Anton
- Contraste extremo de tamaños intencional (ej: 120px título con 9px label)

**RETIRADAS (nunca usar):**
- ~~Barlow Condensed~~
- ~~DM Sans~~
- ~~Cormorant Garamond~~
- ~~Arial, Calibri, Roboto, Inter como fuentes principales~~

---

## SISTEMA DE COMPOSICIÓN

**Contraste extremo:** El layout vive en tensiones — grande vs pequeño, negro vs blanco.

**Tipografía arquitectónica:** Las palabras grandes en Anton estructuran el espacio como bloques.

**Numeración visible:** Números de sección siempre visibles, como referencia técnica.

**Diagonal como motivo:** Líneas diagonales heredadas del brand. Máximo 1–2 por pieza, ángulo 20–30°.

**Ghost numbers:** Números Anton stroke-only (transparent + stroke), opacity 0.04–0.06, como capa de fondo.

### Fondos
- Negro sólido o blanco sólido — alternando entre páginas/secciones
- Sin gradientes full-page; sin texturas complejas
- Fotos como fondo estructural con B&W + overlay rojo (40–55% opacidad)

### Overlays fotográficos
- Foto a B&W + overlay rojo semitransparente (40–55%) = look de marca
- Foto a color debe estar anclada por un bloque rojo o negro adyacente
- No usar fotos "flotando" sin ancla visual
- Preferidas: audiencias, acción, multitudes, oradores. Nunca stock "oficina feliz".

### Elementos gráficos recurrentes
- Bloques de color rojo cortados geométricamente (border-radius: 0)
- Líneas finas diagonales (motivo heredado, máx 1–2 por pieza)
- Marcos rectangulares delgados (solo outline)
- Cruces pequeñas (×) como acento puntual — firma de marca
- El X del logo como elemento gráfico aislado
- **Patrón eyebrow:** `──── LABEL TEXT` en DM Mono rojo, siempre antes de títulos de sección

### Border radius
- `0` — fotos, bloques rojos, elementos estructurales
- `12px` — cards
- `20px` — paneles grandes
- `999px` — todos los botones (pill)

### Geometría
- Sin esquinas redondeadas excesivas (>20px en contenedores de contenido)
- Aristas limpias y precisas

---

## LOGO

**Variantes:**
- `assets/logo-celsux-white.png` — Wordmark blanco + X rojo. Para fondos oscuros.
- `assets/logo-celsux-red.png` — Wordmark rojo. Para fondos claros.
- `assets/logo-celsux-360.png` — Logo completo 360. (Nota: la variante 360 tiene círculo verde del brand anterior; usar con criterio)

**Reglas:**
- Siempre en blanco sobre fondos oscuros, rojo sobre fondos claros
- Nunca sobre fondos rojos
- Siempre acompañado de `www.celsux.com.ar` en piezas externas

---

## VOZ VISUAL POR TIPO DE PIEZA

### Catálogo de servicios
- Fondo: negro o blanco (alternando entre páginas)
- Foto del servicio + overlay + tipo display
- Nombre del servicio en rojo o blanco bold
- Descripción en body pequeño

### Redes sociales (feed)
- Formato cuadrado o 9:16
- Una sola idea por pieza
- Tipografía grande, menos texto
- Logo + web en esquina siempre

### Presentaciones comerciales
- Más blanco, más espacio — contexto formal
- Grid consistente por slide
- Datos y números destacados visualmente en Anton
- Fotos en paneles modulares

### Materiales de impacto (flyers, portadas)
- La foto puede ocupar 80% del espacio
- Tipografía en Anton que "rompe" la foto
- Un elemento rojo obligatorio
- Mínimo texto, máximo impacto

---

## REFERENTES VISUALES

El lenguaje visual de Celsux se inspira en:
- Diseño editorial deportivo de alta producción (NCAA, NFL graphics)
- Tipografía Suiza/Bauhaus modernizada con energía contemporánea
- Piezas de agencias de eventos europeas: blanco/negro/rojo, composición estructurada

**Lo que NO es Celsux:**
- Paletas pasteles o gradientes suaves
- Diseño "startup tech" (violetas, blues, esquinas redondeadas)
- Fondos con muchas texturas o patrones complejos
- Tipografías decorativas para textos de servicio
- Startup casual: "¡Hacemos eventos increíbles! 🎉"
- Corporativo genérico: "Somos líderes en soluciones de eventos..."

---

## VOZ Y TONO

- **Idioma:** Español (Argentina) para todos los materiales
- **Registro:** Profesional pero enérgico — no frío corporativo, no casual startup
- **Persona:** Segunda persona directa ("tu evento", "tu empresa")
- **Casing:** MAYÚSCULAS para display/impact headlines; sentence case para body
- **Emoji:** Nunca
- **Números como narrativa:** 25 años, 3.000 eventos, 360° — los números son identidad
- **Vibe:** Seguro, decisivo, premium. Oraciones cortas. Impacto sobre explicación.

**Ejemplos de copy:**
- "El número clave para tu evento."
- "3.000 eventos. 25 años. Una sola agencia."
- "Producimos experiencias corporativas que se recuerdan."

---

## DATOS DE CONTACTO (incluir en piezas externas)

www.celsux.com.ar
info@celsux.com.ar
Celsux 360 — All-in-one agency
Buenos Aires, Argentina

**Clientes de referencia:** DirecTV, McDonald's, Adidas, LATAM, GSK, Mercado Libre, BBVA
