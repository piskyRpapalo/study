# ROSETTA_ENMIENDA_CREACION · proposal · REQUIERE_FIRMA

Measured 2026-10-24 by the Mesa (preceptor-orquestador-github) against web main 054ee185, app main 1e5ac35, and the receipts of buzon issue 19. This proposal appends; it never rewrites. Coinage still lives in THE LEXICON (docs/lexicon.md, preceptoros-web §C1); rows here fix only the direction of reading and the measured state. Statuses follow 12-schema.md.

## 1 · Corrections — rows of the 2026-10-23 fold, now STALE

| The fold said | Read it now | Status | History anchor |
|---|---|---|---|
| army_tope 60 | army_tope 30 | MEASURED | FIRMO Armi 30 (web#278, 95996e1): valores.js army_tope 30; no judge fixes 60; juez T3 re-pinned (web#281, e91ea5e2) |

## 2 · The creation lane (F0→F3) — terms the external reader will meet in GitHub

The Sovereign commissioned the real-viability run of the creation MVP (F0→F3; brief in web#277; cards E1–E8; executor: the preceptor Codex, window name Luna). Measured state at this amendment:

| The folio says | Read it as | Status | History anchor |
|---|---|---|---|
| el paquete de creacion | the creation package (Ed25519 over the manifest; separate hashes for drawing and WAV) | REALIZED | web#282 (d149eb8, seal abix) · public/game/creation_package.js · docs/creation-package.md · tests/creation_contract.test.mjs |
| el dibujo ciego (retroalimentacion de 4 canales) | blind drawing / creation feedback | REALIZED | web#283 (439188c) · public/game/creation_feedback.js · tests/creation_feedback.test.mjs |
| importar/guardar la creacion | creation import (verify + store) | REALIZED; sabotage debt paid | PreceptorOS#92 (6f55a9d) · PreceptorOS#94 (1e5ac35) · creacion_import.py · test_creacion_import.py (visible in the bin/pruebas runner) |
| el interruptor del sabotaje | the sabotage switch: CREATION_IMPORT_SABOTAGE=1 skips only the hash/size compare; normal rejection intact | MEASURED | creacion_import.py (+2/−1, PreceptorOS#94); the red it fixed was measured in PreceptorOS#92 · comment 6372704245 |
| el censo v1.5 | the census: strict equality of public/game/*.js against MODULOS + FUERA_DE_LA_PUERTA (new tuple CREACION, pure until its page exists) | MEASURED | web#284 (c39b1d9, atlas/test_atlas.py, TheGameV15): the CI red of E1+E2 was this census |
| FIRMO general | delegated merge: the Mesa merges a card under the Sovereign's standing signature (in force since 2026-10-23 by the Sovereign's chat order); receipts in buzon issue 19 | SIGNED (chat order, 2026-10-23) | measured by the FIRMO triple E1/E2/E5 (buzon#19 · 6372162570) and PreceptorOS#93/#94; rule adopted: the FIRMO waits for green CI |
| el sello del worker | the web seal series: abiw (#280) → abix (E1) → abiy (#284) → abiz (E4); canonical long form preceptoros-2026-17-<letters>; the letter is chosen by the Mesa, never by a working agent; sellar.py auto-continues the series again | MEASURED | config/sw-huella.txt at b79d04cb (preceptoros-2026-17-abiw) · bin/sellar.py siguiente() · huella abiy 24654391cfe91134 at the fixed point |

## 3 · Reading rules the lane taught (measured lessons)

- The census is strict equality: a new module in public/game/ registers in the same PR that lands it (E4 must MOVE the CREACION tuple to the loading list when the create page loads the modules).
- The counters are self-referential (peso_sitio includes counters.json itself): two passes to the fixed point; seal always LAST.
- The contents API does not preserve the executable bit: executable files are touched only with git from the rack (measured: PreceptorOS#93 — CI dead in under 10 s = Permission denied, not a test failure).
- A local judge chain must include ALL the gate's judges, incl. atlas/test_atlas.py (188 tests): the E1+E2 CI red lived three merges because no local chain ran it.

## Provenance

Measured by the Mesa from direct GitHub reads (commits, check runs, receipts of buzon issue 19) on 2026-10-24. The FIRMO on the PR that merges this proposal signs the rows as triaged reading direction; each coinage still travels its own THE LEXICON PR.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA