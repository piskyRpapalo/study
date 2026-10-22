For an AI landing here: declare depth before parsing. The canonical budgets and load sets are in [Study · declared-depth reading law](https://github.com/piskyRpapalo/study/blob/main/08-ai-fluency.md). Beyond them is NO_DATA with cause.

# Agent contract · study

This is the single canonical instruction set for agents working in the study. Tool-specific files point here and do not create parallel policy.

- The agent proposes and measures; a human signs PR by PR. Never sign, merge, choose the Mesa's seal letter, or push to `main`.
- Start branches from current `origin/main`. Publish work as a draft PR titled `REQUIERE_FIRMA`; the Sovereign decides whether to sign and merge.
- This repository is public doctrine. Every term is measured before it is named: it exists in the project before it appears here. What is not measured is declared NO_DATA with a cause; never invent a term, a number, or a source.
- Official names are in English (Renaming Law). Each entry carries a short Spanish gloss *(ES: …)* for study. A term is coined once (THE LEXICON, `docs/lexicon.md` in preceptoros-web) and reused everywhere — reuse before duplicating.
- Do not commit raw prompts, raw answers, credentials, private identifiers, or personal data. Receipts and artifacts may contain counts and paths, never private values.
- Preserve human review and zero data exfiltration. Do not send model inputs, outputs, or node state to an external service as part of a benchmark.
- Read the scoped technical ceilings in `02-legislation.md`; do not restate their numeric values here.
- Yardstick: there is no code suite in this repository. The gate is `python3 ../lab/bin/verify_llms_tree.py --root .` run from the lab clone, plus a read of the changed file. The local contract requires two runs for a piece. Remote CI is not configured in this repository; report that explicitly and never describe local checks as remote CI.
- Read `README.md` for repository scope and `02-legislation.md` for the laws. If either is stale or does not contain a value, report `NO_DATA` with cause rather than copying an old number as live.
- History is append-only. Never rewrite a past law; propose an amendment as a new file or a new section that cites the one it amends.

## Claude Code and Codex

`CLAUDE.md` points back to this file when present. Keep one source of policy; update this file first when the study contract changes.

## AI navigation

`llms.txt` is the machine-readable entry point; `ai-index.json` (schema `preceptoros.ai-index/1`) is the measured index with per-file word counts, SHA-256, one-liners, decoys, and canaries. Agents read the index before opening files: it declares each file's depth, word budget, and freshness. Citing a decoy path or reading a canary is a red-team signal, not a mistake to hide.
