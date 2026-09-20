# \# Proyecto Final - Tic Tac Toe

# 

# \## Descripción

# 

# Este proyecto corresponde a la modificación de un videojuego de la librería open source Freegames de Python.

# 

# El juego seleccionado fue Tic Tac Toe. A partir de la versión original se analizó el funcionamiento del código y se implementaron mejoras visuales y funcionales utilizando Python, Turtle Graphics y Git como sistema de control de versiones.

# 

# \## Datos del alumno

# 

# \- Matrícula: A01713962

# \- Usuario de GitHub: jojuespinosa-7

# \- Juego seleccionado: Tic Tac Toe

# \- Rama de trabajo: A01713962\_tictactoe

# 

# \## Objetivo

# 

# El objetivo del proyecto fue aplicar los conocimientos adquiridos durante el curso relacionados con:

# 

# \- Uso de la terminal.

# \- Control de versiones con Git.

# \- Uso de GitHub.

# \- Manejo de ramas.

# \- Buenas prácticas en commits.

# \- Programación en Python.

# \- Análisis y modificación de código existente.

# \- Documentación del proceso de desarrollo.

# 

# \## Tecnologías utilizadas

# 

# \- Python 3

# \- Turtle Graphics

# \- Freegames

# \- Git

# \- GitHub

# \- Windows PowerShell

# \- Entorno virtual de Python (.venv)

# 

# \## Preparación del ambiente de desarrollo

# 

# El proyecto fue desarrollado utilizando PowerShell de Windows, ya que la aplicación utiliza Turtle Graphics para mostrar la interfaz gráfica del videojuego.

# 

# Primero se clonó el repositorio del proyecto en la computadora.

# 

# Posteriormente se creó un entorno virtual de Python utilizando el siguiente comando:

# 

# python -m venv .venv

# 

# El entorno virtual se activó mediante:

# 

# .\\.venv\\Scripts\\Activate.ps1

# 

# Después se instaló la librería Freegames utilizando:

# 

# python -m pip install freegames

# 

# Para verificar que Freegames se hubiera instalado correctamente se utilizó:

# 

# python -m freegames list

# 

# Este comando mostró la lista de videojuegos disponibles dentro de la librería, incluyendo Tic Tac Toe.

# 

# La versión original del juego se ejecutó con:

# 

# python -m freegames.tictactoe

# 

# Después de comprobar que la versión original funcionaba correctamente, el código fuente fue copiado al repositorio utilizando:

# 

# python -m freegames copy tictactoe

# 

# Este comando generó el archivo tictactoe.py, sobre el cual se realizaron todas las modificaciones del proyecto.

# 

# \## Rama de trabajo

# 

# Para desarrollar las modificaciones se creó una rama individual siguiendo el formato solicitado para el proyecto.

# 

# La rama utilizada fue:

# 

# A01713962\_tictactoe

# 

# Todas las modificaciones fueron desarrolladas primero dentro de esta rama.

# 

# Posteriormente, una vez terminadas y verificadas, la rama fue integrada a la rama principal main.

# 

# \## Modificación 1 - Apariencia y centrado de X y O

# 

# La primera modificación consistió en cambiar la apariencia de los símbolos utilizados por los jugadores.

# 

# En la versión original del juego, X y O utilizaban el estilo gráfico predeterminado.

# 

# Se realizaron los siguientes cambios:

# 

# \- La X se dibuja en color rojo.

# \- La O se dibuja en color azul.

# \- Se aumentó el grosor de ambos símbolos.

# \- Se modificaron las coordenadas utilizadas para dibujar los símbolos.

# \- X y O quedaron centrados dentro de cada casilla.

# \- Se dejó un margen entre los símbolos y las líneas del tablero para mejorar la presentación visual.

# 

# La función drawx fue modificada para dibujar una X roja con mayor grosor.

# 

# La función drawo fue modificada para dibujar una O azul y mantenerla centrada dentro de la casilla correspondiente.

# 

# \## Modificación 2 - Validación de casillas ocupadas

# 

# La segunda modificación consistió en impedir que un jugador pudiera seleccionar una casilla que ya había sido utilizada.

# 

# Para implementar esta funcionalidad se agregó una estructura llamada board dentro del estado del juego.

# 

# Esta estructura almacena las coordenadas de cada casilla ocupada y el jugador que realizó el movimiento.

# 

# Antes de realizar cada movimiento, el programa verifica si la posición seleccionada ya existe dentro de board.

# 

# Si una casilla ya se encuentra ocupada:

# 

# \- El clic es ignorado.

# \- No se dibuja un nuevo símbolo.

# \- El turno no cambia.

# \- El juego continúa normalmente.

# 

# Esto evita que una X o una O pueda dibujarse encima de otro símbolo.

# 

# \## Modificación 3 - Detección de ganador y empate

# 

# La tercera modificación consistió en agregar la lógica necesaria para detectar automáticamente cuándo termina una partida.

# 

# Se creó una función llamada check\_winner.

# 

# Esta función analiza las ocho combinaciones posibles para ganar una partida de Tic Tac Toe:

# 

# \- Tres combinaciones horizontales.

# \- Tres combinaciones verticales.

# \- Dos combinaciones diagonales.

# 

# Cada vez que un jugador realiza un movimiento, el programa verifica si dicho movimiento produjo una combinación ganadora.

# 

# Si existe un ganador, el programa identifica qué jugador ganó y muestra en la parte superior del tablero uno de los siguientes mensajes:

# 

# X wins!

# 

# o

# 

# O wins!

# 

# También se agregó una variable llamada game\_over.

# 

# Esta variable permite bloquear nuevos movimientos después de que la partida haya terminado.

# 

# \## Detección de empate

# 

# Además de detectar un ganador, se implementó la detección de empate.

# 

# El programa cuenta las posiciones almacenadas dentro del tablero.

# 

# Si las nueve casillas se encuentran ocupadas y ningún jugador ha conseguido una combinación ganadora, la partida termina en empate.

# 

# En ese caso el programa muestra el siguiente mensaje:

# 

# Tie game!

# 

# Después de mostrar el empate tampoco se permiten nuevos movimientos.

# 

# \## Estado del juego

# 

# Para controlar el funcionamiento del programa se utiliza una estructura llamada state.

# 

# Esta estructura contiene tres elementos principales:

# 

# player

# 

# Indica el jugador que tiene el turno actual.

# 

# El valor 0 representa al jugador X.

# 

# El valor 1 representa al jugador O.

# 

# board

# 

# Almacena las casillas que ya fueron utilizadas durante la partida.

# 

# Cada posición del tablero se relaciona con el jugador que realizó el movimiento.

# 

# game\_over

# 

# Indica si la partida ya terminó debido a una victoria o un empate.

# 

# Cuando game\_over tiene el valor True, el programa ignora cualquier clic adicional.

# 

# \## Comentarios y documentación del código

# 

# El código fue documentado utilizando comentarios y docstrings.

# 

# Se decidió mantener los comentarios en inglés para conservar consistencia con el idioma utilizado originalmente en el código de Freegames.

# 

# Se agregaron comentarios para explicar principalmente:

# 

# \- El estado general del juego.

# \- El funcionamiento de la variable player.

# \- El almacenamiento de casillas ocupadas.

# \- La función de la variable game\_over.

# \- El proceso de validación de casillas.

# \- Las combinaciones posibles para ganar.

# \- La detección de ganador.

# \- La detección de empate.

# \- El proceso de dibujo de X y O.

# \- El cambio de turno entre jugadores.

# \- El bloqueo de movimientos después de terminar la partida.

# 

# La documentación se agregó buscando que otra persona pueda comprender la lógica del programa sin necesidad de analizar cada instrucción individualmente.

# 

# \## Pruebas realizadas

# 

# Durante el desarrollo se realizaron diferentes pruebas para comprobar el funcionamiento de las modificaciones.

# 

# \### Prueba de la versión original

# 

# Antes de realizar modificaciones se ejecutó el videojuego original utilizando Freegames.

# 

# Se verificó que el tablero se abriera correctamente mediante Turtle Graphics y que fuera posible colocar X y O.

# 

# \### Prueba de apariencia

# 

# Se verificó que:

# 

# \- X apareciera en color rojo.

# \- O apareciera en color azul.

# \- Los símbolos tuvieran mayor grosor.

# \- Los símbolos estuvieran centrados dentro de las casillas.

# \- Los símbolos no se sobrepusieran con las líneas del tablero.

# 

# El resultado de la prueba fue correcto.

# 

# \### Prueba de casillas ocupadas

# 

# Se realizó un movimiento en una casilla y posteriormente se intentó seleccionar la misma posición varias veces.

# 

# El comportamiento esperado era que el segundo clic fuera ignorado.

# 

# El resultado obtenido fue correcto:

# 

# \- No se dibujó un segundo símbolo.

# \- El turno no cambió.

# \- La casilla permaneció ocupada por el jugador original.

# 

# \### Prueba de victoria

# 

# Se realizaron movimientos para generar una combinación ganadora.

# 

# Por ejemplo, se realizó una combinación diagonal de tres X.

# 

# El programa detectó correctamente la victoria y mostró:

# 

# X wins!

# 

# Después de detectar la victoria se intentó seguir seleccionando casillas.

# 

# El programa bloqueó correctamente los nuevos movimientos.

# 

# \### Prueba de empate

# 

# Se llenaron las nueve casillas del tablero sin formar ninguna combinación ganadora.

# 

# Al utilizar todas las posiciones, el programa detectó correctamente el empate y mostró:

# 

# Tie game!

# 

# También se comprobó que después del empate ya no fuera posible realizar nuevos movimientos.

# 

# \## Uso de Git

# 

# Git fue utilizado como sistema de control de versiones durante todo el desarrollo.

# 

# Se trabajó utilizando una rama individual llamada:

# 

# A01713962\_tictactoe

# 

# Se realizó un commit independiente para cada modificación importante con el objetivo de mantener un historial claro y organizado.

# 

# \## Historial de commits

# 

# Los commits principales realizados durante el proyecto fueron:

# 

# 9692c68 - feat: agrega versión inicial de Tic Tac Toe

# 

# Este commit contiene la versión original de Tic Tac Toe descargada desde la librería Freegames.

# 

# 10a40ee - feat: mejora apariencia y centrado de X y O

# 

# Este commit contiene los cambios visuales realizados en los símbolos del juego.

# 

# 7151deb - fix: evita jugar en casillas ocupadas

# 

# Este commit agrega la validación necesaria para impedir movimientos sobre posiciones utilizadas.

# 

# c268ca2 - feat: detecta ganador y empate

# 

# Este commit implementa la detección de victoria, empate y finalización de la partida.

# 

# 9a879dd - docs: documenta estado y lógica del juego

# 

# Este commit agrega documentación y comentarios adicionales para facilitar la comprensión del código.

# 

# \## Buenas prácticas de Git

# 

# Durante el desarrollo se buscó seguir buenas prácticas de control de versiones.

# 

# Las principales prácticas utilizadas fueron:

# 

# \- Trabajar en una rama individual.

# \- Mantener la rama main estable.

# \- Realizar un commit diferente para cada cambio importante.

# \- Utilizar mensajes de commit descriptivos.

# \- Utilizar prefijos como feat, fix y docs.

# \- Verificar los cambios mediante git diff antes de realizar commits.

# \- Verificar el estado del repositorio mediante git status.

# \- Subir los cambios regularmente al repositorio remoto.

# \- Integrar la rama individual a main únicamente después de terminar y verificar las modificaciones.

# 

# \## Integración con main

# 

# Una vez terminadas las modificaciones, se cambió a la rama principal main.

# 

# Se actualizó la rama utilizando:

# 

# git pull origin main

# 

# Posteriormente se integró la rama individual utilizando:

# 

# git merge A01713962\_tictactoe

# 

# Finalmente, los cambios fueron enviados al repositorio remoto mediante:

# 

# git push origin main

# 

# De esta manera, todas las modificaciones realizadas quedaron disponibles dentro de la rama principal del proyecto.

# 

# \## Ejecución del juego

# 

# Para ejecutar el videojuego es necesario tener Python y Freegames instalados.

# 

# Con el entorno virtual activado, el programa puede ejecutarse mediante:

# 

# python tictactoe.py

# 

# Al ejecutar el comando se abre una ventana de Turtle Graphics.

# 

# Los jugadores realizan movimientos haciendo clic sobre las diferentes casillas del tablero.

# 

# X comienza la partida y posteriormente los jugadores alternan turnos.

# 

# \## Estructura del proyecto

# 

# La estructura principal del proyecto es:

# 

# Proyecto\_Final\_Freegames/

# 

# tictactoe.py

# README.md

# .gitignore

# 

# El archivo tictactoe.py contiene el código del videojuego modificado.

# 

# El archivo README.md contiene la documentación del proyecto.

# 

# El archivo .gitignore evita almacenar archivos y directorios que no deben formar parte del repositorio.

# 

# El directorio .venv se utiliza localmente para el entorno virtual de Python y no debe almacenarse dentro del repositorio.

# 

# \## Resultados

# 

# La versión final del videojuego permite:

# 

# \- Jugar Tic Tac Toe utilizando una interfaz gráfica.

# \- Mostrar X en color rojo.

# \- Mostrar O en color azul.

# \- Mantener ambos símbolos centrados.

# \- Impedir movimientos sobre casillas ocupadas.

# \- Detectar automáticamente una victoria.

# \- Identificar al jugador ganador.

# \- Detectar automáticamente un empate.

# \- Mostrar el resultado de la partida en la pantalla.

# \- Bloquear movimientos después de terminar el juego.

# 

# \## Conclusión

# 

# Este proyecto permitió aplicar de forma práctica los conocimientos adquiridos sobre programación en Python, uso de terminal, Git y GitHub.

# 

# A partir de un código existente de la librería Freegames fue necesario analizar su estructura y comprender el funcionamiento de las funciones originales antes de realizar las modificaciones.

# 

# El uso de ramas permitió desarrollar los cambios sin afectar directamente la rama principal.

# 

# La separación de las modificaciones en diferentes commits permitió mantener un historial claro del proceso de desarrollo.

# 

# Las modificaciones realizadas mejoraron tanto la presentación visual como el funcionamiento del videojuego.

# 

# Finalmente, el uso de comentarios y documentación permitió dejar un proyecto más fácil de comprender, mantener y revisar.

