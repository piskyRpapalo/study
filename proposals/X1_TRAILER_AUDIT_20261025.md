# X1 · Model / Agent / Run trailer audit

**State:** proposed; read-only inventory. This file does not change any target repository.

## Scope and method

Scanned every commit reachable from the observed default-branch head in each named repository. Study, lab, PreceptorOS, preceptoros-web, and p0x were read from their local clones after fetching; buzon was read from its GitHub default branch. The parser recognizes standalone labels and the compact `Agent: … · Model: … · Run: …` form. Counts below are trailer-value occurrences, not commits. Refs are the complete heads observed in this run; they can advance.

| Repository | Ref | Head | Commits scanned |
|---|---|---|---:|
| study | main | `57cfe0f60f3b90d85df3fc52dc6556fae82bbf7b` | 121 |
| lab | main | `a60908d2423b4f33e7dcfe8867cba6be5342edff` | 174 |
| PreceptorOS | main | `a88bf42a971d5e6289956333dcfd22c4c022b968` | 463 |
| preceptoros-web | main | `b23a512aa6c232512dbe93fef108d7e7a70e58be` | 1,248 |
| p0x | master | `9656ff3d4aad6909f22256c4544cf04b98ef0ad3` | 863 |
| buzon | main | `472caf94353d78b7c29d0cee282e86867cbe35a3` | 69 |

Total: 2,938 commits. `s`=study, `l`=lab, `a`=PreceptorOS, `w`=preceptoros-web, `p`=p0x, `b`=buzon. Omitted cells are zero.

## Complete distinct-value mapping

Provider labels follow the trailer value itself. `GPT` and `Codex` are mapped to ChatGPT by their literal family/product names. A role or run label does not identify a provider. `Vibe` and `GLM (Vibe)` do not identify Mistral or ChatGPT from evidence in this audit; they remain `NO_DATA` rather than being guessed.

| Field | Exact value | Result | Occurrences by repository |
|---|---|---|---|
| Agent | `Codex` | ChatGPT | a=2, w=4 |
| Agent | `orquestador general (Mesa · terreno)` | NO_DATA, cause: role label has no provider | s=3, w=1, p=2 |
| Agent | `preceptor-externo-constructor` | NO_DATA, cause: role label has no provider | s=3, l=8, w=11, p=1 |
| Agent | `preceptor-orquestador-github` | NO_DATA, cause: role label has no provider | s=21, l=6, a=9, w=20, p=10, b=4 |
| Model | `Codex` | ChatGPT | l=6 |
| Model | `GLM (Vibe)` | NO_DATA, cause: provider not evidenced in the audited source | s=25, l=8, a=7, w=22, p=6 |
| Model | `GPT-6` | ChatGPT | a=1, w=2 |
| Model | `GPT-6.1-Sol` | ChatGPT | a=1, w=6 |
| Model | `Vibe` | NO_DATA, cause: provider not evidenced in the audited source | s=1, a=2, w=2, p=8, b=4 |
| Model | `gpt-6.1-sol` | ChatGPT | s=3, l=2, w=7, p=1 |
| Run | `NO_DATA` | NO_DATA, cause: run identity absent in source value | s=28, l=10, a=9, w=37, p=7 |
| Run | `local-only` | NO_DATA, cause: execution location is not a provider | l=6 |

No trailer value explicitly names Mistral in the scanned history. The provider assignments based on `GPT`/`Codex` are literal-name mappings, not independent runtime verification.

## Commission decisions recorded

- **X5:** record the web `BUDGET` line as a `CEILING`, not a measurement. This audit does not edit web `llms.txt`.
- **X3:** record the three `navegante/*` merges in app#80, lab#57, and study#26 as pre-rule historical exceptions. No history rewrite.

## Receipt

Read-only history scan: six default branches, 2,938 commits. Distinct values mapped: GPT/Codex → ChatGPT by literal name; provider ambiguity and run/role labels → `NO_DATA` with cause. X5 and X3 recorded from study#61. No target repo changed. No raw prompts, credentials, private network values, or personal values included. Local study yardstick passed twice; changed file read after measurement. State: proposed, awaiting FIRMO.
