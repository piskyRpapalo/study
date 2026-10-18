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

## Fourth wave — the corpus unification (measured in the October corpus 2026-10-18; repo counts pending)

**What this is:** the terms coined while unifying the vocabulary against the October corpus (the Papers). Counts inside the corpus were measured by reading; counts in the repos are pending and declared NO_DATA until counted. All names are RENAME-SUGGESTED until the Sovereign's sign-off. *(ES: la cuarta ola — los términos que la unificación del corpus acuñó; nada sellado sin FIRMO.)*

| Term | ES pair | What it is |
|---|---|---|
| countersign | contrafirma | the game's mutual signature (the attacker signs the challenge); never sign-off, never signature |
| one state, many renders | un estado, muchas vistas | channel N1's signed finding: two stores = a broken contract |
| telemetry vs measurement vs receipt | telemetría · medida · recibo | the actor's declared self-report vs the yardstick's verdict vs the worker's form — three acts, never one |
| privilege levels N0–N4 | niveles de privilegio | the node's authority ladder; NOT the decision tiers (tier 1 / tier 2) — a different ladder |
| the Papers | los Papeles | the October corpus of manifests (ideas, sessions, canon drafts); declared evidence, never code — distinct from the Corpus (XERJ) |
| the State Buoy | la Boya del Estado | Proof of Tick with a game body: alive · fading · NO_DATA · unattended |
| the Observatory | el Observatorio | STALE made playable: old data shows its age on screen |
| the Reef of Gravestones | el Arrecife de Tumbas | zero retention WITH receipt: the Necropolis's game face |
| the Latency Crystal | el Cristal de Latencia | latency_crystal.js measured on the metal; hardware classes, never quarantine shelves |

**New GREY AREA pairs:** the Latency Crystal's classes (gold/silver/bronze of the measured link) vs the Bronze/Silver/Gold quarantine shelves · the Papers (October manifests) vs the Corpus (XERJ) · privilege levels N0–N4 vs decision tiers · telemetry vs measurement vs receipt.

**Second sowing — the buried jewels, surfaced by the inverse re-reading (measured in the October corpus; sown before the sign-off so nothing is lost):**

| Term | ES pair | What it is |
|---|---|---|
| the Stone Path | el Sendero de Piedras | the ledger made game: one river stone per measured closure, append-only, walkable |
| the Valve | la Válvula de Polifonía | the sandbox with a game body (closed = safety; open = risk); the Wasmtime cell (64 MiB, zero I/O) is its machine face — one piece, two names absorbed |
| Compressed Oxygen | el Oxígeno Comprimido | the signed question-answer-verdict triple as a resource |
| the Breeder's Medal | la Medalla de Criador | verifiable recognition, never a balance |
| no anonymous debt | sin deuda anónima | a metric without an assigned measurement task is not an absence: it is an anonymous debt — every tray row carries owner, command and seal (the Signing Tray's foundational law) |
| the Eye's ports | los puertos del ojo | declared 8790 in the September manifest; the Eye today is 8807 + S110; room 8831 lives only in the digests — Necropolis aliases, history intact |
| the bus channels | los canales del bus | thegame-estado · thegame-taller · boya · radio-estado · mapa · terminal-cangrejo · thegame-batalla — each panel declares its channel and LIVE/STALE(+Δ)/NO_DATA |
| the regulatory renames | los renombrados regulatorios | the corpus declares RENAME PENDIENTE in its customs section and the state radio's file carries a regulatory name — debt the corpus already declared; enters the renaming map piece by piece under sign-off |
| false green's origin | el origen del falso verde | J-WEB-11 (September corpus): the green seal only if the rack is measured available, and the counter that doesn't count — the corpus legislated it before the Study coined it |
| the crab anatomy | la anatomía del cangrejo | Shell = Core · Claws = Army · Legs = Forest · Eyes = Lighthouse: the module-name source for the renaming map, one sign-off per name |
| the Crab Account | la Cuenta Cangrejo | the corpus declared it THE structural decision of the protocol: bridge phase (the agent travels on YOUR charter) vs roving phase (the agent's own charter) — the choice is the Sovereign's, pending |
