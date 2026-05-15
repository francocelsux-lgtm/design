# Celsux 360 — Design System

## About Celsux 360

**Celsux 360** is a Buenos Aires-based full-service corporate events production agency with 25+ years of experience and 3,000+ events produced. Clients include DirecTV, McDonald's, Adidas, LATAM, GSK, Mercado Libre, and BBVA.

**Tagline:** "El número clave para tu evento" / "All-in-one agency"  
**Positioning:** Premium, experiential, reliable. Not generic institutional — an agency that produces real emotions.  
**Web:** www.celsux.com.ar | info@celsux.com.ar | Buenos Aires, Argentina

### Products / Surfaces
- **Social media** — Instagram feed (1080×1080), Stories (1080×1920), LinkedIn posts, LinkedIn banners (1584×396)
- **Commercial presentations** — Slide decks (1280×720), proposals, one-pagers
- **Print materials** — Flyers (A4), catalogs, credentials, event programs, signage
- **Merchandise** — Thematic catalogs, product sheets
- **Web interfaces** — Landing pages, dashboards, UI components

---

## Sources

- **Brand identity repo:** `github.com/francocelsux-lgtm/design` (branch: `claude/celsux-design-system-EGnO4`)
  - `skills/celsux-brand/brand-identity.md` — master visual identity document
  - `skills/celsux-brand/SKILL.md` — piece classification and execution rules
  - `skills/canvas-design/SKILL.md` — PDF/PNG output engine
  - `skills/frontend-design/SKILL.md` — HTML/web output engine
  - `Catálogo Celsux360.pdf` — service catalog (not imported; large binary)
- **Logos provided:** Three PNG variants (360, red wordmark, white wordmark)

---

## CONTENT FUNDAMENTALS

### Voice & Tone
- **Language:** Spanish (Argentina) for all internal/external materials
- **Register:** Professional but energetic — not cold corporate, not casual startup
- **Tense/person:** Direct, second-person ("tu evento", "tu empresa") — speaks to the client
- **Casing:** UPPERCASE for display/impact headlines; sentence case for body copy
- **Emoji:** Never. The brand communicates through typography and imagery.
- **Numbers as narrative:** 25 años, 3.000 eventos, 360° — numbers are identity
- **Punctuation style:** The period in `celsux.` is part of the logo; used intentionally in copy as a brand marker
- **Vibe:** Confident, decisive, premium. Short sentences. Impact over explanation.

### Copy Examples
- "El número clave para tu evento."
- "All-in-one agency."
- "3.000 eventos. 25 años. Una sola agencia."
- "Producimos experiencias corporativas que se recuerdan."

### What Celsux does NOT sound like
- Generic corporate: "Somos líderes en soluciones de eventos..."
- Startup casual: "¡Hacemos eventos increíbles! 🎉"
- Timid: "Podríamos ayudarte a organizar..."

---

## VISUAL FOUNDATIONS

### Colors
| Name | Hex | Role |
|------|-----|------|
| Rojo Celsux | `#E8001D` | Dominant accent — blocks, highlights, emphasis |
| Negro | `#0A0A0A` | Backgrounds, heavy text, total contrast |
| Blanco | `#F5F5F5` | Clean backgrounds, text on dark |
| Gris Medio | `#6B6B6B` | Secondary text, data, labels |
| Gris Claro | `#D0D0D0` | Lines, separators, subtle textures |

**Rules:** Max 3 colors per piece. Red is accent only — never full-page background. No green (previous brand color, retired).

### Typography
| Level | Fonts | Style |
|-------|-------|-------|
| DISPLAY | Bebas Neue, Oswald ExtraBold, Anton | Ultra-bold condensed, UPPERCASE, large scale |
| HEADLINE | Oswald Bold, similar condensed bold | Bold, tight tracking |
| BODY | DM Sans, Open Sans | Regular/Light, high legibility |
| LABEL | Mono or condensed regular | Small, data/tags/numbering |

- Typography IS a design element, not just text
- Extreme size contrast (120pt title with 14pt caption in same piece)
- Display titles can bleed, stack, break out of frame — intentionally
- Large numbers (years, event counts) are visual elements, not just data
- **Never:** Arial, Calibri, Roboto, Inter as primary font

### Backgrounds
- Solid black or solid white — alternating between sections/pages
- No full-page gradients; no complex textures or patterns
- Photos used as structural backgrounds with B&W + red overlay (40–60% opacity)

### Photography
- Always converted to B&W first
- Red semi-transparent overlay (40–60%) = brand look
- Photos are structure, not decoration — can be cut geometrically, overlapped with type
- Color photos must be anchored by an adjacent red or black block
- Photos never "float" without visual anchor

### Composition
- **Extreme contrast:** Large vs small, black vs white, photo vs type
- **Typographic architecture:** Big words structure space like blocks
- **Diagonal motif:** Inherited brand element — 1–2 diagonal lines per piece max
- **Visible numbering:** Section numbers always visible as technical reference
- **Angular geometry:** No excessive rounded corners — clean, sharp edges
- **The X element:** The X from the logo used as standalone graphic accent

### Recurring Graphic Elements
- Red color blocks cut geometrically (no rounded corners)
- Thin diagonal lines (brand motif, used with restraint)
- Thin rectangular frames (outline only)
- Small cross marks (×) as punctual accents
- The Celsux X as isolated graphic element

### Animation (web/digital)
- Animations have purpose — not decorative
- CSS-only preferred
- One well-orchestrated entrance animation > ten micro-interactions
- No bouncy/playful easing — precise, controlled motion

### Hover & Interaction States
- Opacity shifts or color inversions (white ↔ black)
- No soft glow or drop-shadow hover effects
- Press states: slight scale-down (0.97) or color shift to red

### Cards & Containers
- Sharp corners (border-radius: 0 or minimal, 2px max)
- Thin borders (1px) in gray or white, or no border with strong color contrast
- No soft box shadows — if shadow, it's hard/offset (editorial feel)

### Iconography
- No decorative icon set — brand relies on typography and geometry
- Thin-stroke icons acceptable for UI (e.g. Lucide/Feather style)
- Unicode × used as brand accent
- No emoji

### Spacing & Layout
- Generous negative space — breathing room is luxury
- Grid-breaking asymmetry is intentional
- Fixed elements: logo + web URL always present in external pieces

### Imagery Vibe
- B&W or heavily desaturated + red tint
- Corporate event photography: stages, audiences, speakers, celebrations
- Grain acceptable in editorial contexts
- No stock-photo "happy office people" aesthetic

---

## ICONOGRAPHY

Celsux 360 does not use a formal icon system. The brand communicates through:
- **Geometric shapes:** Red blocks, thin lines, angular frames
- **The X mark:** From the logo — used as a graphic accent element
- **Typography:** Oversized letters/numbers serve as visual icons
- **No icon font or SVG sprite set** found in the brand repo

For web UI, use **Lucide Icons** (CDN: `https://unpkg.com/lucide@latest`) — thin stroke, clean, minimal. This matches the brand's angular, precise aesthetic. Flag: this is a design system addition, not explicitly specified in brand docs.

Logo assets available in `assets/`:
- `assets/logo-celsux-360.png` — Full logo with 360 (black + green circle, for light backgrounds). Note: the green circle is part of this variant; the current brand uses red/black/white only.
- `assets/logo-celsux-red.png` — Wordmark `celsux.` in brand red, for light backgrounds
- `assets/logo-celsux-white.png` — Full wordmark `celsux.` in white with red X accent, for dark backgrounds

---

## FILE INDEX

```
/
├── README.md                    — This file. Master reference.
├── SKILL.md                     — Claude Code skill definition
├── colors_and_type.css          — CSS variables for all tokens
├── assets/
│   ├── logo-celsux-360.png      — Full logo (360 variant)
│   ├── logo-celsux-red.png      — Wordmark in red
│   └── logo-celsux-white.png    — Wordmark white + red X (dark bg)
├── preview/
│   ├── colors-primary.html      — Primary color palette card
│   ├── colors-neutral.html      — Neutral palette card
│   ├── colors-semantic.html     — Semantic color usage card
│   ├── type-display.html        — Display type specimen
│   ├── type-body.html           — Body/label type specimen
│   ├── type-scale.html          — Type scale overview
│   ├── spacing-tokens.html      — Spacing tokens
│   ├── logo-variants.html       — Logo variants card
│   ├── graphic-elements.html    — Brand graphic elements
│   └── composition-rules.html   — Composition system
└── ui_kits/
    └── web/
        ├── README.md            — Web UI kit notes
        ├── index.html           — Interactive web prototype
        ├── Components.jsx       — Core UI components
        └── Screens.jsx          — Screen compositions
```
