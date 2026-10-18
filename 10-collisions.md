# 10 — Collisions: duplicate names, rename as winner

**What this is:** the measured list of terms that lived twice — an old Spanish name and the official English name — and the verdict for each collision. Counts were measured by search over the project's own files (*.md*, rack + web docs) before any verdict was written. *(ES: los duplicados medidos del sistema y su veredicto — el nombre oficial gana, el viejo queda alias histórico.)*

## The law (rename-winner)

- When two names collide, **the official English name wins**; the old Spanish name becomes a **historical alias, absorbed** — append-only, never silently rewritten. *(ES: en colisión gana el renombrado; el viejo queda alias histórico absorbido.)*
- Dominance counts do **not** decide the winner — they only measure how much absorption work remains. *(ES: la dominancia solo mide el trabajo pendiente.)*
- Historical documents are declared as history, not rewritten. *(ES: los docs históricos se declaran, jamás se reescriben en silencio.)*

## Governance collisions (measured ES ↔ EN)

| Winner | Alias | Measured | What it is |
|---|---|---|---|
| seal | sello | 61 ↔ 242 | the Desk's closing stamp on a measured round; append-only; the silicon never seals for the Sovereign |
| sign-off | firma | 6 ↔ 1866 | the Sovereign's decision signature; the only authority that lands changes |
| ledger | registro | 503 ↔ 580 | append-only history of measured facts; it rules over opinion |
| receipt | recibo | 741 ↔ 90 | a worker's report of what was measured; form only, never a decision |
| commission | encargo | 1 ↔ 95 | a work order the Sovereign issues; workers propose, never decide |
| tray | bandeja | 58 ↔ 130 | the inbox surface; the sign-off tray holds what awaits the Sovereign's word |
| charter | cédula | 5 ↔ 26 | Ed25519 identity document with real expiry |
| customs | aduana | 8 ↔ 79 | the public charter verifier: verifies, writes only hashes, never signs |
| eye | ojo | 90 ↔ 524 | the rack dashboard: shows the measured, never invents; stale data declares itself |
| yardstick | vara | 12 ↔ 37 | the standard a claim must pass (e.g., the file ceiling) |

## States, doctrine, and the two ceilings

- **NO_DATA** (alias: *sin_dato*) — "could not be measured", always with cause and remedy; distinct from **RED** (measured and wrong).
- **gate** — the test batch that decides entry. Two runners exist; the **certified runner** runs everything, the partial one only part. Published counts come only from the certified runner.
- **Necropolis** (alias: *Necrópolis*) — the graveyard of the retired: every piece enters as **CANONIZE / GUARD / DISCARD** with a written reason.
- **Bronze · Silver · Gold** — the quarantine shelves: as-arrived · passed deterministic script validation · read and sealed by the Sovereign. No machine promotes to Gold.
- **Two living ceilings** — web: 10 KiB per served file; core: 16 KiB per file. Doctrine: **split, never trim comments.**

## The loops (the swarm), renamed

- **Guardian** (*guardián*) — nightly stdlib-only guard; a turn that sees zero files is a failed turn.
- **Curator** (*curador*) — weekly dedup and broken-link pass; read-only, proposes, never deletes.
- **Tuner** (*afinador*) — runs the whole suite and hunts the three ways to break green.
- **Director** — NO_DATA: should schedule windows and detect dead loops; not running.
- **S0** — NO_DATA: the watcher of the watchers ("if nothing passes the filter in 7 days, suspect the filter"); never ran.
- **heartbeat** (*latido*) — the shared loop library: every turn beats in and out; a crash leaves its failed beat.
- **oneshot** — run-and-exit service; **inactive between runs is the healthy state.**
- **timer** — the clock that wakes a loop; cadences differ — comparing a weekly with two dailies fabricates outages.
- **the swarm** (*el enjambre*) — five self-waking loops that watch and note; they propose and register, never fix. Also: Haiku batches of 2–3 in parallel, gates n=2.

## Retired by law (scrub list)

- oraculo, notaria — prohibited names that still live in historical documents as declared aliases. Never official, never rewritten in silence.

**Two native languages:** PreceptorOS speaks English for official names (the canon) and Spanish as the working gloss. The alias is history, not an error. *(ES: dos lenguas nativas — el inglés oficial del canon y el español de trabajo; el alias es historia, no error.)*
