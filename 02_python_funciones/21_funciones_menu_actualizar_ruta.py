def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con los datos iniciales del usuario
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def mostrar_menu():
    # Muestra las opciones disponibles del programa
    print("Menú principal")
    print("--------------")
    print("1. Ver perfil")
    print("2. Actualizar ruta")
    print("3. Actualizar horas")


def mostrar_perfil(perfil):
    # Recibe el diccionario del perfil y muestra sus datos
    print("Perfil de usuario")
    print("-----------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


def ejecutar_opcion(opcion, perfil):
    # Según la opción elegida, ejecuta una acción usando el perfil recibido
    if opcion == "1":
        mostrar_perfil(perfil)
    elif opcion == "2":
        perfil = actualizar_ruta(perfil)
        mostrar_perfil(perfil)
    elif opcion == "3":
        perfil = actualizar_horas(perfil)
        mostrar_perfil(perfil)
    else:
        print("Opción no válida")

def actualizar_ruta(perfil):
    nueva_ruta = input("Ingresa la nueva ruta: ")
    perfil["ruta"] = nueva_ruta
    return perfil

def actualizar_horas(perfil):
    nuevas_horas = int(input("Ingresa las nuevas horas semanales: "))
    perfil["horas_semana"] = nuevas_horas
    return perfil

perfil_usuario = crear_perfil("Adrian", "QA Automation", 22)

mostrar_menu()

opcion_usuario = input("Elige una opción: ")

ejecutar_opcion(opcion_usuario, perfil_usuario) 