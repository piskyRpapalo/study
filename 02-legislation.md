# 02 · Legislation — the standing laws

- **D1 (language law)** — English only in served code; no comments in served code. The D1 Guardian catches stray Spanish before commit.
- **D3 (file-name map)** — The regulated renaming of served files (mar.js→sea.js, cria.js→brood.js…). Adopted as official; executed piece by piece under sign-off. Never all at once.
- **one-piece efficiency rule (16,384 B)** — One piece = one file ≤ 16,384 B. Over the rule: prune or declare a split; the rule is never raised silently. This is an efficiency rule, modifiable by the Desk (D-B, FIRMO 2026-10-22); it is not a security limit. The 25 MiB deployed-chunk ceiling stays a technical limit.
- **channel ceiling (1,024 B)** — The body of a channel event is under 1 KiB; it is rejected whole if it does not fit, never truncated.
- **append-only** — History is only added to, never rewritten. An amendment is a new entry, not an edit.
- **single-writer (no HLC this phase)** — One writer per register: insertion order IS causal order; `utc` is declared, carries no authority, and orders nothing. Hybrid logical clocks would only enter with multiple writers, under a separate sign-off.
- **scrub** — Removing private names from public artifacts; figures and paths stay, names go. The scrub list (fail-closed, private) is distinct from the forbidden-names law: two different lists, neither substitutes the other.
- **forbidden as names** — A standing list of words that may never be coined as official terms, in any language. They appear in the Lexicon only as the law that bans them.
- **stamps** — LIVE · STALE · STATIC · SIMULATED · NO_DATA · ERROR. Every figure travels with its stamp; SIMULATED is never dressed as measured.
- **NO_DATA doctrine** — What is not measured is declared NO_DATA with a cause, never invented. "NO_DATA, cause: X" is a valid answer; a guess is not.
- **A11Y law** — Text and drawing never cover each other; text moves to the left side when it covers art. Accessibility is law, not taste.
- **AI Act Article 14 pieces** — The app carries compliance artifacts (a game-policy file and a node-decide script aligned with EU AI Act Article 14, human oversight). Compliance pieces are declared, never claimed: no legal-compliance claim is ever made from the shape of an artifact.
- **push embargo** — One machine of the fleet sits under a permanent push embargo; nothing is ever pushed there. Public traffic is zero: the app is local-first; the web makes zero external requests on load.
- **external-collision law** — A coined term that collides with a live third-party product in the project's own category is renamed; a collision with a generic word is absorbed by definition. Verdicts live in `10-collisions.md`, each under the Sovereign's sign-off. *(ES: ley de colisión externa — choque con producto vivo en la propia categoría se renombra; choque con palabra genérica se absorbe por definición.)*

## Amendment · scoped technical ceilings · 2026-10-22

This entry governs active technical ceiling references; earlier shorthand remains historical and does not define a second limit.

- **deployed chunk ceiling (25 MiB)** — One deployed chunk may not exceed 25 MiB. This is not a whole-site first-load budget.
- **source-piece efficiency rule (16,384 B)** — One source piece is one file of at most 16,384 bytes. Efficiency rule, modifiable by the Desk; not a security limit.
- **channel-event ceiling (1,024 B)** — A valid event body is strictly under 1,024 UTF-8 bytes; 1,024 bytes and above are rejected whole.

These scopes are independent and cannot substitute for one another. The web first-load gzip gate remains a separate measured limit. This amendment supersedes the active-limit shorthand in `10-collisions.md`; its historical text is preserved.

## Amendment proposal · D5 lexical projection

Source: signed Study issue #3 (2026-10-20). This implementation clause remains a proposal until its draft is reviewed.

- The shared envelope is `preceptoros.lexical-projection/1`; its projection is read-only and grants no authority.
- A projection contains only declared fields. Missing or invalid source data is `NO_DATA` with a cause; no field is guessed or filled with a default.
- The compact UTF-8 payload is strictly below 1,024 bytes. At or above the limit, reject the whole payload with a cause; never truncate it.
- A matching visual, mathematical, and audible state is a separate measured claim. Until paired frames and hashes pass the same gate, isomorphic parity remains `NO_DATA`.

## Amendment · ODD routing · 2026-10-28

Source: the Sovereign's ODD decree (2026-10-28, transcribed in the Book), inspired by Gentle Shell's Organic Driven Development. The workflow is adopted, not the harness: the Desk, the gates, and the Book keep their roles.

- **ODD (organic driven development)** — Explore → implement → proportionate checks is the standing workflow for substantial authorized work. Small, understood work creates no durable task artifact; investigation and proposal-only work stay read-only.
- **feature document** — Substantial work is tracked in `odd/tasks/<feature-name>.md`: objective, checklist with stable IDs, verification evidence, next step. One feature, one document, one name — no parallel plans, no task noise.
- **work-unit commits** — Commits land as reviewable work units (about 400 authored lines, advisory, never a cap). An oversized forecast routes through a feature-branch chain; in unattended mode the chain is chosen and recorded, never waited on.
- **the standing-signature rule** — A step that would need a signature never halts the work: the standing signature is searched for in the corpus first (the signed Book, ideas, examples, and jewels count as signed); the modification is recorded and the work continues. A fresh FIRMO gates the merge of the exact head — never the building.
- **delivery gates unchanged** — ODD unblocks the work, not the merge: checks that can go red, the receipt, HITL by hash, and the Sovereign's FIRMO on code, seal, and infrastructure heads are never skipped.


## Amendment · methodology relief · 2026-10-28

Source: the Sovereign's decree (2026-10-28): preceptors may use their own judgment (the "optimizaciones" clause) to improve the methodology on risk-free work — the goal is to liberate the Sovereign's time.

- **methodology relief** — When a risk-free task is made needlessly hard by an old law, the preceptor reviews that law and proposes the change with the delivery. The proposal is part of the delivery, never a blocker. Delivery gates on code, seal, and infrastructure heads are never skipped.

## Amendment · carbon fidelity · 2026-10-28

Source: the Sovereign's decree (2026-10-28, the isometric-colony feature doc).

- **carbon fidelity** — A render is right when a human eye reads it at a glance and a small local model can parse the same state. One state, many renders (D4/D5): the eye, the ear, and the small model all read the same state, and the render serves the human reader first.


## Amendment · conditional carbon signatures · 2026-10-28

A CONDITIONAL CARBON SIGNATURE (firma del carbono) is a standing signature by OBJECTIVE: the Sovereign fixes the objective and delegates the how. The preceptors must reach the objective, solving the architecture and respecting every standing law — the manner found does not matter; the objective and the laws do.

Coverage: the signature covers the work that reaches the objective, conditional on (a) all standing laws holding (SCRUB, determinism, the 1,024-byte frame law, verification with screenshots, honest NO_DATA with cause), and (b) the Desk verifying the objective is reached before the final piece merges.

Fleet clause: when the objective needs the fleet's eyes or hands, the Sovereign's devices act as preceptors — any lawful way possible under the signature.

Scope: a carbon signature covers the objective and its path; it does NOT waive the signing tray — pieces of value (served code) still require the per-piece FIRMO on the exact head.

First exercise (2026-10-28): watch and measure the reference video's images; transcribed in the signing book (buzon#30, FIRMO DEL CARBONO 20261028-c1).


## Amendment · THE MARCH — the living name of the workflow · 2026-11-04

Source: the Preceptor Contract (preceptoros-companion/CONTRACT.md, FIRMO 2026-11-03, clauses 3 and 8), coined in the Babel registry (registry/coins-2026-11-04.md). The amendment of 2026-10-28 (ODD routing) stands unchanged above, with the names of its date: history is append-only.

- **THE MARCH (ES: LA MARCHA)** — the living name of the workflow coined as ODD (organic driven development). In living texts THE MARCH replaces ODD; in every folio of its date, ODD speaks with its own name. The content of the routing amendment (2026-10-28) is unchanged: explore → implement → proportionate checks; work never halts for a signature; the signature gates the merge, never the building.
- **ps (the Preceptor-Sweep)** — the sweep of the living canon, run at the Sovereign's command; each pass declares depth and budget before sweeping (clause 3, verbatim).
- The substitution lands piece by piece under the standing THE MARCH FIRMO (docs-only coverage); sealed history is never rewritten.

## Amendment · ADS-STE100 — agent dependency continuity · 2026-11-20

**Source of authority:** [Preceptor Contract · ADS-STE100](https://github.com/piskyRpapalo/preceptoros-companion/blob/main/CONTRACT.md), integrated by [Companion PR #38](https://github.com/piskyRpapalo/preceptoros-companion/pull/38) (merge `c6a404f281875d944608685a59c84e4aad7641d3`). This section **indexes and clarifies routing**; the Companion Contract remains the single normative source. *(ES: continuidad de dependencias entre agentes; la Mesa coordina, el Carbono firma).*

- **Measured 600-second wait.** When an agent's next step depends on another agent, record the task, owner, counterpart, expected output, start and deadline. Only verified elapsed time triggers recovery; unavailable runtime is `NO_DATA(timer_not_measured)`.
- **Return to the existing Mesa.** At the 10-minute trigger, consult the appropriate existing Mesa and current claims, then choose another independently authorized task. Do not invent a mission, overwrite another owner's files or treat the original dependency as finished.
- **Original agent becomes judge.** If a lawful alternative needs parallel execution, create at most **one** bounded, authorized recovery worker for that dependency. The original owner remains its supervisor and judge, with a separate claim, acceptance criteria and receipt. If no agent/tool/budget/grant exists, declare `NO_DATA(parallel_agent_unavailable_or_not_authorized)` and continue other safe work.
- **Reconcile once.** Keep the original reply under observation while execution is actually active; on return compare results, stop duplicates and allow only one writer for irreversible effects. A paused/offline session cannot claim continuous monitoring.
- **No timer overrides consent.** Human approval, safety checks, owner grants, provider budgets, E-STOP and FIRMO never expire after 600 seconds. Role-specific Markdown profiles route this law with source revision; profiles do not create permissions.

**Acceptance:** an induced dependency with a measured 600-second trigger, Mesa/claim selection, no more than one recovery worker, a judge verdict, no double write and a scrubbed receipt. `NO_DATA(dependency_recovery_E2E_not_verified)` until a real runtime test passes. Readable, audible and machine-facing Acho states must agree; untested channels remain `NO_DATA(cause)`.


## Amendment · effective file-size scopes after 2026-11-01 decree (documented 2026-11-22)

**Source:** dated [Sovereign decree of 2026-11-01](https://github.com/piskyRpapalo/roadmap/blob/main/odd/DECRETO-TECHO-NUEVO-20261101.md) (private Roadmap, may require permission); publicly cross-recorded in [LAB AGENTS.md](https://github.com/piskyRpapalo/lab/blob/main/AGENTS.md). *(ES: se revoca el techo general de archivo, no el del recibo ni el del bloque CDN.)* This is an append-only correction to the *effective reading* of the dated 2026-10-22 source-piece paragraph above, **not** an erasure of that history or a runtime change.

- **General source-piece/file 16,384-byte efficiency ceiling: REVOKED** by 2026-11-01. The original historical provision above remains exactly as enacted on its date. Do not silently enforce or reintroduce it as a universal file-size gate.
- **Channel event / signed or unsigned receipts: strictly below 1,024 UTF-8 bytes remains** as independently scoped under the channel contract. This is distinct from the source-file size and must never be relaxed merely because a larger piece fits on disk.
- **Deployed chunk: at most 25 MiB per block remains**, separate from a whole-site first-load budget and from Android performance constraints. Passing this limit is not proof that Android can render the payload.
- **Specialized schema budgets, including custom world pages, immutable envelopes and frames:** `NO_DATA(scope_not_reverified_per_own_contract)`; do not infer their repeal or validation from the general source-piece decree. Each must be checked against its own verifier before a code change.

See the [Babel reconciliation review](https://github.com/piskyRpapalo/babel/pull/9); Babel remains the one vocabulary house. This Study amendment clarifies legislation only and coins no term. **Risk:** changing a parser based on a doctrinal note could accidentally relax a distinct security/safety fence. **Next:** an independent scoped validator inventory and two separate test runs under its owning repo before any code migration. **Evidence from this action:** GitHub file read/write only, `NO_DATA(local_tests_not_executed)`; no active security study, TRAIN-02 training, CLI or service was touched.


## Current reading · three ecosystem size domains (Sovereign clarification 2026-11-22)

**The former 16,384-byte source-file ceiling has no current force.** It is historical above, not a fourth gate to enforce. Also retired is any generic 10 KiB or 16 KiB file-size rule under the same decree. *(ES: solo Cloudflare, GitHub y Acho como ámbitos globales de tamaño; las pruebas históricas no legislan hoy.)*

1. **Cloudflare static asset:** at most **25 MiB** per asset/block (26,214,400 bytes). This does not define a whole-site byte limit and does not prove mobile performance. [Cloudflare's current Workers static-asset limits](https://developers.cloudflare.com/workers/platform/limits/) corroborate 25 MiB.
2. **GitHub repository:** choose **1 GB** (1,000,000,000 bytes) as the ecosystem's *repository-level operating budget*, not a universal hard platform ceiling. GitHub recommends keeping repositories ideally below 1 GB; ordinary Git files have additional enforced 100 MiB upload constraints. See [GitHub large-file documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github). Neither represents permission to bypass GitHub's actual API, push, or LFS restrictions.
3. **Acho frame and receipt:** payload strictly **below 1,024 UTF-8 bytes**. A nominal “1 KB” means the existing Acho transport contract; 1,024 bytes exactly are refused when the schema uses a strict bound. The human-visible, machine and accessible/audible projections must agree on one validated source record or report `NO_DATA(cause)`.

**No global fourth source-piece limit exists.** Declared reading-depth budgets are context-selection controls, not universal file ceilings; source-level validation continues to check type, path, schema, signatures, hashes, trusted grants and protocol-specific confidentiality. A historical 16 KiB constant inside a *runtime input or transport* must be audited before changing it: remove the obsolete size policy without letting untrusted content bypass parsing or memory/DoS protection. This distinction does not resurrect the 16 KiB general ceiling.

**Reconciliation:** LAB's legacy file-size checks are being retired in [LAB #247](https://github.com/piskyRpapalo/lab/pull/247) pending CI and exact-head review. Historical law paragraphs stay as dated evidence, not active gates. **Risk:** a code or test fixture still enforcing 16 KiB after revocation; **next:** scoped diff plus two CI passes per owning repo and an independent runtime E2E for served inputs. **Current check:** `NO_DATA(study_test_execution_not_requested)`.
