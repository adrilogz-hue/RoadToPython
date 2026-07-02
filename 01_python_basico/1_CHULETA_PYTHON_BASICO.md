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



## Git básico

`git status` — Muestra el estado actual del repositorio.

`git add .` — Prepara todos los archivos modificados para el próximo commit.

`git add archivo.py` — Prepara un archivo concreto para el próximo commit.

`git commit -m "mensaje"` — Guarda una versión del proyecto en Git.

`git push` — Sube los commits locales a GitHub.

`git init` — Crea un repositorio Git en la carpeta actual.

`git branch -M main` — Cambia el nombre de la rama principal a `main`.

`git remote add origin URL` — Conecta el repositorio local con GitHub.



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