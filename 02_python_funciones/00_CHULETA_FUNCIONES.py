# ============================================================
# CHULETA - FUNCIONES EN PYTHON
# ============================================================

# Una función es un bloque de código reutilizable.
#
# Sirve para:
# - evitar repetir código
# - organizar mejor un programa
# - dividir problemas grandes en partes pequeñas


# ============================================================
# 1. FUNCIÓN BÁSICA
# ============================================================

def saludar():
    print("Hola")


saludar()


# ============================================================
# 2. FUNCIÓN CON PARÁMETROS
# ============================================================

# Un parámetro es una variable que recibe un valor cuando llamamos a la función.

def saludar_usuario(nombre):
    print(f"Hola, {nombre}")


saludar_usuario("Adri")


# En este ejemplo:
#
# nombre es el parámetro.
# "Adri" es el argumento.
#
# El argumento es el valor real que enviamos.
# El parámetro es el nombre que usa la función por dentro.


# ============================================================
# 3. FUNCIÓN CON VARIOS PARÁMETROS
# ============================================================

def mostrar_personaje(nombre, vida, nivel):
    print(f"Nombre: {nombre}")
    print(f"Vida: {vida}")
    print(f"Nivel: {nivel}")


mostrar_personaje("Arthas", 100, 1)


# Python asigna los valores por posición:
#
# "Arthas" -> nombre
# 100      -> vida
# 1        -> nivel


# ============================================================
# 4. RETURN
# ============================================================

# return devuelve un valor desde la función.

def sumar(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado


total = sumar(5, 3)

print(total)


# Importante:
#
# print() muestra algo en pantalla.
# return devuelve un valor para poder usarlo después.


# ============================================================
# 5. FUNCIÓN QUE MODIFICA UN DICCIONARIO
# ============================================================

def agregar_objeto(inventario, objeto, cantidad):
    if objeto in inventario:
        inventario[objeto] += cantidad
    else:
        inventario[objeto] = cantidad

    return inventario


inventario_jugador = {
    "oro": 50,
    "flechas": 12
}

inventario_jugador = agregar_objeto(inventario_jugador, "oro", 20)

print(inventario_jugador)


# ============================================================
# 6. FUNCIÓN CON INPUT
# ============================================================

def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre


# nombre_usuario = pedir_nombre()
# print(nombre_usuario)


# ============================================================
# 7. FUNCIÓN CON WHILE Y TRY/EXCEPT
# ============================================================

def pedir_numero(mensaje):
    # Repite la pregunta hasta que el usuario escriba un número válido.
    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            # ValueError ocurre si int() no puede convertir el texto en número.
            # Ejemplo: int("dos") produce ValueError.
            print("Error: debes escribir un número entero.")


# edad = pedir_numero("Edad: ")
# print(edad)


# ============================================================
# 8. NONE
# ============================================================

# None significa ausencia de valor válido.

def dividir(numero_1, numero_2):
    try:
        resultado = numero_1 / numero_2
        return resultado

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
        return None


resultado_division = dividir(10, 0)

if resultado_division is not None:
    print(resultado_division)
else:
    print("No hay resultado válido.")


# ============================================================
# 9. RESUMEN RÁPIDO
# ============================================================

# def nombre_funcion():
#     Crea una función.
#
# parámetro:
#     Variable que recibe un valor dentro de la función.
#
# argumento:
#     Valor real que enviamos al llamar a la función.
#
# return:
#     Devuelve un valor.
#
# print:
#     Muestra algo en pantalla.
#
# None:
#     Representa que no hay un valor válido.
#
# ValueError:
#     Error cuando una conversión de tipo falla.
#
# ZeroDivisionError:
#     Error cuando intentamos dividir entre cero.