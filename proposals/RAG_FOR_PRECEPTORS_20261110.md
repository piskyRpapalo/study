# The repos as RAG for preceptors (ES: las repos como RAG para los preceptores) · 2026-11-10

**ID:** STUDY-RAG-PRECEPTORS-20261110. **State:** PROPOSAL, research-only, docs-only. **Agent:** preceptor-orquestador-github (VIGIA) · **Model:** GLM (Vibe) · **Run:** NO_DATA. **Commission:** evaluate the possibility of improving the repos as RAG (retrieval-augmented ground) for the preceptors. Propose-only.

## Verdict

**Viable — and largely already built in-house.** The ecosystem already runs a three-layer, native, fail-closed RAG; what is missing are four declared gaps, each a native slice. No external RAG framework is needed (DESCARTAR with cause, below). *(ES: viable y ya medio construido en casa; faltan cuatro huecos, cada uno una rebanada nativa.)*

## Ground truth measured (2026-11-10, read not assumed)

- **study llms.txt** (494 B, sha256 in ai-index.json): the declared-depth law — INDEX, BUDGET 16,384, DEPTH 0-4, REREAD, SCRUB, AUTHORITY.
- **study ai-index.json**: schema preceptoros.ai-index/1, generated 2026-11-02 by lab/bin/gen_ai_index.py (stdlib, deterministic); 18 entries, each with path, depth, words, bytes, sha256, one-liner; plus **DECOYS** (two non-existent paths = cheater signals for an AI that cites them) and **CANARIES** (depth-99 alerts). A measured, hashed, anti-hallucination index.
- **web llms.txt**: the five declared depths + **Jump index v2, a two-pass retrieval protocol**: pass 1 = the stable index (~300 tokens), pass 2 = ONE package by name (<=300 tokens); two passes total, more = separate design. Plus the local MCP server (8 tools, no network) and /mcp-manifest.json for visiting AIs.
- **hexelion-nexo vector_index/**: schema preceptoros.rag-object/1 — a bounded local vector index: 768-dim, sqlite-vec optional, embeddings supplied by the caller via an explicit loopback endpoint, SHA-256 verified at build AND at search, stale source = the whole result refused, model digest enforced, typed objects (MANDATO · PIEZA · SENSOR · MEDIDA · RECIBO) with typed relations (about, supports, resolves, invalidates...), fail-closed NO_DATA with cause. Its own README declares the gaps: pulpo wiring, corpus ingestion, retrieval-quality benchmarks, real-model end-to-end — all NO_DATA.
- **Engram** (MIT, adopted by decree): the persistent-memory pattern already running in the rack (SQLite + FTS5); the generation fence (study#104 jewel, A5/B1) protects exactly that kind of live SQLite.
- **The mesas**: both mission catalogs + the 2026-11-10 harvest marks (merged today); the append-only ledger channels (buzon#53 measured at 966 comments today).
- **lab benchmarks**: embedding and reading benchmarks measured 2026-10-11 (bench_20261011, raw JSON sha256 26e61fb7...).

## The three layers that already exist (nothing imported)

1. **Declared-depth law** — deterministic retrieval by declaration: budgets, one-pass loading, NO_DATA beyond depth, decoys and canaries as tripwires. Zero-cost RAG for every AI that lands. The decoy/canary pattern is a house invention worth amplifying.
2. **Jump index two-pass protocol** (web) — a measured retrieval contract for ANY reader (visitor AIs included): read the index once, fetch ONE package by name once; the prefix is stable and cacheable.
3. **Hash-verified vector index** (nexo) — real embeddings, fail-closed, staleness refuses the whole result. The citation law (byte-exact or NO_DATA) is already the retrieval law.

## The four gaps (each declared NO_DATA with its cause; each a native slice)

- **G1 freshness.** ai-index.json was generated 2026-11-02: the three proposals merged today are NOT in it. Cause: no regeneration step after FIRMO. Slice: regenerate the index with each FIRMO that moves main (the generator exists, stdlib, deterministic) — the LIVE==main analog: **index==main**. Class: AMPLIAR (E3). Cheapest, converts drift today.
- **G2 ingestion.** The vector index has no corpus pipeline. Cause: its own README (pulpo wiring, corpus ingestion NO_DATA). Slice: **flow B of the harvest** (the live index of receipts + hilo + actas) IS that ingestion; the rag-object types (RECIBO, MEDIDA, PIEZA) already match the ledger content. Class: AMPLIAR (B6/B1/C5).
- **G3 quality.** No retrieval-quality benchmark exists. Cause: NO_DATA (nexo README); the 2026-10-11 lab benchmarks measured embedding/reading, not house-corpus retrieval. Slice: **20 canonical questions** with known answers (from the mission map, the marks, the receipts) — every layer must return the exact doc + sha256; deterministic across 2 runs; decoys included (a retrieval that cites a decoy = RED). Class: AMPLIAR (E3). Makes quality measurable BEFORE building more.
- **G4 end-to-end.** No real-model E2E run. Cause: not run. Slice: one measured build+search cycle with the local loopback embedding endpoint, model digest recorded, receipt <1,024 B. Class: AMPLIAR (E1/F6/A2).

## Synergy with the 2026-11-10 harvest (no duplication)

- The jump-index two-pass protocol IS a training-pair format (question -> package): **the retrieval corpus and the A2/A9 pair corpus are ONE corpus.** Feeding the retriever and feeding the LoRA is the same measured stream (harvest marks row 8).
- The Engram fence (row 4) and the rag-object hash-verification are the same law: never serve bytes that changed under you.
- xerj retrieval math (row 22) feeds flow B = G2; Litestream WAL drills (row 6) are the index's restore drill; GraphRAG's dependency graph (row 7) is half-built already — the rag-object relations (about, supports, resolves, invalidates) are that graph.

## Not recommended (DESCARTAR / NO_DATA with cause)

- **External RAG frameworks** (orchestrator frameworks with their own stores and agents): DESCARTAR, cause: native-first law — every component exists measured in-house, and the house versions are fail-closed with receipts.
- **Vector search on the edge browser** before G4: NO_DATA, cause: edge cost unmeasured (E3/F6).
- **Ingesting private channels into any public index**: prohibited — the SCRUB boundary is the fence; the private corpus stays in the private side (private mesa, private channels), the public mesas serve the public side.

## The three most promising slices (ranked)

1. **Index freshness rule (G1)** — regenerate ai-index.json with every FIRMO that moves main. Acceptance: regenerated index committed in the same session; decoys and canaries intact; deterministic.
2. **The 20-question retrieval benchmark (G3)** — canon, marks and receipts supply the questions; exact doc+sha or NO_DATA with cause; decoys must never be returned. Acceptance: 2 deterministic runs, receipt per run.
3. **Flow B ingestion into the existing vector index (G2)** — receipts+hilo+actas as rag-objects, fence-protected, feeding the WBR (F-01) and the judge citation (C5). Acceptance: one measured offline build+search cycle.

## Mesa

Receipt: buzon#19. Candidates registered: buzon#53. No sign-off, no merge, no new mission, no second catalogue; positions per the harvest marks. The Sovereign's FIRMO decides.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA