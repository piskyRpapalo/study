# Natal training additions (ES: adiciones natales de entrenamiento y flujo) · 2026-11-10

**ID:** STUDY-NATAL-FLOWS-20261110. **State:** PROPOSAL, research-only, docs-only. Companion to STUDY-HARVEST-ECO-20261110 (study PR #104, Agent Codex): the four directions below were cross-audited against that piece's full text and are NOT duplicated there. **Agent:** preceptor-orquestador-github (VIGIA) · **Model:** GLM (Vibe) · **Run:** NO_DATA (rack not accessed; every source read, not assumed).

**Single mission catalogue:** Web canon §9. This file is NOT a second mission catalogue; no mission is created, renumbered, chosen, sealed or promoted. Positions are suggestions only.

## Ground truth and collision check

Read: the 40 existing study/proposals entries (titles swept; COSECHA8_PUERTA_BENCHMARKS, ORCHESTRATOR_IDEAS25OCT_A9 and PROPUESTA-ESTADO-VECTORIAL read in full: no overlap), the FULL text of PR #104, buzon#53 (cross-audit acta ·6755980784; harvest acta ·6755912330), and Web canon-arena-and-duels.md (measured 2026-11-10, 15,094 B): juez.js already judges 2 branches with the pure engine, and rating.js computes integer Elo with a precalculated table. study/14-bench-families.md defines the 7 benchmark families.

## Direction 1 — Natal process-pair corpus (TRAIN, not only evaluate) (ES: pares natales para entrenar)

**Destination:** the canon training mission (A9 in the VIGIA harvest; the catalogue is canon §9). **Problem:** PR #104 uses PRM800K for process-error SCORING (E3/B4); nothing proposes a native TRAINING corpus. **Verified sources:** the hilo's own fields (no_data_heredados, no_data_resueltos, hash_previo) plus the judge's verdict are measured house ground truth; openai/prm800k (MIT, archived 2026-05-29, re-verified by VIGIA) is the FORMAT reference for (step, label) pairs, never a redistribution source. **Native adaptation:** each resolved no_data with its hash chain and judge verdict becomes one pair (input with gap, resolved output with cause); train/val split respects the hash_previo chain; targets LoRA or baked system prompt + RAG for local models (skills harvest: prompt as skill with VARA). **Measure/acceptance:** >=100 real pairs measured from the hilo or NO_DATA with cause; training script deterministic across 2 runs (fixed seed); no pair leaves the private side without SCRUB. **Risk:** train/val leakage; the trainer grading its own students. **Next minimal piece:** one offline pair-extraction script over existing hilo data, propose-only. **NO_DATA:** current pair count; end-to-end training run.

## Direction 2 — Integer tables as the native balance pattern (ES: tablas enteras)

**Destination:** D4-D6 balance and decisor weights. **Problem:** PR #104 asks for deterministic odds without replacing the engine, but does not register the house precedent: balance as precalculated integer tables. **Verified sources:** Web rating.js (integer Elo, precalculated table), gacha.js and combat_ticks.js (seeded, already in Web); jakejack13/gachapy and rexor12/gacha.py (both MIT, read 2026-11-09) contribute pity and curve MATH only. **Native adaptation:** pity counters, drop curves and progression curves become sha256-sealed integer tables measured in bytes; no floats in game balance; RPG-Paper-Maker battle-system.md is a math-only reference (licence NO_DATA, no assets copied). **Measure/acceptance:** table sizes measured; 100% replay parity with the seeded engine on existing cases. **Risk:** table bloat past the size ceiling. **Next minimal piece:** one table beside the existing gacha engine, propose-only. **NO_DATA:** curve data from live play.

## Direction 3 — Native self-repair flows A/B/C (ES: flujos nativos)

**Destination:** workflows binding existing missions; no new mission. **Problem:** PR #104 registers mechanisms, not flows; the house hardware runs all day with no nightly watchman. **Flow A (night watch):** cron (M-P1-02) + varas D1-D10 with receipt -> eventos.db -> triage -> PR REQUIERE_FIRMA (red never merges). **Flow B (live index):** local index of recibos + hilo + actas feeding the F-01 WBR and the BUSCAR clause (M-P1-06); xerj-org/xerj (Apache-2.0, read) is retrieval-math reference, not a service to import. **Flow C (natal training):** the flow of Direction 1. Each flow: one owner, one ledger, propose-only. **Measure/acceptance:** each flow emits a receipt per cycle; a week of cycles or NO_DATA with cause. **Risk:** a flow that heals without a human gate. **Next minimal piece:** Flow A cron + one vara, offline first. **NO_DATA:** end-to-end cycle run.

## Direction 4 — Judge k-branches for arbitration (ES: juez k-ramas)

**Destination:** M5 arbitration. **Problem:** PR #104 sends ToT/beam to ORCHESTRATION (A6/B4); the judge still rules with 2 branches only. **Verified sources:** princeton-nlp/tree-of-thought-llm (MIT, read 2026-11-09) contributes the k-branch concept; juez.js already plays 2 branches with the pure engine, so k>2 extends measured ground truth, not a new service. **Native adaptation:** for verdict-sensitive cases the judge plays k deterministic branches with the pure motor and records the spread before ruling; LATS-style failed-trajectory reflection (PR #104) can feed the hilo no_data -> solution_propuesta loop on the GAME side, complementing the orchestration side already proposed. **Measure/acceptance:** k=3 vs k=1 delta on existing replay cases: verdict flips, extra ticks, wall time; adopt only if delta is measured. **Risk:** k-times cost for zero verdict change. **Next minimal piece:** offline k-spread report on existing canon cases. **NO_DATA:** measured delta.

## Provenance ledger (licences read, not inferred; VIGIA 2026-11-09/10)

| Source | Licence / state |
| --- | --- |
| openai/prm800k | MIT, archived 2026-05-29 (re-verified) |
| jakejack13/gachapy · rexor12/gacha.py | MIT (read) |
| princeton-nlp/tree-of-thought-llm | MIT (read) |
| xerj-org/xerj | Apache-2.0 (read) |
| RPG-Paper-Maker battle-system.md | licence NO_DATA; math only |
| spcl/graph-of-thoughts | CORRECTION to PR #104: metadata reads NOASSERTION but the LICENSE file is readable (ETH Zurich, BSD-style); no code copied either way |
| Web rating.js / juez.js / gacha.js | internal measured ground truth (canon-arena-and-duels.md, 15,094 B) |

**Collisions:** none with the 40 existing proposals (titles swept, 3 closest read in full) nor with PR #104's full text (cross-audited 2026-11-10). This piece adds the TRAINING, TABLE, FLOW and ARBITRATION sides absent from the Codex harvest. Vendor figures: NO_DATA without identical fixture and local two-run evidence.

**Mesa:** buzon#53 (actas ·6755912330, ·6755980784). No sign-off by any agent, no main write or merge. FIRMA del Soberano manda.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA