# Front 6 · system and profile naming proposal

**Status:** proposal for human review; no canon is changed by this document.

| Location | Current → proposed | Reason | Collision measurement | Estimated cost |
| --- | --- | --- | --- | --- |
| `07-hardware.md:3` | “the Rack — The lab machine (a beelink)” → “the Rack — the local computing environment; hardware-specific facts belong to the measured device entry.” | Use the Rack as the system concept rather than equating it with one hardware brand. | On tracked Markdown at base `59ed7f757c384ab815a03bd41f091c4bfaba9431`: 1 matching line for `beelink`, 20 for `the Rack`; the brand match is confined to this entry. | One definition-line edit; no runtime or route changes. |
| `11-repos.md:11` | “piskyRpapalo — the profile (HEXELION)” → “piskyRpapalo — the public profile, named Hexelion.” | Keep Hexelion as the public profile name and separate it from the system concept. | 4 matching lines for `Hexelion` in tracked Markdown at the same base; the profile entry is one. | One definition-line edit; repository census remains unchanged. |
| `09-lore.md:10` | “Hexelion — The reader behind the switch” → “the Rack — the local system behind the switch; Hexelion names the public profile only.” | Replace the system/reader label with the shared system concept while preserving Hexelion for the profile. | The same 4 `Hexelion` lines include this lore entry; `the Rack` has 20 matching lines before the proposal. | One definition-line edit; lore meaning requires Sovereign review. |

## Scope and non-decisions

This proposal changes no canon file, hardware inventory, repository name, profile, or device record. It recommends a terminology-only follow-up edit to these three lines. The proposed phrase in `09-lore.md` changes the referent from “reader” to “local system”; that semantic shift is a decision point, not a measured equivalence, and remains unapproved until the human review.

Collision counts are matching tracked-Markdown lines from `origin/main` at the base above, case-insensitive. They are not global GitHub search counts. No complete cross-repository collision scan was run: **NO_DATA, scope limited to this Study tree**.
