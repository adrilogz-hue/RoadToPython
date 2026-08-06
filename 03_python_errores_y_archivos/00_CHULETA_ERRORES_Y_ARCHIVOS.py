# ============================================================
# CHULETA - ERRORES Y ARCHIVOS EN PYTHON
# ============================================================

# Este bloque sirve para aprender dos cosas importantes:
#
# 1. Manejar errores para que el programa no se rompa.
# 2. Guardar y leer datos usando archivos .txt.
#
# Conceptos principales:
# - try
# - except
# - ValueError
# - ZeroDivisionError
# - FileNotFoundError
# - None
# - open()
# - modos "w", "r", "a"
# - read()
# - write()
# - for linea in archivo
# - strip()
# - split()


# ============================================================
# 1. TRY / EXCEPT
# ============================================================

# try significa:
# "intenta ejecutar este código".
#
# except significa:
# "si ocurre este error, ejecuta este otro código".

try:
    edad = int(input("Edad: "))
    print(f"Tienes {edad} años.")

except ValueError:
    # ValueError ocurre si int() no puede convertir el texto en número.
    # Ejemplo: int("treinta") produce ValueError.
    print("Error: debes escribir un número.")


# ============================================================
# 2. VALUEERROR
# ============================================================

# ValueError aparece cuando el tipo de dato es correcto,
# pero el valor no se puede convertir o usar como esperábamos.

# Ejemplo:
#
# int("25")       funciona
# int("treinta") falla con ValueError

try:
    numero = int(input("Escribe un número: "))
    print(numero)

except ValueError:
    print("Error: el valor introducido no es válido.")


# ============================================================
# 3. WHILE TRUE CON TRY / EXCEPT
# ============================================================

# Este patrón sirve para repetir una pregunta hasta que el usuario
# escriba un dato válido.

while True:
    try:
        numero = int(input("Número válido: "))
        break

    except ValueError:
        print("Error: debes escribir un número entero.")

print(f"Número aceptado: {numero}")


# ============================================================
# 4. FUNCIÓN PEDIR_NUMERO()
# ============================================================

# Esta función reutiliza el patrón anterior.
# Así no tenemos que repetir try/except en muchas partes del programa.

def pedir_numero(mensaje):
    # mensaje es un parámetro.
    # Recibe el texto que queremos mostrar en input().
    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            # ValueError ocurre si int() no puede convertir el texto en número.
            print("Error: debes escribir un número entero.")


edad_usuario = pedir_numero("Introduce tu edad: ")
print(f"Edad guardada: {edad_usuario}")


# ============================================================
# 5. ZERODIVISIONERROR
# ============================================================

# ZeroDivisionError ocurre si intentamos dividir entre 0.

try:
    numero_1 = int(input("Primer número: "))
    numero_2 = int(input("Segundo número: "))

    resultado = numero_1 / numero_2

    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes escribir números.")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")


# ============================================================
# 6. NONE
# ============================================================

# None significa ausencia de valor válido.
#
# Lo usamos cuando una función no puede devolver un resultado correcto.

def dividir(numero_1, numero_2):
    try:
        resultado = numero_1 / numero_2
        return resultado

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
        return None


resultado_division = dividir(10, 0)

if resultado_division is not None:
    print(f"Resultado: {resultado_division}")
else:
    print("No hay resultado válido.")


# ============================================================
# 7. ARCHIVOS - OPEN()
# ============================================================

# open() sirve para abrir archivos.
#
# Estructura general:
#
# with open("archivo.txt", "modo", encoding="utf-8") as archivo:
#     código para trabajar con el archivo
#
# with se encarga de cerrar el archivo automáticamente al terminar.
#
# encoding="utf-8" ayuda a trabajar correctamente con:
# á, é, í, ó, ú, ñ


# ============================================================
# 8. MODO "w" - WRITE
# ============================================================

# "w" significa write, es decir, escribir.
#
# Si el archivo no existe, Python lo crea.
# Si el archivo ya existe, Python borra su contenido anterior.

with open("ejemplo_write.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea escrita desde Python.\n")
    archivo.write("Segunda línea escrita desde Python.\n")

print("Archivo escrito con modo w.")


# ============================================================
# 9. MODO "r" - READ
# ============================================================

# "r" significa read, es decir, leer.
#
# El archivo debe existir.
# Si no existe, Python lanzará FileNotFoundError.

with open("ejemplo_write.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido leído:")
print(contenido)


# ============================================================
# 10. MODO "a" - APPEND
# ============================================================

# "a" significa append, es decir, añadir al final.
#
# No borra el contenido anterior.
# Añade nuevas líneas al final del archivo.

with open("ejemplo_write.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Nueva línea añadida con append.\n")

print("Línea añadida con modo a.")


# ============================================================
# 11. LEER LÍNEA POR LÍNEA
# ============================================================

# Leer línea por línea es útil cuando:
# - el archivo es grande
# - queremos buscar algo
# - queremos procesar cada línea por separado
#
# archivo.read() lee todo de golpe.
# for linea in archivo lee una línea cada vez.

with open("ejemplo_write.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())


# ============================================================
# 12. STRIP()
# ============================================================

# strip() elimina espacios y saltos de línea al principio y al final.
#
# Ejemplo:
#
# "   oro:50\n".strip()
#
# se convierte en:
#
# "oro:50"

texto = "   oro:50\n"
texto_limpio = texto.strip()

print(texto_limpio)


# ============================================================
# 13. SPLIT()
# ============================================================

# split() separa un texto usando un separador.
#
# Ejemplo:
#
# "oro:50".split(":")
#
# produce:
#
# ["oro", "50"]

linea = "oro:50"
partes = linea.split(":")

objeto = partes[0]
cantidad = int(partes[1])

print(objeto)
print(cantidad)


# ============================================================
# 14. FILENOTFOUNDERROR
# ============================================================

# FileNotFoundError ocurre si intentamos leer un archivo que no existe.

try:
    with open("archivo_que_no_existe.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe.")


# ============================================================
# 15. GUARDAR UN DICCIONARIO EN TXT
# ============================================================

# Ejemplo de inventario:
#
# {
#     "oro": 50,
#     "flechas": 12
# }
#
# Lo guardaremos así:
#
# oro:50
# flechas:12

inventario = {
    "oro": 50,
    "flechas": 12,
    "pocion de curacion": 3
}

with open("inventario_chuleta.txt", "w", encoding="utf-8") as archivo:
    for objeto, cantidad in inventario.items():
        archivo.write(f"{objeto}:{cantidad}\n")

print("Inventario guardado en archivo.")


# ============================================================
# 16. CARGAR UN DICCIONARIO DESDE TXT
# ============================================================

inventario_cargado = {}

with open("inventario_chuleta.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()

        if linea != "":
            partes = linea.split(":")

            objeto = partes[0]
            cantidad = int(partes[1])

            inventario_cargado[objeto] = cantidad

print("Inventario cargado:")
print(inventario_cargado)


# ============================================================
# 17. CARGAR ARCHIVO O CREAR DATOS INICIALES
# ============================================================

# Este patrón es muy importante:
#
# 1. Intentar cargar datos desde archivo.
# 2. Si el archivo no existe, crear datos iniciales.

def crear_inventario_inicial():
    return {
        "oro": 50,
        "flechas": 12,
        "pocion de curacion": 3
    }


def cargar_inventario_seguro():
    inventario = {}

    try:
        with open("inventario_chuleta.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if linea != "":
                    partes = linea.split(":")

                    objeto = partes[0]
                    cantidad = int(partes[1])

                    inventario[objeto] = cantidad

        return inventario

    except FileNotFoundError:
        print("No existe el archivo. Se usará inventario inicial.")
        return crear_inventario_inicial()


inventario_final = cargar_inventario_seguro()

print(inventario_final)


# ============================================================
# 18. RESUMEN RÁPIDO
# ============================================================

# try:
#     Intenta ejecutar código que puede fallar.
#
# except ValueError:
#     Captura errores de conversión de valores.
#
# except ZeroDivisionError:
#     Captura divisiones entre cero.
#
# except FileNotFoundError:
#     Captura archivos inexistentes.
#
# None:
#     Representa que no hay un valor válido.
#
# open("archivo.txt", "w"):
#     Abre archivo para escribir. Borra lo anterior.
#
# open("archivo.txt", "r"):
#     Abre archivo para leer. El archivo debe existir.
#
# open("archivo.txt", "a"):
#     Abre archivo para añadir al final.
#
# archivo.write("texto"):
#     Escribe texto en el archivo.
#
# archivo.read():
#     Lee todo el archivo de golpe.
#
# for linea in archivo:
#     Lee el archivo línea por línea.
#
# strip():
#     Limpia espacios y saltos de línea al principio y al final.
#
# split(":"):
#     Divide un texto usando ":" como separador.
#
# encoding="utf-8":
#     Ayuda a trabajar bien con tildes y ñ.


# ============================================================
# 19. PATRONES IMPORTANTES DEL BLOQUE
# ============================================================

# Patrón 1: pedir número seguro
#
# def pedir_numero(mensaje):
#     while True:
#         try:
#             return int(input(mensaje))
#         except ValueError:
#             print("Error: debes escribir un número.")


# Patrón 2: división segura
#
# def dividir(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None


# Patrón 3: leer archivo seguro
#
# try:
#     with open("datos.txt", "r", encoding="utf-8") as archivo:
#         contenido = archivo.read()
# except FileNotFoundError:
#     print("El archivo no existe.")


# Patrón 4: guardar diccionario
#
# with open("datos.txt", "w", encoding="utf-8") as archivo:
#     for clave, valor in diccionario.items():
#         archivo.write(f"{clave}:{valor}\n")


# Patrón 5: cargar diccionario
#
# diccionario = {}
#
# with open("datos.txt", "r", encoding="utf-8") as archivo:
#     for linea in archivo:
#         partes = linea.strip().split(":")
#         clave = partes[0]
#         valor = int(partes[1])
#         diccionario[clave] = valor