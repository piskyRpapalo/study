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
