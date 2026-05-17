# Lessons — Celsux 360 Design Repo

Aprendizajes acumulados por sesión. Actualizar después de cada corrección.

<!-- Formato:
## [Fecha] — [Tema]
**Error:** qué salió mal
**Causa:** por qué pasó
**Regla:** qué hacer diferente
-->

## 2026-05-15 — Tipografía y logo en piezas de catálogo
**Error:** play-and-work.html generado con Barlow Condensed/Barlow y sin logo.
**Causa:** Sesión trabajó en un branch con CLAUDE.md diferente al canónico, sin acceso al design system ZIP actualizado.
**Regla (ACTUALIZADA v3):** Sistema tipográfico canónico = Anton (display, mín 72px) + Oswald 700 (headline) + Open Sans 300 (body) + DM Mono (labels). DM Sans está RETIRADA. NUNCA entregar pieza sin logo `assets/logo-celsux-white.png` (fondos oscuros) o `logo-celsux-red.png` (fondos claros).

## 2026-05-15 — DM Sans retirada del sistema de tipografía
**Error:** Regla anterior decía "usar DM Sans (body)" — esta fuente está RETIRADA en Design System v3.
**Causa:** ZIP Celsux_360_Design_System_3 establece explícitamente que DM Sans, Barlow Condensed y Cormorant Garamond están retiradas.
**Regla:** Body = Open Sans 300 siempre. Verificar ZIP design system ante cualquier duda tipográfica.

## 2026-05-17 — Decks ≠ piezas personalizadas
**Error:** Los agentes `deck-portada`, `deck-cierre` y `deck-diferenciadores` tenían inputs de cliente, fecha y urgencia, asumiendo que los decks son propuestas personalizadas.
**Causa:** El rol del repo fue mal interpretado: los decks son catálogos institucionales. Las piezas personalizadas son las "cartas de presentación", que son un tipo separado.
**Regla:** Los agentes de deck NO reciben `cliente`, `fecha_propuesta` ni `urgencia`. Ningún campo de portada incluye nombre de cliente ni fecha. La selección de clientes en el slide de casos de éxito es fija (variedad de rubros), nunca ordenada por sector del prospecto.

## 2026-05-15 — CLAUDE.md divergente por branch
**Error:** Cada branch acumuló su propia versión de CLAUDE.md con distintas instrucciones, generando outputs inconsistentes.
**Causa:** Claude Code crea sesiones aisladas por branch. Sin un branch canónico único, el "cerebro" se fragmenta.
**Regla:** El CLAUDE.md canónico vive en `claude/fix-pdf-branding-tJaJh` (o el branch principal). Antes de cualquier sesión de diseño, verificar que el branch tiene el CLAUDE.md correcto (>3.000 bytes, con skills table).
