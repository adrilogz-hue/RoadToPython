def pedir_numero(mensaje):
    # Repite la pregunta hasta que el usuario escriba un número válido
    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
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
    # Pide el objeto y la cantidad de forma segura
    objeto = input("Objeto a añadir: ").lower()
    cantidad = pedir_numero("Cantidad a añadir: ")

    if objeto in inventario:
        inventario[objeto] += cantidad
    else:
        inventario[objeto] = cantidad

    return inventario


inventario_jugador = crear_inventario()

inventario_jugador = agregar_objeto(inventario_jugador)

mostrar_inventario(inventario_jugador)