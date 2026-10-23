# ROSETTA · COSECHA 6 · IDEAS OCT vs METAL · 2026-10-23

PROPUESTA · propose-only · REQUIERE_FIRMO. La biblioteca de ideas de octubre (los Papers) fue releída íntegra por la Mesa y medida contra el metal vivo hoy (tanda 5 de lectura del rack). Propósito del study declarado por el Soberano: el aula; la rosetta: el idioma — rename + fluidez de IA + vocabulario de preceptores, verificable por una IA externa sin acceso al rack.

## La relectura en una tabla

| término (oficial EN) | lo que dice la idea oct | el metal dice hoy (2026-10-23) | sello |
|---|---|---|---|
| declared-depth reading / context-lock (L0-L4) | [MEJORA URGENTE 2026-10-20]: guardrail en perfil + llms.txt + AGENTS.md | YA ES LEY EN OBRA: perfil README L173-191 con las cinco profundidades · llms.txt del study con DEPTH y REREAD · AGENTS.md web L3-22 · la ley vive en 08-ai-fluency.md | LIVE (la propuesta aterrizó) |
| attention-selector (lab) | "ya tienes attention_selector/" | 8 piezas: __init__ · cli · core · evaluation · local_model · package · service · store | LIVE |
| study-spec | plantilla de 5 variables | study_spec.json = 461 B en lab | LIVE |
| the Crucible (el Crisol) | 13 sondas contra las propias vallas | benchmarks/redteam-20261020/: recibos crucible de 2 modelos (1.5b y 30b) + lora_test + carbon_3poles + README | LIVE (ejecutado en lab) |
| fence-probe (sonda de valla) | coinaje con colisión medida | RENAME-SUGGESTED en 10-collisions.md L131, con enlace a lab | REGISTRADO |
| atlas.riesgo/1 (hoja de riesgo) | validador puro <1.024 B | 10-collisions.md L133: ausente de study y lab; 13-rosetta.md L88 lo declara MEDIDO en APP (atlas_riesgo.py + test_atlas_riesgo.py) | DECLARADO · localización física pendiente |
| quaternary-verdict | clasificador_cuaternario.py MEASURED | 13-rosetta.md L86 lo declara (APP, 1.403 B); NO_DATA en la raíz del APP — localización pendiente (mini-tanda 6) | DECLARADO · pendiente localizar |
| crab-account (bridge · wandering) | 2 fases; el cambio exige FIRMO | 13-rosetta.md L87: cuenta_cangrejo.py (APP, 10.221 B) + aiact_art14_game_policy.json | DECLARADO · pendiente localizar |
| VIAS sociales | "solo falta añadir LinkedIn/HF/Bluesky/Mastodon" | YA DOCUMENTADO: VIAS.md L51-54 con las 4 rutas (login de Bluesky: NO_DATA con causa) · adaptador construido: NO_DATA | DOC LIVE · adaptador NO_DATA |
| índice de benchmarks | deriva: 23 carpetas sin README | README.md vive en benchmarks/ (24 entradas) | DERIVA CERRADA |
| ENERGY_BUDGET | traducir al inglés al FIRMO | sigue en español; fórmula J_net/token en L7; sigue REQUIERE_FIRMA | DERIVA ABIERTA |
| wave-ceiling | "10 MEDIDO · 30 NO_DATA (RC-14)" | valores.js L48: tropas_max: 10 — confirmado. Tres topes conviven, cada uno en su ámbito: tropas_max 10 (L48) · army_tope 60 (L46) · escuadrón 32 (L32) | MEDIDO |
| desafina (detuning) | provenance hunt O3 | battle_replay.js L123: desafina es parámetro de estado por daño (0-0.85); 0 coincidencias de detune/cents en audio — la desafinación vive como estado, aún no como tono | MEDIDO (estado) · audio NO_DATA |
| Say Hi (radio, fase 1) | "el botón existe desde el tutorial" | aiact-art50-state-radio.js L83: botón 'radio-say-hi' con texto "Say Hi" | LIVE |
| MCP (client · server · estático) | pregunta de auditoría ideas20oct | mcp-manifest.json se declara a sí mismo: inventario estático de deep-links, NO un manifiesto MCP; el servidor de protocolo vive en PreceptorOS#64; generado mistral/g1 (PR #100), servido (PR #184); FIRMO del manifiesto: NO_DATA con causa | STATIC_MANIFEST honesto |
| zombi / sub-1kb-invariance | prueba vivo/dormido <1.024 B | "zombi" vive en deploy_building.js; 0 coincidencias de 1024 en bin/pruebas | PARCIAL · prueba NO_DATA con causa |
| preceptor-cell (2 clics) | PROPUESTA | preceptor_cell.py: NO_DATA (sigue PROPUESTA); piezas base LIVE: empaquetado/ (construir_pc.sh · install.sh · install.ps1 · lanzador.py) · empieza_aqui.py 13.915 B | PROPUESTA confirmada |
| ORQUESTADOR_BUILDINGS | ideas21oct: "VERIFICADO en data/" | NO_DATA en APP/data — la cita es STALE o la pieza se movió | STALE |
| aduana: receptor de alerta | tubería firmada humano→web→rack | solo GET /health + POST /aduana/cedulas (src/index.js L61-63); el resto 404 ruta_ausente; cliente: public/assets/enviar-ar.js | CLIENTE LIVE · RECEPTOR NO_DATA |

## Censo APP raíz "ya tienes" (medido hoy)

LIVE: canales.py 14.566 · decisor.py 11.848 · generar_leitmotivs.py 5.600 · frontera.py 6.335 · fuga.py 40.282 · soberano.py 5.142 · estado.py 7.039 · corredor.py 2.822 · empieza_aqui.py 13.915 · atlas_runner.py 12.857 · cara.py 53.156 · exportar_contexto.py 13.314 · aiact_art14_node_decide.py 4.058 B.
NO_DATA en raíz (pendiente mini-tanda 6): clasificador_cuaternario.py · canal_event.py · ficha_cartucho.py.

## Lo que esta cosecha le dice al preceptor que llega

1. La lectura a profundidad declarada YA es ley en los gates: no hay que construirla, hay que obedecerla.
2. El red-team del ecosistema ya corrió una vez en el lab (el Crisol, 2 modelos con recibo): las sondas de valla tienen evidencia.
3. La última milla social está DOCUMENTADA en VIAS.md; lo que falta es el adaptador medido, no el diseño.
4. Las piezas citadas del APP raíz viven y pesan lo que pesan; tres citas de 13-rosetta.md esperan localización física antes de sellarse MEASURED (mini-tanda 6).
5. R-D3b (casa-* → house-*): 0 coincidencias en study main — el alcance del renombre no vive en study; es carril del brazo.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
