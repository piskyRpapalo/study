# HITL · PROPUESTA · the Rosetta as the preceptor's guide in GitHub (2026-10-23)

Encargo de la Mesa (bloque, propose-only): todo lo que la Rosetta permite debe
guiar al preceptor que abre cualquier repo del ecosistema. Se mide, se cruza
y se propone. Nada se firma aquí; cada fila nombra el FIRMO que necesita.

Método: inventario medido sobre origin/main fresco de los 8 repos
(2026-10-23T13:55Z). Lo medido lleva comando y fecha; lo no medido es NO_DATA
con causa. La Biblia manda sobre el lore; nada de la casa interna sale aquí.
Detalle de mediciones (FASE 0 inventario + FASE 1 cruce fila a fila) en
ROSETTA_PRECEPTOR_GUIDE_DETAIL_20261023.md.

================================================================================
TRIAJE T1–T12
================================================================================

| # | Superficie | Hallazgo | Estado | Cambio propuesto | FIRMO requerido |
|---|---|---|---|---|---|
| T1 | study 09-lore.md | 9 nombres §C1 ausentes del lore | PROPUESTA | 9 filas nuevas (detalle §1.1) | sí, por fila o por lote |
| T2 | web lexicon §C | "the real-graphic style" name pending | PROPUESTA | acuñar "the measured style" (detalle §1.1b) | sí, nombre oficial |
| T3 | study 09-lore.md | rename-winner re-medido tras R-D3a | LIVE (medido) | actualizar tabla con conteos nuevos (detalle §1.1c) | no (medición) |
| T4 | study 09-lore.md | 2 anclas ruta:línea | LIVE (verificadas) | ninguna (0 muertas) | no |
| T5 | APP PRECEPTOR.md | no cita Rosetta ni lexicon | PROPUESTA | addendum reading order (detalle §1.2) | sí, aparte |
| T6 | study 05-contracts.md | quaternary-verdict sin fila | PROPUESTA (si Codex no acuñó) | cross-ref o fila (detalle §1.3) | sí, si fila nueva |
| T7 | web AGENTS.md L33 | "revocado el tope de 16 KiB" contradice E1 | STALE (incoherencia abierta E1/D1) | alinear a "regla de eficiencia" | sí (texto firmado) |
| T8 | web AGENTS.md L43 | "Con Codex solo por GitHub" contradice D-A | STALE (incoherencia abierta E2) | sustituir por línea de rol | sí (texto firmado) |
| T9 | web AGENTS.md | techo 25 MiB dicho, canal 1.024 B dicho | LIVE | ninguno | no |
| T10 | APP/lab/p0x/study AGENTS.md | techos no restated | LIVE (correcto) | ninguno | no |
| T11 | study lore+contratos | ban list cumplida | LIVE | ninguno | no |
| T12 | buzon/profile/aduana | sin AGENTS.md | NO_DATA (causa: sin contrato de agente) | ninguno (no es defecto) | no |

Resumen del cruce (mediciones completas en el doc de detalle):

- 09-lore.md tiene 0 de los 9 nombres firmados de §C1 → T1 (9 filas
  PROPUESTA). the Crucible / crab-account / quaternary-verdict quedan como
  cross-ref (Codex los acuña, no se duplica).
- rename-winner re-medido tras R-D3a (mar*→sea*): EN gana en ficheros
  servidos; los 7 ficheros ES restantes son docs/metadatos. 2 anclas
  ruta:línea en el lore verificadas VIVAS (0 muertas).
- PRECEPTOR.md (571 palabras) no cita la Rosetta ni el lexicon → T5,
  addendum «Reading order» (~700 B, append-only, cuerpo FIRMOado intacto).
- AGENTS.md por repo: web es el único que cita cifras y lo hace con dos
  contradicciones abiertas (T7 = E1/D1, T8 = E2); study AGENTS.md es el
  modelo ("do not restate numeric values"); APP/lab/p0x correctos.
- Ban list §E: cumplida en lore y contratos (hits = negaciones/guardanes).

Contratos M0/M1/L4a/L4b/L5a/L5b: solo lectura hasta FIRMO. No se tocan en
este PR.

================================================================================
PARADAS RESPETADAS
================================================================================

- R-D3b..f (casa→house, cria→brood, mercado→market, onda_profunda→deep_wave,
  cable_*→cable_call/cable_chat): NO arrancados. Esperan FIRMO uno por uno.
- Ramas huérfanas (p0x bcaabb7 audit V2 · web fix-main-gates): no borradas.
  Decisión del Soberano.
- PARA_LA_MESA.md: no escrito (regla de la casa).
- Contratos M0/M1/L4a/L4b/L5a/L5b: solo lectura.
- Nada fusionado. Rama mesa/*, PR borrador.
- docs/lexicon.md §C1: no tocado (territorio del PR web#274 en curso, G5a).

================================================================================
SUGERENCIAS (1–3)
================================================================================

1. **FIRMO en lote único para T1+T5**: las 9 filas de lore y el addendum de
   PRECEPTOR.md son la misma decisión (la Rosetta guía al preceptor). Un solo
   FIRMO desbloquea ambas superficies.
2. **T7+T8 como un solo PR de alineación web AGENTS.md**: son la misma
   incoherencia (ARREGLOS RÁPIDOS v2 E1+E2), texto del mismo fichero. Un PR,
   un FIRMO, cierra dos filas.
3. **T2 (the measured style) antes que C3b**: el tutorial fase 2 (keepsake)
   usa estilos; si el nombre oficial del estilo se firma antes, C3b hereda un
   léxico ya cerrado y no necesita enmienda posterior.

================================================================================
RECIBO
================================================================================

Medido 2026-10-23T13:55Z · sandbox Linux 6.18.35 · Python 3.12.15.
Comandos: wc -wc sobre ficheros en origin/main|master de los 8 repos; grep
de nombres §C1 sobre 09-lore.md y 13-rosetta.md; git grep sobre origin/main
de web post-R-D3a; git cat-file -e para verificar anclas; git show para
tamaños de AGENTS.md/CLAUDE.md por repo. Cada cifra sale de esos comandos en
esta sesión. Nada inferido: lo no medido está marcado NO_DATA con causa.

Ambos docs < 16.384 B (techo de pieza, regla de eficiencia) · 0 palabras
vetadas usadas como nombre (las citas son la propia lista §E) · español
(Mesa, doc interno de triaje).

Agent: preceptor-orquestador-github · Model: Vibe · Run: NO_DATA
