# DISAGREEMENTS — the empirical collision log (RV3-*)

**What this is:** the disagreements-log (ES: el registro de colisiones): the append-only record of every collision between a plan and a measurement — where the silicon said one thing and the metal answered another. One immutable ID per entry, anchored to its round or commission, each entry carrying its receipt: numbers, dates, shapes — never keys, never private names. (ES: registro empirico de colisiones y divergencias, append-only, anclado a ruling/ronda.)

**Piece 01 of the ideas18oct master specification. State:** PROPOSED — propose-only: the silicon writes, the Sovereign signs. Nothing here is canon until the sign-off.

## The law (how an entry lives)

- **Append-only.** An entry is never rewritten or deleted; a verdict changes only by a newer entry that cites the old ID. (ES: una entrada nunca se reescribe; el veredicto solo cambia con una entrada nueva que cita el ID viejo.)
- **Immutable IDs.** RV3-NN is never reused, never renumbered.
- **The machine wins.** A plan loses to a measurement, always, whoever wrote the plan (04-measurement.md). A test that lies is worth less than no test.
- **Form only.** Receipts carry numbers, dates and shapes; zero keys, zero private names.
- **NO_DATA is declared, never invented.** An unresolved collision stays OPEN with its cause.

## The log

| ID | Date | Anchor | The claim (the plan said) | The measurement (the metal said) | Verdict |
|---|---|---|---|---|---|
| RV3-01 | 2026-10-05 | container session, corpus search | "the phrase is not on disk" (one case-sensitive search) | the phrase was on disk; the search missed it by case | RESOLVED — measure twice, with two orthogonal methods, before declaring absence |
| RV3-02 | 2026-10-05 | container session, device census | phones paired by assumption | pairing measured on the USB bus | RESOLVED — assumption demoted to NO_DATA; the bus is the source |
| RV3-03 | 2026-10-01 | October sweep | one app tree, one gate count | two trees, two counts: 812 vs 830 under the same remote name | OPEN — NO_DATA on the authoritative tree until a fresh gate count follows the 2026-10-18 census |
| RV3-04 | 2026-10-07 | external figure vs lab record | 30.65 tok/s (external claim) | 25.7 generated tok/s measured on the rack's main node (Vulkan) | RESOLVED — mixed series; the external figure never enters the lab record |
| RV3-05 | 2026-10-09 | commission E1 | "the node refuses connections" (probe: wrong route, 5 s timeout) | /api/salud answered: version 0.2.0, 10 sensors; the service is a user unit, not a system unit | RESOLVED — false rejection; the probe lied, the node was alive; lesson: a lying test is worth less than no test |
| RV3-06 | 2026-10-09 | commission E2 | 37 local models (snapshot count) | 36 names from the live API; one model carried under two tags | RESOLVED — the snapshot counted a tag twice; the live API count wins |
| RV3-07 | 2026-10-18 | ideas18oct master spec | "30 waves in inventory" | no such constant in any repo; the measured ceiling is 10 active waves (tropas_max: 10) | OPEN — 10 measured, 30 NO_DATA until re-measured or amended by the Sovereign |
| RV3-08 | 2026-10-18 | ideas18oct master spec | "NPCs attack from the fog of war" | the fog is expired maintenance (npc_occupancy); no attacking NPC exists; the push mechanism is TO BUILD | OPEN — design intent, not a measured behavior |
| RV3-09 | 2026-10-01 | October sweep | one spelling of the Eye's directory | two spellings found in the tree | OPEN — NO_DATA on the authoritative spelling until re-measured |

**Reading note:** numbers and shapes in these receipts are true at their measurement date; the log never silently updates them — a new entry cites the old one. (ES: el registro no se actualiza en silencio; una entrada nueva cita a la vieja.)

## Pending the Sovereign's vocabulary seal (ideas18oct)

The master specification also carried coinages that are NOT defined here — a term is coined once, in THE LEXICON, under sign-off; this log only anchors that they are pending:

- **Explicit Role Handshake** (ES: protocolo de asuncion de rol explicito) — the consented-role contract: declare what is known, what is NO_DATA, and the limits of operation.
- **Sensor-Grounded HITL** (ES: verificacion asimetrica por sensor) — the human signs the sensor output, never the pretty plan.
- **Multimodal Semiotic Bridge** (ES: acople sensorial isomorfico) — one state, four channels: geometry, note, pulse, mirror.
- **group-slot** (ES: ranura de grupo) — the intermediate summary packet (<= 1,024 B) between node and world; name checked against collision ("Multics" avoided by law).
- **S1 · S2 · S3** — the active study objectives: second-order cybernetics, epistemic alignment, symbol grounding.
- **B1–B6** — the resolved-bottlenecks record: context collapse, multi-writer, offline defense, benchmark gaming, vocabulary barrier, plan-vs-metal hallucination.

State: coined in the master specification; FIRMO of vocabulary pending the Sovereign's seal at THE LEXICON. Zero duplication by law. (ES: FIRMO de vocabulario pendiente; el termino se acuna una sola vez.)
