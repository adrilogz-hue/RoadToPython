inventario = {
    "pocion de curacion": 5,
    "espada": 1,
    "arco": 1,
    "flechas": 20,
    "oro": 150
}

print("Inventario inicial:")

# items() permite recorrer el diccionario obteniendo clave y valor:
# objeto = nombre del objeto
# cantidad = cantidad disponible
for objeto, cantidad in inventario.items():
    print(f"{objeto}: {cantidad}")

# lower() normaliza la respuesta para aceptar "AÑADIR", "Añadir" o "añadir"
accion = input("¿Quieres añadir o quitar objetos? Escribe añadir/quitar: ").lower()

# Variable de control:
# empieza en True porque asumimos que la acción será válida
# si el usuario escribe algo incorrecto, la cambiaremos a False
accion_valida = True

if accion == "añadir":
    objeto = input("¿Qué objeto quieres modificar? ").lower()

    # int() convierte el texto introducido en número para poder sumar
    cantidad = int(input("¿Cuántos quieres añadir? "))

    # Si el objeto ya existe como clave del diccionario, aumentamos su cantidad
    if objeto in inventario:
        inventario[objeto] += cantidad

    # Si el objeto no existe, se crea una nueva clave con esa cantidad
    else:
        inventario[objeto] = cantidad

elif accion == "quitar":
    objeto = input("¿Qué objeto quieres modificar? ").lower()

    # int() convierte el texto introducido en número para poder restar
    cantidad = int(input("¿Cuántos quieres quitar? "))

    # Antes de restar, comprobamos que el objeto exista en el inventario
    if objeto in inventario:

        # Evita que el jugador quite más unidades de las que tiene
        if cantidad > inventario[objeto]:
            print(f"No puedes quitar más {objeto} de los que tienes.")

        else:
            # -= resta la cantidad indicada al valor actual del objeto
            inventario[objeto] -= cantidad

            # Si el objeto queda a 0, se elimina del inventario
            if inventario[objeto] == 0:
                del inventario[objeto]

    else:
        print(f"No tienes {objeto} en tu inventario.")

else:
    # Si la acción no es "añadir" ni "quitar", no tiene sentido mostrar inventario actualizado
    accion_valida = False
    print("Acción no reconocida.")

# Solo muestra el inventario final si la acción principal fue válida
if accion_valida:
    print("Inventario actualizado:")

    for objeto, cantidad in inventario.items():
        print(f"{objeto}: {cantidad}")