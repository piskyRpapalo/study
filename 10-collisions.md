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

- **NO_DATA** (alias: *sin_dato*) — "could not be measured", always with cause and remedy; distinct from **RED** (measured and wrong). Measured: 2,337 ↔ 6 — the most absorbed term in the project.
- **gate** — the test batch that decides entry. Two runners exist; the **certified runner** runs everything, the partial one only part. It runs alone, in a hook. Published counts come only from the certified runner.
- **Necropolis** (alias: *Necrópolis*) — the graveyard of the retired: every piece enters as **CANONIZE / GUARD / DISCARD** with a written reason. It has two faces: the code graves and the physical box where dead hardware goes. Measured: 132 ↔ 73.
- **Bronze · Silver · Gold** — the quarantine shelves: as-arrived · passed deterministic script validation · read and sealed by the Sovereign. No machine promotes to Gold.
- **Two living ceilings** — web: 10 KiB per served file; core: 16 KiB per file. Doctrine: **split, never trim comments.** Measured: ceiling 288 ↔ techo 156.

## The loops (the swarm), renamed

- **Guardian** (*guardián*) — 229 ↔ 172 — nightly stdlib-only guard; a turn that sees zero files is a failed turn.
- **Curator** (*curador*) — 24 ↔ 110 — weekly dedup and broken-link pass; read-only, proposes, never deletes.
- **Tuner** (*afinador*) — 6 ↔ 108 — runs the whole suite and hunts the three ways to break green.
- **Director** — NO_DATA: should schedule windows and detect dead loops; not running.
- **S0** — NO_DATA: the watcher of the watchers ("if nothing passes the filter in 7 days, suspect the filter"); never ran.
- **heartbeat** (*latido*) — 770 ↔ 101 — the shared loop library: every turn beats in and out; a crash leaves its failed beat.
- **oneshot** — run-and-exit service; **inactive between runs is the healthy state.**
- **timer** — the clock that wakes a loop; cadences differ — comparing a weekly with two dailies fabricates outages.
- **the swarm** (*el enjambre*) — 159 ↔ 62 — five self-waking loops that watch and note; they propose and register, never fix. Also: Haiku batches of 2–3 in parallel, gates n=2.
- *Count caveat:* third-party noise (vendored code, chat histories) lives inside the project tree and inflates some counts; no verdict ever depends on dominance.

## Second wave — identity, lore, named ambiguities (measured)

| Winner | Alias | Measured | What it is |
|---|---|---|---|
| signature | firma (crypto) | heavy in the public identity docs | the Ed25519 64-byte proof of a key — NOT a sign-off: signature = crypto, sign-off = the Sovereign's decision. A trimmed signature is an ornament with a guarantee's name. |
| the Rift | la Grieta | 12 ↔ 31 | the world's break (canon); the personal crack is a different term — never confuse |
| the Refuge | el Refugio | 1 ↔ 25 | where the world survived the break |
| the Preceptor Statue | la Estatua | 12 ↔ 46 | the statue that watches |
| the Five Storms | las Tormentas | 26 ↔ 2 | the canonical storms; the Spanish singular barely exists |
| the Descent | la Caída | 22 ↔ 63 | the abyssal work of seven sections (OPEN, CLIFF, START, TREMOR, SPLIT, FALL, GATE), drawn in the bubble language |
| tomb | tumba | 0 ↔ 57 | the Necropolis burial unit: every tomb carries its written cause; nothing is deleted, it is buried |
| false green | falso verde | two reds measured | a green sensor can fabricate health: an OK row with nothing listening behind it |
| dormant ≠ absent | DORMIDO, no ausente | measured (dead_path) | a dormant register is not an absent one: it is declared, never assumed |
| blind judge vs context judge | juez_ciego · juez_de_contexto | two judges measured | the blind judge calibrates contracts; the context judge watches the session at compaction — never interchangeable |
| the loops vs the batch swarm | dos enjambres | real polysemy | the five rack loops (propose and register) vs the MODE PLAN Haiku batches (execute the plan): different owners, different law |

## Retired by law (scrub list)

- oraculo, notaria — prohibited names that still live in historical documents as declared aliases. Never official, never rewritten in silence.

## Coined, not yet built

- TWO-CLICK, contact sheet, MODE PLAN, the Harvest, stopping point — zero hits in the rack files: coined by the Desk in the ledger, not yet built in the project's own files. Declared, not absent.

**Two native languages:** PreceptorOS speaks English for official names (the canon) and Spanish as the working gloss. The alias is history, not an error. *(ES: dos lenguas nativas — el inglés oficial del canon y el español de trabajo; el alias es historia, no error.)*


## Third wave — external collisions with the live outside world (measured 2026-10-18)

**What this is:** the project's own terms checked against today's live products and collectively accepted vocabulary, web-measured on 2026-10-18. Governed by the **external-collision law** (02-legislation.md): a collision with a live product in the project's own category renames; a collision with a generic word is absorbed by definition. Every verdict was signed off by the Sovereign the same day.

| Term | Collides with (measured) | Verdict |
|---|---|---|
| atlas | ChatGPT Atlas — OpenAI's browser | KEPT — GREY AREA: the atlas here is the game-world engine, never the browser |
| Codex · Claude Code · Mistral web | the external tools themselves | Not coinages — external preceptors, parts of the system; to be named as agents or functions, pending real lab verification and presentation in the app (MVP) |
| astra | Project Astra — Google DeepMind's universal assistant | Absorbed into the preceptors ruling above |
| the swarm | Swarm — OpenAI's multi-agent framework (evolved into the Agents SDK) | KEPT — GREY AREA: the five rack loops, never the framework |
| ledger | Ledger — crypto hardware-wallet brand | KEPT — GREY AREA: the accounting word first; never the wallet |
| the Register | The Register — tech news site | KEPT — qualified in public docs as "the rack's record" |
| preceptor | clinical-education term; "The AI Preceptor" product | KEPT — PreceptorOS stays the brand; the bare word is a GREY AREA in education contexts |
| Hexelion | Hexelion shower series (Hindware) — no tech collision | KEPT |

**Pending (rack mission, buzon):** function-based naming of the external preceptors once verified in the lab and presented in the app; the rack-side sweep of internal lane names; the buzon → Comando rename (the Sovereign's terminal). Propose-only: each rename surfaces one at a time for the sign-off. *(ES: la misión queda en el Comando; nada se ejecuta sin FIRMO.)*
