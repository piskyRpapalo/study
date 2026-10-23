# ROSETTA AS THE PRECEPTOR'S GUIDE · MEASUREMENT DETAIL (2026-10-23)

Detalle de mediciones del encargo de la Mesa "la Rosetta como guía del
preceptor en GitHub" (propose-only). El triaje T1–T12 vive en
ROSETTA_PRECEPTOR_GUIDE_20261023.md; este doc guarda el inventario (FASE 0)
y el cruce Rosetta fila a fila (FASE 1). Nada se firma aquí.

Medido 2026-10-23T13:55Z · sandbox Linux 6.18.35 · Python 3.12.15.
Base: origin/main fresco de los 8 repos (p0x en origin/master).

================================================================================
FASE 0 · INVENTARIO (medido, no inventado)
================================================================================

| Superficie | Fichero | Palabras | Bytes | Base medida |
|---|---|---:|---:|---|
| study | 13-rosetta.md | 2.077 | 13.097 | origin/main |
| study | 09-lore.md | 824 | 4.848 | origin/main |
| study | 05-contracts.md | 568 | 3.553 | origin/main |
| study | 01-governance.md | 432 | 2.678 | origin/main |
| study | 02-legislation.md | 735 | 4.567 | origin/main |
| APP | PRECEPTOR.md | 571 | 3.831 | origin/main |
| APP | CONTRIBUTING.md | 699 | 4.035 | origin/main |
| APP | AGENTS.md | 495 | 3.279 | origin/main |
| APP | CLAUDE.md | — | 515 | origin/main (pointer a AGENTS.md) |
| web | docs/lexicon.md | 2.418 | 13.995 | origin/main (§A–§L) |
| web | AGENTS.md | 654 | 3.990 | origin/main |
| web | CLAUDE.md | — | 6.080 | origin/main |
| lab | AGENTS.md | 623 | 4.388 | origin/main |
| lab | CLAUDE.md | — | 208 | origin/main (pointer) |
| p0x | AGENTS.md | 550 | 3.318 | origin/master |
| study | AGENTS.md | 447 | 2.802 | origin/main |

AGENTS.md ausentes (medido, NO_DATA con causa — no es defecto, es alcance):
buzon, piskyRpapalo (profile), aduana. Causa: repos de registro/infraestructura
sin contrato de agente; el contrato vive en study/AGENTS.md y los AGENTS.md
por repo que sí lo tienen.

================================================================================
FASE 1 · CRUCE ROSETTA (hallazgo por fila, con estado y ancla)
================================================================================

--------------------------------------------------------------------------------
1.1 · 09-lore.md vs lexicon §C1 — nombres FIRMADOS ausentes del lore
--------------------------------------------------------------------------------

Medido: grep de los 9 nombres de §C1 sobre 09-lore.md → 0 hits de los 9.
Los 9 viven en 13-rosetta.md (1–3 hits cada uno) pero NO en el lore canon.

El lore canon (09-lore.md) es el doc que un preceptor lee para entender el
mundo del juego. Si los nombres firmados no están ahí, el preceptor que abre
el lore no los encuentra. Son PROPUESTA de fila nueva en 09-lore.md, cada
una con su alias ES entre paréntesis (patrón del propio 09-lore.md).

| # | Nombre FIRMO | Alias ES | Dónde firmado | Estado en lore | Cambio propuesto | FIRMO |
|---|---|---|---|---|---|---|
| 1 | the Risen | zombi / zombis | p0x#52 | AUSENTE | fila en 09-lore.md: el mundo paralelo a Atlantis | sí (fila) |
| 2 | the rotor | superviviente | p0x#52 | AUSENTE | fila: el personaje jugable, paralelo al cangrejo | sí (fila) |
| 3 | the beacon | nodo / faro | p0x#52 | AUSENTE | fila: el punto de entrada que selecciona mundo y tutorial | sí (fila) |
| 4 | the Wastes | los Yermos | p0x#52 | AUSENTE | fila: hábitat paralelo al Reef | sí (fila) |
| 5 | the Flats | las Llanuras | p0x#52 | AUSENTE | fila: hábitat paralelo al Forest | sí (fila) |
| 6 | keepsake | recuerdo | p0x#54 | AUSENTE | fila: el objeto del tutorial fase 2 | sí (fila) |
| 7 | the Trunk | el tronco | p0x#54 | AUSENTE | fila: la web como objeto único; mundos = WORLDS, nunca branches | sí (fila) |
| 8 | the front door | la puerta principal / portada | web#272 · G3 | AUSENTE | fila: la portada directa dibujada con bubble_editor + bubble_paint | sí (fila) |
| 9 | WavesCraft | incubadora del bosque | G5a · web#274 | AUSENTE | fila: el taller local de ondas y vista de incubación | sí (fila) |

Cross-ref ONLY (Codex los acuña, no duplicar): the Crucible · crab-account ·
quaternary-verdict. Ya están en 13-rosetta.md o los acuña Codex en §C1; esta
propuesta no añade filas para ellos.

--------------------------------------------------------------------------------
1.1b · «the real-graphic style» — candidato con chequeo 10-collisions
--------------------------------------------------------------------------------

Estado medido: lexicon §C L66 lo lista como "working name", "Official name
pending (open decision 6)". El estilo está FIRMADO (adopción in situ,
2026-10-18) pero el nombre oficial no está acuñado.

Medido en código servido: `world_creator.js:191` ya usa el id
`'real-graphic-style'` y el título `'the real-graphic style'` — el nombre
trabajador está VIVO en servido.

Chequeo the Alphabet para el candidato:

| Criterio | Medición | Veredicto |
|---|---|---|
| exists | firmado 2026-10-18, adoptado in situ app+web; id vivo en world_creator.js:191 | ✓ |
| cheap | "the measured style" = 3 tokens planos; sin camelCase, sin números | ✓ |
| collision | "measured" aparece en 6 ficheros servido pero siempre en prosa/comentarios (MEDIDO, measured), nunca como identificador de estilo; "the measured style" 0 hits en lexicon; no colisiona con "the abyssal comic" (estilo distinto: abyssal = web servida, measured = app test) | ✓ |

Candidato propuesto para FIRMO: **the measured style** *(ES: el estilo medido)*.
Razón: "real" es vago (¿real cómo?) y "graphic" ya nombra a otra cosa (the
abyssal comic es el estilo gráfico servido). El estilo firmado es el de la app
test: medido, con recibos, sin promesas. "Measured" es la palabra que la casa
ya usa para todo lo honesto.

Fila propuesta para lexicon §C (reemplaza el working name cuando se firme):

| the measured style | el estilo gráfico real | The drawing style of the app test, signed off 2026-10-18; adopted in situ. Text moves to the left side (A11Y). | proposal → FIRMO pendiente |

Nota: el id `'real-graphic-style'` en world_creator.js:191 NO se renombra en
este PR — es un identificador interno, no el nombre servido al usuario. El
renombrado del id es lote aparte (iv.b del inventario de vocabulario).

--------------------------------------------------------------------------------
1.1c · Tabla rename-winner — RE-MEDIDA tras R-D3a (mar*→sea*)
--------------------------------------------------------------------------------

R-D3a (web#275, mergeado 13:35Z) renombró mar*→sea*. Se re-mide el conteo
ES↔EN en el corpus de study (09-lore.md + 13-rosetta.md) y en web servida
(public/, origin/main post-R-D3a):

| Pareja | study ES↔EN | web public/ ES↔EN (ficheros) | Veredicto |
|---|---|---|---|
| la Grieta ↔ the Rift | 3 ↔ 3 | — | estable |
| el Refugio ↔ the Refuge | 2 ↔ 2 | — | estable |
| la Estatua ↔ the Preceptor Statue | 2 ↔ 2 | — | estable |
| las Tormentas ↔ the Five Storms | 1 ↔ 2 | — | estable |
| la Caída ↔ the Descent | 2 ↔ 2 | — | estable |
| el tronco ↔ the Trunk | 0 ↔ 3 | — | EN gana (lore aún no tiene fila) |
| recuerdo ↔ keepsake | 1 ↔ 1 | — | estable |
| zombi ↔ the Risen | 1 ↔ 2 | 0 ↔ 1 | EN gana |
| superviviente ↔ the rotor | 1 ↔ 1 | 1 ↔ 0 | pendiente V3b (app#90 mergeado 13:09Z; web servido 0 hits tras V1) |
| los Yermos ↔ the Wastes | 0 ↔ 1 | — | EN gana (lore sin fila) |
| las Llanuras ↔ the Flats | 0 ↔ 1 | — | EN gana (lore sin fila) |
| mar ↔ sea | — | 7 ↔ 14 | R-D3a ejecutado: EN gana en ficheros; 7 ficheros ES restantes son referencias en docs/metadatos, no ficheros servidos |
| casa ↔ house | — | 42 ↔ 6 | R-D3b pendiente FIRMO (42 hits = clases CSS .casa-* + ficheros casa-*.js; el renombrado de FICHERO no toca las clases) |
| faro ↔ the beacon | — | 8 ↔ 0 | 8 hits = identificadores/comentarios, no display servido; V1 verificó 0 textos ES en display |
| cria ↔ brood | — | 1 ↔ 0 | R-D3c pendiente FIRMO (1 hit = referencia en atlas/, no servido) |

Anclas muertas tras renombrados: 09-lore.md tiene 2 anclas ruta:línea
(`aiact-art50-state-radio.js:4` → 220 Hz · `core.js:61` → 110 Hz). Verificadas
contra origin/main post-R-D3a: AMBAS VIVAS (ninguna tocaba mar*). 0 anclas
muertas medidas. Causa de no-haber-más: R-D3a no tocó ficheros anclados.

--------------------------------------------------------------------------------
1.2 · PRECEPTOR.md — no cita la Rosetta ni el lexicon
--------------------------------------------------------------------------------

Medido: PRECEPTOR.md (571 palabras, 3.831 B) menciona CONTRIBUTING.md y
SECURITY.md, pero NO menciona 13-rosetta.md (study) ni docs/lexicon.md (web).
Un preceptor que abre PRECEPTOR.md no sabe que debe leer la Rosetta antes de
nombrar.

PROPUESTA de addendum (≤ media página, cuerpo FIRMOado intacto — se APPENDE,
no se edita el cuerpo firmado):

> ## Reading order · PROPUESTA de addendum · REQUIERE_FIRMA
>
> Before naming anything, a preceptor reads the Rosetta
> (`study/13-rosetta.md`): it translates the Sovereign's language into the
> ecosystem's terms. Official names live in THE LEXICON
> (`preceptoros-web/docs/lexicon.md` §C1), coined once, reused everywhere.
> A signed name is used as-is; a working name is a proposal, never a fact.
> No preceptor has a work limit (p0x#54): build the whole plan by
> dependencies, one draft PR per subsystem. What is not measured is NO_DATA
> with its cause — never invented, never padded.

Tamaño estimado del addendum: ~700 B (cabe holgado en el doc). FIRMO aparte
requerido (es texto nuevo en un contrato firmado).

--------------------------------------------------------------------------------
1.3 · 05-contracts.md — quaternary-verdict (cross-ref, no fila nueva)
--------------------------------------------------------------------------------

Medido: `clasificador_cuaternario.py` existe en APP root (1.403 B), parsea
SI/NO/CUANDO/NO_DATA del mini-modelo. Referenciado por `test_ficha_cartucho.py`
(2 hits). 0 hits en 05-contracts.md.

Veredicto: cross-ref ONLY. El término "quaternary-verdict": si Codex ya lo
acuñó en lexicon §C1, no se duplica aquí. Si no está acuñado, fila PROPUESTA:

| quaternary-verdict | el veredicto cuaternario | The closed parser's four labels: SI / NO / CUANDO / NO_DATA-with-cause. Pure function, < 1,024 B envelope, rejects without repairing. | measured (APP clasificador_cuaternario.py) |

--------------------------------------------------------------------------------
1.4 · AGENTS.md por repo — reconciliación de techos (uno por ámbito, una vez)
--------------------------------------------------------------------------------

Regla FIRMO 23-oct (D-B + E1): «un techo por ámbito, escrito una vez».
Ámbitos medidos en 02-legislation.md §Amendment 2026-10-22:

| Ámbito | Techo | Dónde se escribe (una vez) |
|---|---|---|
| pieza fuente | 16.384 B (regla de eficiencia, modificable por la Mesa) | 02-legislation.md |
| bloque desplegado | 25 MiB (límite técnico) | 02-legislation.md |
| canal/evento | 1.024 B | 02-legislation.md |

Medido por repo (grep de cifras en AGENTS.md / CLAUDE.md):

| Repo | AGENTS.md dice el suyo | ¿Solo una vez? | Hallazgo |
|---|---|---|---|
| web | SÍ: "Máximo 25 MiB por bloque (revocado el tope de 16 KiB el 2026-10-11, firma D2…)" | ⚠ PARCIAL | Dice 25 MiB pero la frase "revocado el tope de 16 KiB" contradice E1 (D-B FIRMO 2026-10-22: 16 KiB es regla de eficiencia, no revocada). Es fila E1/D1 de ARREGLOS RÁPIDOS v2 — incoherencia abierta, ya registrada. web CLAUDE.md (6.080 B) sí lo dice bien: "regla de eficiencia, modificable por la Mesa". |
| web | canal 1.024 B | ✓ | En el comentario de profundidad (Depth 4): "< 1,024 B payload" |
| APP | NO cita cifras | ✓ | No repite: apunta a study. Correcto (una vez, en legislation). |
| lab | NO cita cifras de pieza/canal | ✓ | Cita "byte ceilings" del selector como regla de código (ámbito distinto, no contradice). Correcto. |
| study | NO cita cifras | ✓ | "Read the scoped technical ceilings in 02-legislation.md; do not restate their numeric values here." — EXACTAMENTE la regla. Modelo a seguir. |
| p0x | NO cita cifras | ✓ | AGENTS.md (550 palabras) sin cifras de techo. Correcto. |

Contradicción detectada: web AGENTS.md L33 ("revocado el tope de 16 KiB")
vs web CLAUDE.md L12 + 02-legislation.md (regla de eficiencia, no revocación).
Es la incoherencia E1/D1 ya registrada en ARREGLOS RÁPIDOS v2. No se parchea
directo: es fila de triaje con FIRMO (cambiar texto en AGENTS.md firmado).

--------------------------------------------------------------------------------
1.4b · E2 — web AGENTS.md «Con Codex solo por GitHub» (incoherencia abierta)
--------------------------------------------------------------------------------

Medido: web AGENTS.md L43: "Con Codex solo por GitHub: PRs PROPUESTA en ramas
mistral/*… jamás tocar codex/* ni claude/*".

D-A (ARREGLOS RÁPIDOS v2, FIRMO del Soberano 2026-10-23): Codex es
preceptor-externo-constructor, construye en la CLI del rack, propone por PR
en su rama. La línea de web AGENTS.md contradice D-A.

Es la incoherencia E2 ya registrada. Fila de triaje, no parche directo.
Texto propuesto (E2): "preceptor-externo-constructor: construye en la CLI del
rack según su PRECEPTOR.md de dispositivo; propone por PR en su rama".

--------------------------------------------------------------------------------
1.5 · Ban list §E en lore y contratos — solo negaciones/guardianes
--------------------------------------------------------------------------------

Medido (grep de la lista §E sobre 09-lore.md, 05-contracts.md, 13-rosetta.md):

| Fichero | Hits | Tipo | Veredicto |
|---|---|---|---|
| 09-lore.md | 2 ("tokenizes", "prohibited names") | negación/metáfora | ✓ correcto |
| 05-contracts.md | 0 | — | ✓ limpio |
| 13-rosetta.md | 2 ("tokenizes cheap" ×2) | the Alphabet (regla, no nombre) | ✓ correcto |
| web lexicon §E | lista completa | declaración de la ley | ✓ es la fuente |

Veredicto: la ban list está cumplida en lore y contratos. Los hits son
negaciones o la propia declaración de the Alphabet. Nada que limpiar.

================================================================================
RECIBO DE MEDICIONES
================================================================================

Comandos ejecutados en esta sesión (2026-10-23T13:55Z, sandbox Linux 6.18.35,
Python 3.12.15): wc -wc sobre ficheros en origin/main|master de los 8 repos;
grep de nombres §C1 sobre 09-lore.md y 13-rosetta.md; git grep sobre origin/main
de web post-R-D3a; git cat-file -e para verificar anclas; git show para
tamaños de AGENTS.md/CLAUDE.md por repo. Cada cifra sale de esos comandos.
Nada inferido: lo no medido está marcado NO_DATA con causa.

Ambos docs < 16.384 B (techo de pieza, regla de eficiencia) · 0 palabras
vetadas usadas como nombre (las citas son la propia lista §E) · español
(Mesa, doc interno de triaje).

Agent: preceptor-orquestador-github · Model: Vibe · Run: NO_DATA
