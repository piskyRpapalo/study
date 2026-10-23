# ROSETTA · ENMIENDA DE TECHOS · 2026-10-23

PROPUESTA · propose-only · REQUIERE_FIRMO · nada se fusiona sin FIRMO.
Ejecuta la ley anticipada por la auditoría del 21-oct: **un techo por ámbito, escrito una vez.** Todo lo citado se leyó hoy del metal vivo (2026-10-23).

## Ley consolidada · un techo por ámbito

| ámbito | techo | naturaleza | texto vivo leído 2026-10-23 |
|---|---|---|---|
| pieza (archivo fuente) | < 16.384 B raw | regla de eficiencia, modificable por la Mesa (D-B, FIRMO 2026-10-22); NO revocada | web/CLAUDE.md L12 · origen escrito 28-Sep: "strictly under 16,384 bytes raw" (harvest 5, B.3) |
| bloque (despliegue) | máximo 25 MiB por bloque | límite técnico de despliegue | web/CLAUDE.md L12 |
| puerta del juego (gzip) | < 153.600 B (=150 KB) | ley con daño: pasada la puerta, la grieta hace el doble de daño | web/CLAUDE.md L12 (gzip_juego_b) |
| canal / recibo del buzon | < 1.024 B UTF-8 | ley de canal | 9 recibos sellados 2026-10-23, todos <1.024 B |
| llms.txt estudio | BUDGET 11.420 | vara ×2 verde contra origin/main e5f4947 (11.420 <= 11.420) | yardstick verify_llms_tree |
| llms.txt app | 1.024 B | presupuesto de la app | auditoría 21-oct |

Regla de lectura: "16 KiB" (v1.3) y "16.384 bytes" (ley 28-Sep) son la misma regla en dos ortografías. No son dos leyes.

## STALE a sanar (fila T7 · E1/D1)

- web/AGENTS.md L33: "revocado el tope de 16 KiB" — STALE. Contradice la ley viva: el techo de pieza NO está revocado; es regla de eficiencia modificable (D-B, FIRMO 2026-10-22; web/CLAUDE.md L12 lo dice bien).
- Propuesta: sustituir esa línea por la fila "pieza" de la tabla, y que cada techo viva escrito una sola vez en su texto dueño.

## Trazabilidad de la evidencia

- 28-Sep · origen escrito del techo de pieza: strictly under 16.384 B raw (harvest 5, B.3).
- 2026-10-11 (firma D2) y 2026-10-20 (lab G4): dos ortografías del mismo número; sin cambio de ley.
- 2026-10-22 · D-B FIRMO: 16 KiB = regla de eficiencia, no revocada.
- 2026-10-23 · lectura del metal vivo + esta enmienda (propuesta).

## Metal medido hoy (2026-10-23 · conteo y arquitectura, sin marcas)

- La ley gzip de 150 KB vive en los textos de ley; NO en el código del juego: 0 coincidencias de gzip o kb en las 133 piezas de public/game (131 js + 2 css).
- La pieza mayor del juego: 16.295 B — 89 B bajo el techo de pieza.
- Topes de juego viven en valores.js: army_tope 60 (L46) · escuadrón tope 32 (L32) · esquiva tope 300 (L50).

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
