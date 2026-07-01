inventario = {
    "pocion de curacion": 5,
    "espada": 1,
    "arco": 1,
    "flechas": 20,
    "oro": 150
}

# Recorre el diccionario y muestra el inventario inicial
for objeto, cantidad in inventario.items():
    print(f"{objeto}: {cantidad}")

# Si la clave no existe, la crea; si existe, la actualiza
inventario["escudo"] = 1

# input() devuelve texto; int() lo convierte en número para poder restarlo
flechas_usadas = int(input("¿Cuántas flechas has usado? "))

# -= resta al valor actual de "flechas"
inventario["flechas"] -= flechas_usadas

print("Inventario actualizado:")

# Recorre de nuevo el diccionario después de modificarlo
for objeto, cantidad in inventario.items():
    print(f"{objeto}: {cantidad}")