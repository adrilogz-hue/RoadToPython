def cargar_inventario():
    # Creamos un diccionario vacío.
    # Aquí iremos guardando los objetos que leamos desde el archivo.
    inventario = {}

    # Abrimos inventario.txt en modo lectura.
    with open("inventario.txt", "r", encoding="utf-8") as archivo:

        # Recorremos el archivo línea por línea.
        for linea in archivo:
            # strip() elimina el salto de línea final.
            linea = linea.strip()

            # split(":") separa el texto usando ":" como punto de corte.
            # Ejemplo: "oro:50" se convierte en ["oro", "50"].
            partes = linea.split(":")

            objeto = partes[0]
            cantidad = int(partes[1])

            inventario[objeto] = cantidad

    return inventario


def mostrar_inventario(inventario):
    print("Inventario cargado")
    print("------------------")

    for objeto, cantidad in inventario.items():
        print(f"{objeto}: {cantidad}")


inventario_jugador = cargar_inventario()

mostrar_inventario(inventario_jugador)