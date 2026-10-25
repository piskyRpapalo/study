# ORCHESTRATOR BRIEF ideas25oct — CLARIFYING OBJECTIVES A1-A14 (verbatim relay)

Status: proposals only. Nothing decreed. This file is a verbatim relay by the Mesa of the
Sovereign's ORCHESTRATOR BRIEF ideas25oct (2026-10-25), objectives section, so the orchestrator
(Luna/codex) can draft the A1-A14 proposal documents without inventing scope. Each proposal stays
in the proposals lane with its receipt; no target repository is edited; nothing is signed.

============================================================
OBJETIVOS ACLARATIVOS
============================================================

A1 · Tutorial en dos partes.
Parte 1: captura un edificio en la niebla y lo tunea. Todo en el dispositivo.
Elección de lado: Atlantis o Zombie.
Parte 2: dentro del nodo elegido. La controla el propietario del nodo.
Acción: diagrama de estados y lista de pantallas. Marca cada pantalla con su equivalente en la app.

A2 · Partida efímera.
Datos de partida: en el dispositivo.
Identidad de firma: efímera.
Son conceptos separados. Escríbelo así en todos los documentos.

A3 · Guardado.
Vigente: la partida se descarga como fichero JSON. Botones "Guardar" y "Cargar".
Pendiente de firma: almacenamiento de paquetes de modelo en OPFS o Cache API, y un guardado automático en IndexedDB.
Hasta la firma, no escribas que el juego guarda en el navegador.

A4 · Paquetes de modelo.
Descarga explícita del usuario. Sha256 y firma Ed25519 del manifiesto. Fuente: release de PreceptorOS, nunca un CDN de terceros.
Aviso de espacio con navigator.storage.estimate(). Umbral propuesto: 80 %. Texto honesto: el navegador puede borrar datos.

A5 · Preceptor del chat.
Mitad inferior de la pantalla en la web. Respuestas semi-deterministas.
Conversación en memoria por defecto. Guardado solo si el usuario lo activa.
Funciona offline solo si el service worker cachea el modelo. Verificarlo con test.

A6 · Gacha como pre-test visual.
Sirve para emparejar visuales y medir cuál funciona. Nunca da ventaja de combate. Nunca se vende. Etiqueta de prueba visible.

A7 · Incentivos del propietario.
Prestar ondas: equipo paralelo, con duración, pérdida y revocación declaradas.
Porcentaje sobre lo que gana el visitante: calibrar. Propón un techo y una forma de declararlo. No fijes un número.
Recursos por edificio para el ejército: con techo por nodo.

A8 · Rutas de comercio.
Visibles en el mapa. Asaltables. Reglas pendientes: coste de asalto, recuperación, pérdida, sin reloj real, sin probabilidad oculta.

A9 · Misma marca en web y app.
La app replica el estilo completo de la web: bubble language y rosetta como sistema de diseño, con study como referencia. Hoy la app tiene 0 ficheros con rosetta.
Cada cambio de la web se propone con su equivalente en la app.

A10 · Colaboración del usuario.
Un usuario participa sin instalar nada: partidas, gacha, formularios, sugerencias.
La firma de entrada a un nodo es prueba de interacción.
El nodo expone en sus edificios las formas de colaboración. El usuario elige cuáles usar.
Feedback voluntario, local. Sale solo un recibo con hash y categoría. No se guarda texto libre fuera del dispositivo.
Telemetría del gacha: mínima, declarada, sin perfiles de comportamiento.

A11 · Usuario con nodo conectado.
Descarga la app y conecta su nodo: pasa a colaborador directo.
Desde otro dispositivo entra como visitante al terreno de su nodo.
Pendiente: cómo se alcanza el nodo remoto. Opciones: relé sin almacenamiento, punto a punto cifrado, o nodo siempre encendido del Soberano. Propón medidas para comparar.

A12 · Red teaming con usuarios.
Opt-in y local. Solo salen recibos con hash, categoría y resultado. Los prompts no salen.
Solo sobre pesos locales.

A13 · Piezas de software extra.
Vídeo, preceptoros-coder como una pantalla más, otras piezas. Cada una es un paquete firmado, fuera del bundle base. Presupuesto de tamaño por pieza.

A14 · Enlaces a redes sociales del nodo.
Válido como enlace. Sin carga al abrir la página. Sin seguimiento.

============================================================
GATES
============================================================
Cada cuadro y cada recibo: menos de 1.024 bytes UTF-8.
Accesibilidad por pantalla: teclado, 44 px, texto alternativo, sin solapes, reduced motion.
Cero peticiones externas al cargar la página.
Palabras vetadas fuera del código e interfaz: token, moneda, oraculo, notario, depin, clearing, magia.
Cero IP privadas, rutas privadas o prompts crudos en los repos.

============================================================
PARADAS
============================================================
Detente si un paso requiere: credenciales, merge, deploy, firma, escritura en PARA_LA_MESA.md,
prompt crudo, IP, ruta privada, o un CDN de terceros.

============================================================
NO VERIFICADO / NO_DATA
============================================================
Qué significa "auto-host de CLM" para Mistral. Dato del Soberano, pendiente.
Dispositivo de referencia y su RAM real para WebGPU.
Tamaños reales de los modelos mini.
Método de acceso remoto a nodos.
Decisiones que están en la parte privada y en el rack. No se deducen aquí.
