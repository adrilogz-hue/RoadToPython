def mostrar_menu():
    # Muestra las opciones disponibles para el usuario
    print("Menú principal")
    print("--------------")
    print("1. Ver perfil")
    print("2. Actualizar ruta")
    print("3. Actualizar horas")


def ejecutar_opcion(opcion):
    # Ejecuta una acción diferente según la opción elegida
    if opcion == "1":
        print("Mostrando perfil...")
    elif opcion == "2":
        print("Actualizando ruta...")
    elif opcion == "3":
        print("Actualizando horas...")
    else:
        print("Opción no válida")


mostrar_menu()

opcion_usuario = input("Elige una opción: ")

ejecutar_opcion(opcion_usuario)