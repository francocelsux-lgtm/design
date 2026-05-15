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
**Regla:** SIEMPRE usar Oswald (display/headline) + DM Sans (body). NUNCA entregar pieza sin logo `assets/logo-celsux-white.png` o `logo-celsux-red.png` según el fondo.

## 2026-05-15 — CLAUDE.md divergente por branch
**Error:** Cada branch acumuló su propia versión de CLAUDE.md con distintas instrucciones, generando outputs inconsistentes.
**Causa:** Claude Code crea sesiones aisladas por branch. Sin un branch canónico único, el "cerebro" se fragmenta.
**Regla:** El CLAUDE.md canónico vive en `claude/fix-pdf-branding-tJaJh` (o el branch principal). Antes de cualquier sesión de diseño, verificar que el branch tiene el CLAUDE.md correcto (>3.000 bytes, con skills table).
