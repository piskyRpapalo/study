# VERIFICACIÓN FORENSE · MANIFIESTO CORREGIDO · 2026-11-10

> Manifiesto contrastado con el metal: 30 afirmaciones, cada cifra medida.
> Método: GitHub HEAD por API (babel, study, lab, app, companion) + rack `soberano`
> (clones frescos de lab/babel/study, `ollama list/ps`). Lo no verificable viaja como
> `NO_DATA` con causa. Recibo: buzon#19 ·6769399751 (954 B).

## §1 · Archivos específicos (8/10 verificados, 2 corregidos)

| Afirmación | Veredicto | Medida |
|---|---|---|
| `aiact_art14_node_decide.py` existe y declara HITL | ✓ | 4,056 chars; `atlas.accion/1`; `firma: null`; "el nodo propone; firmar es de la persona (AI Act art. 14)" |
| `aiact_art14_game_policy.json` prohibe las 4 prácticas | ✓ (en español) | "acreditar por tiempo pasivo", "perfil psicologico por telemetria", "gacha casino: reroll pagado o urgencia falsa", "huella del aparato como identidad" |
| `clasificador_cuaternario.py` con 4 verdictos | ✓ (etiquetas SI/NO/CUANDO) | `SI/NO/CUANDO/NO_DATA`, NO_DATA con causa, techo 1,024 B |
| "SCRUB en `frontera.py`" | ✗ CORREGIDO | `frontera.py` es la jaula Wasmtime (fuel, 64 MiB); cero ocurrencias de "SCRUB". La ley vive en `babel/registry/governance.md`; el motor es `guardrails.py` (`redactar_salida`, fail-closed, "clase y cantidad, jamás el texto") |
| `study/04-measurement.md`: "red before green" + "gates n=2" | ✓ | Ambas frases presentes en HEAD |
| `study/13-adversarial.md` existe | ✗ CORREGIDO | No existe. En study: `13-objectives.md` y `13-rosetta.md` |
| `babel/registry/implementation.md` §K: `preceptoros.acho/1` | ✓ | "versioned frame schema" |
| `babel/registry/game.md` §E: nombres prohibidos | ✓ | Los 8: oracle · notary · depin · coin · clearing · magic · token-as-a-name · cryptocurrency |
| `babel/registry/coins-2026-11-03.md`: oversight clause | ✓ | Los 4 elementos (passive/profiling/rerolls/fingerprint) |
| `babel/registry/governance.md`: ley SCRUB | ✓ | "Removing private names from public artifacts; figures and paths stay, names go" |

## §2 · Modelos residentes (2/4, 2 NO_DATA)

- ✓ Receipts del Crucible EXACTOS: `lab/benchmarks/redteam-20261020/crucible_qwen3-coder_30b_20261020_202431.json` = **21,621 B** y `crucible_qwen2.5_1.5b-instruct-q4_K_M_20261020_202856.json` = **15,708 B**. Ruta corregida: viven en el repo lab, NO en `~/.preceptoros/crucible/` (directorio vacío).
- ✗ `ollama ps` VACÍO: ningún modelo cargado en memoria al medir.
- ✓ Instalados en `soberano`: `qwen3:1.7b`, `hf.co/ggml-org/embeddinggemma-2-GGUF:Q8_0`, `qwen2.5:1.5b-instruct-q4_K_M`.
- ✗ `qwen3-coder:30b` NO instalado en el rack (ausente de `ollama list`).

## §3 · Benchmarks precedentes (5/6 con matiz, 1 NO_DATA)

- ◐ `redteam-20261020`: directorio existe; su README es NO_DATA puro ("independent review blocked"); las cifras "13 probes, 5 fences" NO aparecen. Receipt redteam 28,273 B cuadra con babel §I.
- ✓ `h9-readability-20261016` (fecha corregida, no 20261021): negativos publicados de verdad: 0/8 exact reads, diccionario −25 pp, estímulo denso −25 pp.
- ✓ `attention-selector-20261017`: 24 tests · 0 fallos · 2 corridas ("two independent runs"; la frase literal "gates n=2" vive como ley en governance.md).
- ✓ LoRAtelier: 4 receipts en `lab/benchmarks/redteam-20261020/`: `qwen3.5:4b` ×2 (19,150 + 20,697 B), `qwen3-coder:30b` (28,625 B), `qwen2.5:1.5b` (24,674 B).
- ◐ `bench-fluency` mecánico: vive en `lab/benchmarks/bench-fluency/` (M1–M4; fuente rack `p0x/estudios/bench-fluency/MECANICO.md`). El contrato `p0x.bench_fluency.mecanico.medicion/1` no aparece indexado.
- ✗ `rack_instantanea.py` existe en `p0x/hexelion/laboratorio/` (no en app); el servicio `rack_instantanea.service` NO existe (not-found/inactive).

## §5 · Colaboradores (1/2)

- ✓ Aimilios94: PR #3 de `preceptoros-companion` MERGED 2026-11-03T20:21:52Z, título "HITL". Confirmado por API.
- NO_DATA Suraindran Kamalakanan: falta consentimiento explícito para atribución pública.

## §6 · Afirmações técnicas (1/3 limpias)

- ✗ "Every receipt is <1,024 B": 20 de 48 JSON en `lab/benchmarks` superan 1,024 B. Matiz declarado: el techo 1,024 B gobierna el carril de recibos de buzon, no la evidencia de benchmarks.
- ✗ "Package <16,384 B": 1 violación, `study/13-rosetta.md` = 21,860 B (lab: 0/98; babel: 0).
- ✓ "gates n=2": ley en `babel/registry/governance.md` + práctica en 04-measurement.md, attention-selector y h9.

## §4 · DFA: NO_DATA (pospuesto por diseño)

El texto oficial COM(2026) no está publicado. Las cifras externas (97%, €7.9B,
4,300+ respuestas, agenda 11-nov-2026, artículos del borrador filtrado) se
verifican cuando exista fuente oficial. Igual criterio para el consentimiento
de §5.

## Correcciones obligatorias aplicadas al manifiesto

1. La ley SCRUB se atribuye a `babel/registry/governance.md` + `guardrails.py`, no a `frontera.py`.
2. `study/13-adversarial.md` eliminado (no existe; los negativos adversariales publicados viven en `h9-readability-20261016` y `redteam-20261020`).
3. Ruta de receipts corregida: `lab/benchmarks/redteam-20261020/`, no `~/.preceptoros/`.
4. Etiquetas del clasificador declaradas en español: SI/NO/CUANDO/NO_DATA.
5. Ámbito del techo 1,024 B declarado: recibos de buzon, no evidencia de benchmarks.
6. Violación medida declarada: `study/13-rosetta.md` = 21,860 B > 16,384 B.

## Licencia

CC BY-SA 4.0, [LICENSE-PROSE](LICENSE-PROSE).
