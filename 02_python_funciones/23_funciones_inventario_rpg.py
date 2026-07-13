def crear_inventario():
    # Crea un diccionario inicial para el inventario
    # Cada clave es un objeto y cada valor es la cantidad disponible
    return {
        "pocion de curacion": 3,
        "espada corta": 1,
        "arco": 1,
        "flechas": 12,
        "oro": 50
    }


def mostrar_inventario(inventario):
    # Recorre el diccionario y muestra cada objeto con su cantidad
    print("Inventario del personaje")
    print("------------------------")

    for objeto, cantidad in inventario.items():
        print(f"{objeto}: {cantidad}")


def agregar_objeto(inventario, objeto, cantidad):
    # Si el objeto ya existe, aumenta su cantidad
    # Si no existe, lo crea con la cantidad indicada
    if objeto in inventario:
        inventario[objeto] += cantidad
    else:
        inventario[objeto] = cantidad

    return inventario


def eliminar_objeto(inventario, objeto, cantidad):
    # Solo intenta quitar el objeto si existe en el inventario
    if objeto in inventario:
        inventario[objeto] -= cantidad

        # Si la cantidad queda en 0 o menos, elimina el objeto del diccionario
        if inventario[objeto] <= 0:
            del inventario[objeto]

    else:
        print(f"No tienes {objeto} en el inventario.")

    return inventario


def usar_pocion(inventario):
    # Comprueba que exista la poción y que haya al menos una disponible
    if "pocion de curacion" in inventario and inventario["pocion de curacion"] > 0:
        inventario["pocion de curacion"] -= 1
        print("Has usado una poción de curación. Te sientes mejor.")

        # Si se quedan a 0, eliminamos la poción del inventario
        if inventario["pocion de curacion"] == 0:
            del inventario["pocion de curacion"]

    else:
        print("No tienes pociones de curación disponibles.")

    return inventario

def mostrar_menu():
    # Muestra las acciones disponibles del inventario
    print("Menú de inventario")
    print("------------------")
    print("1. Ver inventario")
    print("2. Añadir objeto")
    print("3. Quitar objeto")
    print("4. Usar poción")
    print("5. Salir")


def ejecutar_opcion(opcion, inventario):
    # Ejecuta una acción diferente según la opción elegida por el usuario
    if opcion == "1":
        mostrar_inventario(inventario)

    elif opcion == "2":
        objeto = input("Objeto a añadir: ").lower()
        cantidad = int(input("Cantidad a añadir: "))
        inventario = agregar_objeto(inventario, objeto, cantidad)
        mostrar_inventario(inventario)

    elif opcion == "3":
        objeto = input("Objeto a quitar: ").lower()
        cantidad = int(input("Cantidad a quitar: "))
        inventario = eliminar_objeto(inventario, objeto, cantidad)
        mostrar_inventario(inventario)

    elif opcion == "4":
        inventario = usar_pocion(inventario)
        mostrar_inventario(inventario)

    elif opcion == "5":
        print("Saliendo del inventario...")

    else:
        print("Opción no válida")

    return inventario



inventario_jugador = crear_inventario()

opcion_usuario = ""

while opcion_usuario != "5":
    mostrar_menu()

    opcion_usuario = input("Elige una opción: ")

    inventario_jugador = ejecutar_opcion(opcion_usuario, inventario_jugador)

    print()