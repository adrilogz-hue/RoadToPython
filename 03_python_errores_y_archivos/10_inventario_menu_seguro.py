def pedir_numero(mensaje):
    # Repite la pregunta hasta que el usuario escriba un número válido
    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            # ValueError aparece si int() no puede convertir el texto en número
            print("Error: debes escribir un número.")


def crear_inventario():
    # Crea el inventario inicial del personaje
    return {
        "pocion de curacion": 3,
        "espada corta": 1,
        "arco": 1,
        "flechas": 12,
        "oro": 50
    }


def mostrar_inventario(inventario):
    # Recorre el inventario y muestra cada objeto con su cantidad
    print("Inventario del personaje")
    print("------------------------")

    for objeto, cantidad in inventario.items():
        print(f"{objeto}: {cantidad}")


def agregar_objeto(inventario):
    # Pide el objeto y una cantidad segura
    objeto = input("Objeto a añadir: ").lower()
    cantidad = pedir_numero("Cantidad a añadir: ")

    if objeto in inventario:
        inventario[objeto] += cantidad
    else:
        inventario[objeto] = cantidad

    return inventario


def quitar_objeto(inventario):
    # Pide el objeto y una cantidad segura
    objeto = input("Objeto a quitar: ").lower()
    cantidad = pedir_numero("Cantidad a quitar: ")

    if objeto in inventario:
        inventario[objeto] -= cantidad

        # Si el objeto queda a 0 o menos, se elimina del inventario
        if inventario[objeto] <= 0:
            del inventario[objeto]

    else:
        print(f"No tienes {objeto} en el inventario.")

    return inventario


def usar_pocion(inventario):
    # Comprueba que exista la poción y que haya unidades disponibles
    if "pocion de curacion" in inventario and inventario["pocion de curacion"] > 0:
        inventario["pocion de curacion"] -= 1
        print("Has usado una poción de curación.")

        # Si se queda a 0, se elimina del inventario
        if inventario["pocion de curacion"] == 0:
            del inventario["pocion de curacion"]

    else:
        print("No tienes pociones de curación disponibles.")

    return inventario


def mostrar_menu():
    # Muestra las opciones disponibles del inventario
    print("Menú de inventario")
    print("------------------")
    print("1. Ver inventario")
    print("2. Añadir objeto")
    print("3. Quitar objeto")
    print("4. Usar poción")
    print("5. Salir")


def ejecutar_opcion(opcion, inventario):
    # Ejecuta una acción según la opción elegida
    if opcion == "1":
        mostrar_inventario(inventario)

    elif opcion == "2":
        inventario = agregar_objeto(inventario)
        mostrar_inventario(inventario)

    elif opcion == "3":
        inventario = quitar_objeto(inventario)
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