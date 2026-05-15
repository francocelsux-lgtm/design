---
name: celsux-brand
description: >
  Crear piezas gráficas para Celsux 360 respetando el sistema de identidad visual.
  Activar SIEMPRE que se pida cualquier pieza, diseño, gráfico, flyer, post,
  portada, catálogo, slide, banner, o material visual de Celsux.
---

# Celsux 360 — Skill de Diseño Gráfico

## PASO 1 — Leer siempre primero

Antes de generar cualquier pieza, leer:
- `skills/celsux-brand/brand-identity.md`
- `assets/celsux-brand-prompt.md`

No ejecutar sin haber cargado ese contexto.

## PASO 2 — Clasificar la pieza

| Tipo           | Descripción                             | Formato            |
|----------------|-----------------------------------------|--------------------|
| `catalogo`     | Slide para catálogo de servicios        | A4 portrait        |
| `social_feed`  | Post feed Instagram/LinkedIn            | 1080×1080px        |
| `social_story` | Story o formato vertical                | 1080×1920px        |
| `portada`      | Portada de propuesta o presentación     | 1280×720px o A4    |
| `flyer`        | Flyer de impacto para evento            | A4 o 1080×1350px   |
| `slide`        | Slide de presentación comercial         | 1280×720px         |
| `banner`       | Banner digital                          | Según plataforma   |
| `one_pager`    | Ficha de servicio o producto            | A4 portrait        |

Si el usuario no especifica tipo, inferirlo del pedido.

## PASO 3 — Reglas de ejecución

### Paleta
- Negro `#0A0A0A` + Blanco `#F5F5F5` + Rojo `#E8001D`
- Máximo 3 colores por pieza
- El rojo es acento (15–25% del visual), nunca fondo total

### Tipografía (Design System v3 — CANÓNICO)
- **Display:** Anton — UPPERCASE, -0.01em, lh 0.88, NUNCA por debajo de 72px
- **Headline:** Oswald 700 — UPPERCASE, 0.02em tracking
- **Body:** Open Sans 300 — 15–17px, lh 1.65
- **Label:** DM Mono — 8–10px, 0.20em tracking, UPPERCASE

**RETIRADAS (nunca usar):** DM Sans, Barlow Condensed, Cormorant, Arial, Roboto

### Composición
- Alto contraste — sin grises suaves ni gradientes
- Un elemento rojo obligatorio por pieza (15–25% del visual)
- Eyebrow pattern: `──── LABEL` en DM Mono rojo antes de cada sección
- Ghost numbers: Anton stroke-only, opacity 0.04–0.06, como capa de fondo
- Cruces × como acento puntual de marca
- Logo `celsux.` + `www.celsux.com.ar` en toda pieza externa

### Fotografía
- Con foto: B&W + overlay rojo 40–55%
- Sin foto: composición tipográfica pura sobre negro o blanco

### Geometría
- Border-radius: 0 en bloques estructurales y fotos
- 12px en cards, 20px en paneles, 999px en botones

## PASO 4 — Output

Usar `skills/canvas-design/SKILL.md` para la ejecución visual.
Entregar como `.pdf` (multi-página) o `.png` (pieza individual).

La pieza tiene que parecer producida por una agencia premium.
No por una plantilla genérica.
