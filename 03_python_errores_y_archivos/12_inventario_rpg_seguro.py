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


def pedir_numero_positivo(mensaje):
    # Repite la pregunta hasta recibir un número mayor que 0.
    while True:
        numero = pedir_numero(mensaje)

        if numero > 0:
            return numero

        print("Error: la cantidad debe ser mayor que 0.")


def pedir_nombre_objeto(mensaje):
    # strip() elimina espacios al principio y al final.
    # Ejemplo: "   oro   ".strip() se convierte en "oro".
    objeto = input(mensaje).strip().lower()

    while objeto == "":
        print("Error: el nombre del objeto no puede estar vacío.")
        objeto = input(mensaje).strip().lower()

    return objeto


def crear_inventario():
    # Crea el inventario inicial del personaje.
    return {
        "pocion de curacion": 3,
        "espada corta": 1,
        "arco": 1,
        "flechas": 12,
        "oro": 50
    }


def mostrar_inventario(inventario):
    print("Inventario del personaje")
    print("------------------------")

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        for objeto, cantidad in inventario.items():
            print(f"{objeto}: {cantidad}")


def agregar_objeto(inventario):
    objeto = pedir_nombre_objeto("Objeto a añadir: ")
    cantidad = pedir_numero_positivo("Cantidad a añadir: ")

    if objeto in inventario:
        inventario[objeto] += cantidad
    else:
        inventario[objeto] = cantidad

    print(f"Has añadido {cantidad} de {objeto}.")

    return inventario


def quitar_objeto(inventario):
    objeto = pedir_nombre_objeto("Objeto a quitar: ")

    if objeto not in inventario:
        print(f"No tienes {objeto} en el inventario.")
        return inventario

    cantidad = pedir_numero_positivo("Cantidad a quitar: ")

    if cantidad > inventario[objeto]:
        print(f"No puedes quitar {cantidad} de {objeto}. Solo tienes {inventario[objeto]}.")
        return inventario

    inventario[objeto] -= cantidad

    if inventario[objeto] == 0:
        del inventario[objeto]
        print(f"Has quitado todo el objeto: {objeto}.")
    else:
        print(f"Has quitado {cantidad} de {objeto}.")

    return inventario


def usar_pocion(inventario):
    if "pocion de curacion" not in inventario:
        print("No tienes pociones de curación disponibles.")
        return inventario

    inventario["pocion de curacion"] -= 1
    print("Has usado una poción de curación.")

    if inventario["pocion de curacion"] == 0:
        del inventario["pocion de curacion"]

    return inventario


def mostrar_menu():
    print("Menú de inventario")
    print("------------------")
    print("1. Ver inventario")
    print("2. Añadir objeto")
    print("3. Quitar objeto")
    print("4. Usar poción")
    print("5. Salir")


def ejecutar_opcion(opcion, inventario):
    if opcion == "1":
        mostrar_inventario(inventario)

    elif opcion == "2":
        inventario = agregar_objeto(inventario)

    elif opcion == "3":
        inventario = quitar_objeto(inventario)

    elif opcion == "4":
        inventario = usar_pocion(inventario)

    elif opcion == "5":
        print("Saliendo del inventario...")

    else:
        print("Opción no válida.")

    return inventario


inventario_jugador = crear_inventario()
opcion_usuario = ""

while opcion_usuario != "5":
    mostrar_menu()

    opcion_usuario = input("Elige una opción: ")

    inventario_jugador = ejecutar_opcion(opcion_usuario, inventario_jugador)

    print()