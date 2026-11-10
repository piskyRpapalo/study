# Native ecosystem harvest (ES: cosecha nativa de ecosistemas) · 2026-11-10

**ID:** STUDY-HARVEST-ECO-20261110. **State:** PROPOSAL, research-only. The Sovereign approved investigation of THREE mechanisms on 2026-11-10; approval does not sign or merge a future PR head. **Agent:** Codex · **Model:** GPT-6 · **Run:** NO_DATA (rack and end-to-end not accessed).

**Single mission catalogue:** [Web canon §9](https://github.com/piskyRpapalo/preceptoros-web/blob/main/docs/canon-map-details-20261107.md). This file is NOT a second mission catalogue; no mission is created, renumbered, chosen, sealed or promoted. Potential dependency positions are suggestions only.

## Ground truth and collision check

Read `study/AGENTS.md`, `08-ai-fluency.md`, `05-contracts.md`, `10-collisions.md`, `02-legislation.md`, `roadmap/{NORTE,ROADMAP,PUENTES,COLISIONES,REPOS-VECTORIAL}.md`, 40 existing `study/proposals` entries, Web canon §9, `buzon#53` and `buzon#19`. Prior overlapping proposals: `COSECHA8_PUERTA_BENCHMARKS_20261023.md`, `ORCHESTRATOR_IDEAS25OCT_20261025.md`, `PROPUESTA-ESTADO-VECTORIAL-20261102.md`; previously discussed Mesa candidates A6-SKILL, P3-SEARCH, E3-PRM and B6-GRAPH.

Existing CODE, not a claimed deployed SERVICE: [p0x `hexelion/harness/cerca.py`](https://github.com/piskyRpapalo/p0x/blob/main/hexelion/harness/cerca.py) enforces a tool allowlist, 8-step ceiling and SCRUB; `herramientas.py` selects canonical MCP schemas. [Web `atlas/puros/acho.js`](https://github.com/piskyRpapalo/preceptoros-web/blob/main/atlas/puros/acho.js) already validates closed `preceptoros.acho/1` frames below 1,024 UTF-8 bytes; [`acho_cases.mjs`](https://github.com/piskyRpapalo/preceptoros-web/blob/main/atlas/puros/acho_cases.mjs) tests parity and the 1,023/1,024 boundary. [Lab benchmark index](https://github.com/piskyRpapalo/lab/blob/main/benchmarks/README.md) and `study/14-bench-families.md` already define benchmark/receipt families. App `memory_lookup.py` is bounded SQLite FTS; `decisor.py` abstains instead of inventing confidence; Nexo `vector_index/README.md` documents SHA-verified optional vector search with real retrieval E2E NO_DATA. Web has seeded `public/game/gacha.js`, `public/game/combat_ticks.js`, and replay cases.

**B6:** [WEB PR #798](https://github.com/piskyRpapalo/preceptoros-web/pull/798) already offers pure D/A/I calculations and synthetic fixtures; it was unmerged at inspection and its source adapter remains NO_DATA. Never duplicate its calculator or claim measured historical distances.

## Signed research jewel 1 — MCP reverse-call trust (ES: frontera inversa)

**Classification / destination:** **AMPLIAR** A6, B3, F1/F5. **Problem:** client-to-tool name checks do not cover all server-originated nested model/tool requests, tool substitution or cross-source instructions.

**Verified inner source:** `modelcontextprotocol/modelcontextprotocol/docs/specification/2026-07-28/client/sampling.mdx` at commit `632a0c9a65c9b4fbc889d8aface5c9cf5edef3b7`. Repo licence metadata: NOASSERTION; avoid copying protected text. **Critical correction:** Sampling was deprecated on 2026-07-28; new implementations SHOULD NOT adopt it. Research it as a legacy attack/compatibility surface, not a new gateway.

**Native adaptation:** reuse `p0x/harness/cerca.py`; check explicit `direction`, `capability`, `policy` outside the model; fail closed with a typed NO_DATA cause. Reuse the existing HITL boundary for writes. No new control plane.

**Measure / acceptance (proposed):** >=12 offline allowed/poisoned/revoked/nested-call cases, n=2 independent runs; 0 forbidden executions, 0 unauthorized network requests, and no authorized-read regression. Keep only case IDs and hashes in public. **Risk:** testing a policy at the wrong boundary gives false security. **Next minimal piece:** pure permit/deny fixture in existing harness. **NO_DATA:** no real MCP transcript or live safety E2E.

## Signed research jewel 2 — Acho grammar admission (ES: gramatica de entrada)

**Classification / destination:** **AMPLIAR** A9, C8, B8, F7, not a new Acho format. **Problem:** only if an actual authoring workflow needs textual syntax, parse it unambiguously before accepting the already existing structured frame.

**Verified inner source:** `lark-parser/lark/examples/calc.py` and `examples/turtle_dsl.py` at `9a4fb9c7458e8155636773a3cded0016d52516da`, MIT. These show grammar-to-AST and transformer patterns; do not copy a Python parser into browser code by default.

**Native adaptation:** a single optional closed subset -> AST -> canonical existing `preceptoros.acho/1` JSON -> current `Acho.valida`. Reject unknown, ambiguous or unsafe syntax, malformed Unicode, and >=1,024-byte frames. One accepted state, multiple visual/text/machine/audio projections.

**Measure / acceptance (proposed):** existing Acho cases plus 20 minimal grammar cases, n=2; valid round-trip invariance and 100% rejection of invalid test cases. No new served dependency unless its size is measured. **Risk:** unnecessary DSL and duplicate validator. **Next minimal piece:** one one-page grammar tied to a verified input requirement. **NO_DATA:** physical screen-reader and speech parity, no paired E2E recording.

## Signed research jewel 3 — Inference evidence manifest (ES: recibo de inferencia)

**Classification / destination:** **AMPLIAR** E3/E7, A6, F6; reuse existing Lab benchmark cards. **Problem:** temperature=0 and seed do not prove bitwise model-output reproducibility across software/hardware. Deterministic interpreter correctness and stochastic model output must not share a label.

**Verified inner source:** `ggml-org/llama.cpp/docs/function-calling.md` at `3b4d6ab3f79651935fba1dd93732f29022a7f5f5`, MIT. It documents `llama-server --jinja` and model-specific/generic function-call handlers. The reported universal `--tools all` switch was NOT verified there; outputting a tool call never executes or authorizes it.

**Native adaptation:** append model weight/build/template/config digests, tool registry and evaluator SHA, sample/dataset SHA, output/judge hash, backend class, UTC, status and causes to an existing Lab receipt. Do not create another benchmark DB. Maybe compare pinned Nix build inputs later.

**Measure / acceptance (proposed):** same local fixture run twice; 100% required fields measured or NO_DATA with cause; compare model byte equality separately from exact deterministic judge/tool outputs; pass@1, p95, token speed and power only when sensors are available. **Risk:** hash != sign-off, dataset leakage, mistaken vendor speed transfer. **Next minimal piece:** one SCRUBbed specimen beside an existing Lab benchmark. **NO_DATA:** actual host replay and sensor data.

## Four further inner-mechanism jewels (NOT separately signed)

| Source and code inside | Verdict / mission | Native adaptation, measurement, risk, next piece |
| --- | --- | --- |
| `Gentleman-Programming/engram/internal/store/generation_fence.go` @ `b53422f45c57c1003cc9c063c5a4e1fe1c694f27`, MIT | **AMPLIAR** A5/B1 | Reuse detection of SQLite/WAL/SHM generation replacement; fail closed on swapped files. Two injected-replacement runs, 0 stale successes. Linux/Windows file identity differs. Next: fault fixture in current App/Nexo owner; NOT another memory service. |
| `andyz245/LanguageAgentTreeSearch/hotpot/lats.py` @ `853d81614607dd27433faf17c7b0a7d660f95d22`, MIT | **AMPLIAR** A6/B4 | UCT nodes with visits/reward and failed-trajectory reflection under existing <=8-step gate. Test against single-branch baseline for answers, latency and calls. Source uses external GPT/requests: borrow mathematics, not runtime. Next: offline synthetic tree. |
| `benbjohnson/litestream/db_wal_rewind_test.go` @ `af28505f39a8e1afe9291febbe11e9926bd230aa`, Apache-2.0 | **AMPLIAR** E1/F6 | Restoration fault cases and SHA parity. Litestream is backup, NOT consensus; source database can gain an internal lock table. Next: restore-only fixture, no daemon. |
| `microsoft/graphrag/packages/` @ `34b2b67ae4601ad0b47bcd179fbe3f2a23aa0857`, MIT | **AMPLIAR** C5/B6 relationships | Pin explicit sourced requires/provides/affects edges over existing Nexo; compare sourced-path accuracy vs plain retrieval on 20 edges. GraphRAG README declares maintenance mode. Next: static graph fixture; no second corpus. |

## Complete compressed intake / no mission duplication

| Other external inner mechanisms | Verdict | Existing destination / measurement |
| --- | --- | --- |
| `reasoning-machines/pal/pal/`, `microsoft/ToRA/src/`, `hendrycks/math/modeling/math_equivalence.py` | **REUTILIZAR** | A6/E3 bounded math AST and independent answer equivalence; compare pass@1 to answer-only. NO generated `exec`. |
| ToT `src/tot/`, GoT `graph_of_thoughts/operations/`, rStar `rstar2_agent/` | **AMPLIAR** | A6/B4 bounded beam search first; MCTS only if delta-quality vs cost justified. |
| `openai/prm800k` (archived) and `EleutherAI/lm-evaluation-harness/lm_eval/tasks/` | **AMPLIAR** | E3/B4 process-error scoring and pinned tests. Vendor pass@1 and dataset redistribution rights NO_DATA pending independent verification. |
| XERJ `engine/crates/xerj-fts`, `xerj-query`, `xerj-mcp` | **AMPLIAR** | C5/E3 benchmark native FTS + Nexo vector vs XERJ hybrid, same local corpus: Recall@5, MRR@5, correct SHA, p95, RAM. XERJ is retrieval, NOT rack networking. |
| Openrig `packages/`, Gentle AI/Dot/Shell, both Jobpilot projects | **DESCARTAR** full framework | A6/F1: agent lifecycle patterns only; live browser job automation is not orchestration. Both `maazbin/jobpilot` and `suxrobGM/jobpilot` actually exist. |
| Gachapy, gacha.py, Darklings rollback, RPG Paper Maker `battle-system.md` | **AMPLIAR** | D4-D6 deterministic odds, signed replay and balance; don't replace existing engine or copy unlicensed assets. |
| `mattpocock/skills/skills/engineering/research/SKILL.md` | **AMPLIAR** | A6 skill frontmatter and destination test with pin + permissions; existing `p0x/skills/auditar-p0x/SKILL.md` has side effects. |
| OPA declarative policy, MCP registry/gateway patterns | **REUTILIZAR** | F1/F5 policy-test cases against current allowlist before adding another daemon. AI Act compliance: NO_DATA without legal review. |
| Label Studio `label_studio/` | **REUTILIZAR** | E3/B4 optional LOCAL annotation of redacted traces with no second score ledger. |
| Mesa simulation / game lockstep | **AMPLIAR** | D5/E3 test pure input replay first, no simulator unless difference measured. |
| Nix pinned environments | **REUTILIZAR** | E3/F6 source/build hashes first; an environment pin does not prove LLM output identity. |
| celld SQLite/LTX + Litestream recovery | **REUTILIZAR** | E1/F6 node outage/recovery simulation before another distributed state service. |
| VictoriaMetrics/Grafana; Headscale/NetBird/ZeroTier | **NO_DATA** | F5/E1: no verified gap against existing Nexo metrics/mesh; measure running services and risk before considering imports. |
| x402/NEAR/BOINC economy | **NO_DATA** | Missing signed custody, payments, fraud and consent rules; no new canonical mission. |
| OpenVINO, KTransformers, external CPU tokens/s, Nix 90% reproducibility claim | **NO_DATA** | No same-machine pinned measurements or hardware/build compatibility E2E. |
| Landauer => append-only saves physical energy | **DESCARTAR** inference | Append-only is audit doctrine; joules require controlled wattmeter experiment. |

## Provenance ledger (reviewed external GitHub branch heads, 2026-11-10)

Repository licence refers to repo metadata, NOT permission to redistribute included data/assets. Refer to commit-pinned paths in the body. No third-party code copied.

| Repo | Commit | Licence |
| --- | --- | --- |
| `modelcontextprotocol/modelcontextprotocol` | `632a0c9a65c9b4fbc889d8aface5c9cf5edef3b7` | NOASSERTION |
| `lark-parser/lark` | `9a4fb9c7458e8155636773a3cded0016d52516da` | MIT |
| `ggml-org/llama.cpp` | `3b4d6ab3f79651935fba1dd93732f29022a7f5f5` | MIT |
| `Gentleman-Programming/engram` | `b53422f45c57c1003cc9c063c5a4e1fe1c694f27` | MIT |
| `andyz245/LanguageAgentTreeSearch` | `853d81614607dd27433faf17c7b0a7d660f95d22` | MIT |
| `benbjohnson/litestream` | `af28505f39a8e1afe9291febbe11e9926bd230aa` | Apache-2.0 |
| `microsoft/graphrag` | `34b2b67ae4601ad0b47bcd179fbe3f2a23aa0857` | MIT |
| `reasoning-machines/pal` | `f81ca2a9777f002f98a6b4d0f10b61bd5c8feb02` | Apache-2.0 |
| `microsoft/ToRA` | `213c1c995038c73fab10343814df7a42f990f026` | MIT |
| `openai/prm800k` | `7ecc794703b2877f63226f2477a49b34f9b25163` | MIT, archived |
| `hendrycks/math` | `985bdc1696e88e8643f081a0ff4719da39f2ae2a` | MIT |
| `princeton-nlp/tree-of-thought-llm` | `8050e67d0e3a0fddc424d7fa5801538722a4c4cc` | MIT |
| `spcl/graph-of-thoughts` | `3d9d9dbd8937d47a4441f681b8b40e3c5b054f16` | NOASSERTION |
| `microsoft/rStar` | `ecbfb943e202b4ed017d2d35f2029917b27db4cd` | MIT |
| `EleutherAI/lm-evaluation-harness` | `d6de81643928d653435c431bae19945d41d32520` | MIT |
| `xerj-org/xerj` | `50e4ffded5518b1822cfac5450fa34d3829ab8ab` | Apache-2.0 |
| `denoland/celld` | `8702f6d186c77698dbfb30cf29e3b1922a88f008` | Apache-2.0 |
| `mvschwarz/openrig` | `24dd3eb888c6b59b3dc1861d9e05ad40e43eb79a` | Apache-2.0 |
| `mattpocock/skills` | `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` | MIT |
| `maazbin/jobpilot` | `ad063db97e168041c8d999adfb7b1839dcf73d1d` | MIT |
| `jakejack13/gachapy` | `e3257a5ab8657abd1d73eacd76a7c5ff52b204e9` | MIT |
| `rexor12/gacha.py` | `946f31adb40f3184ce4ddd447439bbd5421d3506` | MIT |
| `kidagine/Darklings-FightingGame` | `96a60d34cedd4b6898c026d5a0adfc9e3040f20a` | NO_DATA (licence not verified) |
| `RPG-Paper-Maker/Documentation` | `78b22ee6ab511dc611a09993e92a8cf2720fec98` | NO_DATA (licence not verified) |

**Identity corrections:** `tasksource/PRM800K`, `litestream/litestream`, `pal-model/pal`, `AlternativeQL/Reasoning-LLMs-Tree-of-Thoughts`, and `chuangxinyu/Reasoning-Tree` did not resolve at inspection. Use original `openai/prm800k`, `benbjohnson/litestream`, and `reasoning-machines/pal`. The official LATS readme was found at `andyz245/LanguageAgentTreeSearch`; no unsupported "percentage of hallucinations" follows from such a hand-picked list.

**Vendor figures not measured locally:** claimed ToRA success rates, XERJ 160-question comparison, CPU speed and general reproducible-build percentages: **NO_DATA: no identical fixture and local two-run evidence**.

## B6 dependency proposal; no historical distance invented

Stable study identity is NOT a GitHub issue number. Proposed edges: F1/F5 -> A6 -> B3 for tool trust; existing Acho validator -> optional text grammar -> C8 -> B8 (depends on A9); E3 receipts -> manifest -> E7; Nexo source index -> C5 cited edges -> B6 impact. A conceptual position such as `778.5` may be *suggested after* mission `782` exists, without changing IDs or build order. Unknown historical edges = `NO_DATA: missing verified dependency/build receipt`, not zero impact.

**Next slice:** offline MCP deny matrix on existing harness; only then an implementation PR in the owning repo. This study PR contains documentation, not a new service or policy. Screen-reader/radio E2E: NO_DATA, no paired test. `study` has no own remote CI; AGENTS requests `python3 ../lab/bin/verify_llms_tree.py --root .` ×2, **NO_DATA: no Lab checkout available here**.

**Mesa:** [buzon#53](https://github.com/piskyRpapalo/buzon/issues/53) · **receipt:** [buzon#19](https://github.com/piskyRpapalo/buzon/issues/19). No sign-off by Codex, no main write or merge.
