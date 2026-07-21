def crear_inventario():
    # Crea el inventario inicial del personaje.
    return {
        "pocion de curacion": 3,
        "espada corta": 1,
        "arco": 1,
        "flechas": 12,
        "oro": 50
    }


def guardar_inventario(inventario):
    # Abre el archivo en modo escritura.
    # Si inventario.txt no existe, Python lo crea.
    # Si ya existe, borra su contenido anterior y escribe el inventario actual.
    with open("inventario.txt", "w", encoding="utf-8") as archivo:

        # Recorremos el diccionario para guardar cada objeto y su cantidad.
        for objeto, cantidad in inventario.items():
            archivo.write(f"{objeto}:{cantidad}\n")

    print("Inventario guardado correctamente.")


inventario_jugador = crear_inventario()

guardar_inventario(inventario_jugador)