# Chuleta Python básico


## Conceptos generales

`print()` — Muestra información en pantalla.

`input()` — Pide información al usuario y la guarda como texto.

`int()` — Convierte un texto numérico en número entero.

`.lower()` — Convierte un texto a minúsculas.

`type()` — Muestra el tipo de dato de una variable.

`# comentario` — Línea ignorada por Python; sirve para dejar notas en el código.



## Variables y tipos de datos

`nombre = "Adrian"` — Guarda texto en una variable.

`edad = 30` — Guarda un número entero en una variable.

`horas = 4` — Guarda un dato numérico que luego se puede usar en cálculos.

`str` — Tipo de dato texto.

`int` — Tipo de dato número entero.

`True` — Valor lógico verdadero.

`False` — Valor lógico falso.



## Textos y f-strings

`f"Hola {nombre}"` — Permite insertar variables dentro de un texto.

`{variable}` — Dentro de una f-string, inserta el valor de una variable.

`persona["nombre"]` — Accede al valor de la clave `"nombre"` dentro de un diccionario.

`f"{persona['nombre']}"` — Inserta un valor de diccionario dentro de una f-string.



## Operadores matemáticos

`+` — Suma.

`-` — Resta.

`*` — Multiplicación.

`/` — División.

`+=` — Suma una cantidad al valor actual.

`-=` — Resta una cantidad al valor actual.



## Comparaciones

`=` — Asigna un valor a una variable.

`==` — Compara si dos valores son iguales.

`!=` — Compara si dos valores son diferentes.

`>` — Mayor que.

`<` — Menor que.

`>=` — Mayor o igual que.

`<=` — Menor o igual que.



## Condicionales

`if` — Ejecuta un bloque si la condición se cumple.

`elif` — Comprueba otra condición si la anterior no se cumple.

`else` — Ejecuta un bloque si ninguna condición anterior se cumple.

`and` — Exige que dos condiciones sean verdaderas.

`or` — Exige que al menos una condición sea verdadera.

`not` — Invierte una condición.

`in` — Comprueba si un valor está dentro de una lista o diccionario.

`not in` — Comprueba si un valor no está dentro de una lista o diccionario.



## Listas

`rutas = ["data", "qa", "backend"]` — Crea una lista con varios elementos.

`rutas[0]` — Accede al primer elemento de la lista.

`rutas.append("devops")` — Añade un elemento al final de la lista.

`len(rutas)` — Cuenta cuántos elementos tiene la lista.



## Diccionarios

`persona = {"nombre": "Adrian", "edad": 30}` — Crea un diccionario con claves y valores.

`persona["nombre"]` — Lee el valor asociado a la clave `"nombre"`.

`persona["ruta"] = "Python"` — Crea o actualiza una clave del diccionario.

`del persona["ruta"]` — Elimina una clave del diccionario.

`persona.items()` — Permite recorrer clave y valor al mismo tiempo.



## Bucles

`for elemento in lista:` — Recorre una lista elemento por elemento.

`for clave, valor in diccionario.items():` — Recorre un diccionario obteniendo clave y valor.



## Sangría

La sangría indica qué líneas pertenecen a un bloque `if`, `elif`, `else`, `for` o `def`.

Después de `:` normalmente la siguiente línea va indentada.


## Terminal

`cd carpeta` — Entra en una carpeta.

`cd ..` — Sube una carpeta hacia atrás.

`pwd` — Muestra la carpeta actual.

`mkdir nombre` — Crea una carpeta nueva.

`python archivo.py` — Ejecuta un archivo Python.



## Nombres de archivos

Usar minúsculas, números y guiones bajos.

Correcto: `01_funciones_basicas.py`

Evitar espacios: `f string.py`

Mejor: `f_string.py`


===========================================================
## Git básico
===========================================================

`git status` — Muestra el estado actual del repositorio.

`git add .` — Prepara todos los archivos modificados para el próximo commit.

`git add archivo.py` — Prepara un archivo concreto para el próximo commit.

`git commit -m "mensaje"` — Guarda una versión del proyecto en Git.

`git push` — Sube los commits locales a GitHub.

`git init` — Crea un repositorio Git en la carpeta actual.

`git branch -M main` — Cambia el nombre de la rama principal a `main`.

`git remote add origin URL` — Conecta el repositorio local con GitHub.


# ============================================================
# USO INTERMEDIO DE GIT EN EMPRESA
# ============================================================

# Situación típica:
#
# Estás trabajando en tu rama:
#
# feature/consulta-pedidos
#
# Pero mientras tú trabajas, otros compañeros han subido cambios nuevos a main.
# Antes de terminar tu tarea o abrir la Pull Request, conviene actualizar tu rama
# con los últimos cambios de main.


# ============================================================
# 1. ACTUALIZAR MAIN
# ============================================================

# Primero volvemos a main y traemos los últimos cambios del repositorio remoto.

# git checkout main
# git pull


# ============================================================
# 2. VOLVER A TU RAMA DE TRABAJO
# ============================================================

# Después vuelves a tu rama.

# git checkout feature/consulta-pedidos


# ============================================================
# 3. TRAER LOS CAMBIOS DE MAIN A TU RAMA
# ============================================================

# Hay dos formas habituales: merge o rebase.


# ------------------------------------------------------------
# OPCIÓN A: MERGE
# ------------------------------------------------------------

# git merge main

# Esto une los cambios de main dentro de tu rama.
#
# Ventaja:
# - Es más fácil de entender.
# - Es más seguro para principiantes.
#
# Desventaja:
# - Puede crear commits extra de merge.
# - El historial puede quedar menos limpio.


# ------------------------------------------------------------
# OPCIÓN B: REBASE
# ------------------------------------------------------------

# git rebase main

# Esto "recoloca" tus commits encima de la versión más reciente de main.
#
# Ventaja:
# - El historial queda más limpio y lineal.
#
# Desventaja:
# - Es más delicado.
# - Si no se entiende bien, puede liar el historial.
#
# Como junior, si la empresa no te indica otra cosa, normalmente es más seguro
# usar merge al principio.


# ============================================================
# 4. POSIBLE CONFLICTO
# ============================================================

# Un conflicto ocurre cuando Git no sabe qué cambio conservar.
#
# Ejemplo:
# Tú modificaste una línea de app.py.
# Otro compañero modificó esa misma línea en main.
#
# Git no puede decidir automáticamente cuál es la correcta.


# Flujo básico ante conflicto:
#
# 1. Abrir los archivos marcados con conflicto.
# 2. Revisar las marcas:
#
# <<<<<<< HEAD
# tu versión
# =======
# versión de main
# >>>>>>> main
#
# 3. Dejar el código final correcto.
# 4. Guardar el archivo.
# 5. Añadir el archivo corregido.
#
# git add archivo_con_conflicto.py
#
# 6. Continuar el proceso.


# Si estabas haciendo merge:
#
# git commit
#
# o, a veces:
#
# git merge --continue


# Si estabas haciendo rebase:
#
# git rebase --continue


# ============================================================
# 5. SUBIR TU RAMA ACTUALIZADA
# ============================================================

# Después de resolver conflictos y probar que todo funciona:

# git status
# git push origin feature/consulta-pedidos


# Si has hecho rebase, puede que Git te pida:
#
# git push --force-with-lease
#
# Importante:
# --force-with-lease es más seguro que --force.
# Aun así, no lo uses sin entenderlo o sin que te lo indiquen.


# ============================================================
# RESUMEN PROFESIONAL
# ============================================================

# Flujo intermedio típico:
#
# git checkout main
# git pull
# git checkout feature/consulta-pedidos
# git merge main
#
# resolver conflictos si aparecen
#
# git status
# git add .
# git commit
# git push origin feature/consulta-pedidos


# ============================================================
# IDEA CLAVE
# ============================================================

# En una empresa tu rama no vive aislada.
# Mientras tú trabajas, main sigue cambiando.
#
# Por eso a veces tienes que actualizar tu rama con los últimos cambios
# antes de abrir o terminar una Pull Request.
#
# Esto ayuda a:
# - evitar conflictos grandes al final
# - comprobar que tu código funciona con la versión actual del proyecto
# - facilitar la revisión de la Pull Request


# ============================================================
# EJEMPLO DE USO DE GIT EN UNA EMPRESA
# ============================================================

# En una empresa normalmente no se trabaja directamente sobre main.
# main suele representar el código estable o de producción.

# Flujo típico:

# 1. Actualizar tu copia local del proyecto
# Antes de empezar, traes los últimos cambios del equipo.
#
# git checkout main
# git pull

# 2. Crear una rama para tu tarea
# Cada ticket o tarea suele tener su propia rama.
#
# Ejemplo:
# ticket: "crear endpoint para consultar pedidos"
#
# git checkout -b feature/consulta-pedidos

# 3. Trabajar en el código
# Modificas archivos, pruebas el programa y compruebas que funciona.

# 4. Revisar cambios
#
# git status
# git diff

# 5. Guardar cambios en commits
#
# git add .
# git commit -m "Añade endpoint para consultar pedidos"

# 6. Subir la rama al repositorio remoto
#
# git push origin feature/consulta-pedidos

# 7. Crear una Pull Request
# En GitHub/GitLab/Bitbucket abres una Pull Request para que otro compañero revise tu código.
#
# En la PR normalmente explicas:
# - qué has cambiado
# - por qué lo has cambiado
# - cómo probarlo
# - si afecta a algo importante

# 8. Revisión de código
# Un compañero revisa tu código y puede:
# - aprobarlo
# - pedir cambios
# - dejar comentarios

# 9. Corregir comentarios si hace falta
#
# Haces cambios nuevos:
#
# git add .
# git commit -m "Corrige validación de pedidos"
# git push

# 10. Merge a main
# Cuando la PR está aprobada, se fusiona con main.
# Normalmente esto lo hace GitHub/GitLab con un botón de "Merge".


# ============================================================
# RESUMEN RÁPIDO DEL FLUJO PROFESIONAL
# ============================================================

# main
#   Rama estable del proyecto.
#
# feature/nombre-tarea
#   Rama donde trabajas una tarea concreta.
#
# commit
#   Guarda un conjunto de cambios con un mensaje.
#
# push
#   Sube tu rama a GitHub/GitLab.
#
# pull
#   Baja cambios del repositorio remoto.
#
# Pull Request
#   Solicitud para revisar y unir tu código a main.
#
# code review
#   Revisión del código por parte de otro programador.
#
# merge
#   Unión de tu rama con main.


# ============================================================
# EJEMPLO COMPLETO DE COMANDOS
# ============================================================

# git checkout main
# git pull
# git checkout -b feature/consulta-pedidos
#
# trabajar en el código...
#
# git status
# git add .
# git commit -m "Añade consulta de pedidos"
# git push origin feature/consulta-pedidos
#
# Después se crea la Pull Request desde GitHub/GitLab.