# ROSETTA · PROTOCOLO DE RAMAS Y SESIONES · 2026-10-23

PROPUESTA · propose-only · REQUIERE_FIRMA. Encargo del Soberano (2026-10-23): estructurar para que no se creen ramas innecesarias en el futuro (problema recurrente), con la Rosetta como ayuda. Nada de esto es ley hasta el FIRMO.

## 1 · El problema, medido

- Ramas vivas tras su fusión: estado duplicado que una IA externa puede leer como verdad alternativa. La poda siempre llegó tarde y a mano.
- Clones paralelos en el rack con cadenas sin fusionar (medido 2026-10-21/22: una cadena de piezas viva en un solo arbol local, con world_creator +189 lineas sobre main) y remotes rotos apuntando a rutas inexistentes.
- Causa raiz: las sesiones de agentes usan ramas y clones como cuaderno de borrador. El cuaderno correcto ya existe: los recibos del buzon (bitacora) y los folds del study (memoria estable).

## 2 · Ley de la rama unica (propuesta)

- R1. Un mandato = una rama, desde main, nombre: mesa/<slug>-<AAAAMMDD>.
- R2. La rama existe solo mientras su PR esta abierta. Tras FIRMO + vara x2 verde: fusion y poda en la misma sesion.
- R3. Presupuesto: maximo 2 ramas mesa/* vivas a la vez. La tercera espera turno; no se abre.
- R4. Prohibidas las ramas de archivo/backup/wip: el archivo es un merge (o un PR cerrado con su recibo), no una rama.
- R5. Poda verificada: la sesion termina listando ramas; una rama que no este en un PR abierto se declara HUERFANA en el recibo.

## 3 · Ley del clon unico (propuesta, carril rack)

- Un solo clon de trabajo por repo en el rack. Los demas clones pasan a Cuarentena con remote y fecha declarados.
- Ninguna sesion construye fuera del clon de trabajo. Si el metal parece estar en otro arbol, se DECLARA, no se duplica.

## 4 · La puerta de la Rosetta (para el proximo preceptor)

- P1. Entrada unica al study: llms.txt (profundidad L0-L4 + REREAD ya son ley).
- P2. Orden de arranque: llms.txt -> ultimo fold del study -> ultimos recibos del buzon -> inventario del mandato. Sin rama nueva hasta tener mandato.
- P3. Estado de sesion: nada de estado en ramas. La bitacora es buzon#19 (<1.024 B por recibo, UTF-8); la memoria estable son los folds.
- P4. Regla anti-fantasma (ya propuesta en el carril web, se adopta como vocabulario comun): lo construido sin enlazar en la ruta servida y sin recibo = HUERFANO; no suma avance.
- P5. Higiene pegable al cierre de sesion: git branch --merged main y git branch --no-merged main; todo lo --merged se poda salvo main.

## 5 · Erratas que trae esta ronda (MEDIDO 2026-10-23, mini-tanda 6b)

- Los 6 archivos declarados por 13-rosetta.md L86-88 como MEASURED en APP (clasificador_cuaternario.py, cuenta_cangrejo.py, atlas_riesgo.py, test_atlas_riesgo.py, canal_event.py, ficha_cartucho.py): find a profundidad 8 en el arbol APP = 0 coincidencias. Sello: ABSENT en ese arbol. Causa probable: viven en otro arbol del rack. Propuesta: esas celdas pasan de localizacion pendiente a ABSENT-con-causa; no se edita 13-rosetta.md sin FIRMO aparte.
- enviar-ar.js: leido desde main desde fuera. No es el cliente logico: es la locale arabe del flujo de envio al estante (window.ENVT, 8 cadenas). Hallazgo: los textos declaran el contrato del flujo — firma local + clave publica + cola de revision humana, nada se publica solo. El cliente logico vive en otra pieza (medir en la proxima tanda). El grep en espanol dio 0 porque los terminos viajan en arabe.

## 6 · Verificacion propuesta (EXPECT)

- git branch --merged main (sin contar main) = vacio tras cada sesion.
- Ramas vivas != main <= 2 (presupuesto R3).
- Cada PR cerrado tiene su recibo en buzon#19.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
