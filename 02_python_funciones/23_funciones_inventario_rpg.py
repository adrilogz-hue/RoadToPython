def crear_inventario():
    # Crea un diccionario vacío para el inventario
    #Cada clave es un objeto y cada valor es la cantidad disponible
    return {
        "pocion de curacion": 3,
           "espada corta": 1,
            "arco": 1,
            "flechas": 12,
            "oro": 50
            }

def mostrar_inventario(inventario):
    # Recibe el diccionario del inventario y muestra sus datos actuales
    print("inventario del personaje")
    print("-----------------")

    for objeto,cantidad in inventario.items():
        print(f"{objeto}: {cantidad}")


inventario_jugador = crear_inventario()

mostrar_inventario(inventario_jugador)

