# 02 · Legislation — the standing laws

- **D1 (language law)** — English only in served code; no comments in served code. The D1 Guardian catches stray Spanish before commit.
- **D3 (file-name map)** — The regulated renaming of served files (mar.js→sea.js, cria.js→brood.js…). Adopted as official; executed piece by piece under sign-off. Never all at once.
- **one-piece ceiling (16,384 B)** — One piece = one file ≤ 16,384 B. Over the ceiling: prune or declare a split; the ceiling is never raised silently.
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