def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con la estructura que usaremos como perfil
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def mostrar_menu():
    # Esta función solo muestra las opciones disponibles
    # Se llamará cada vez que el while repita el menú
    print("Menú principal")
    print("--------------")
    print("1. Ver perfil")
    print("2. Actualizar ruta")
    print("3. Actualizar horas")
    print("4. Salir")


def mostrar_perfil(perfil):
    # Recibe el diccionario del perfil y muestra sus datos actuales
    print("Perfil de usuario")
    print("-----------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


def actualizar_ruta(perfil):
    # Pide una nueva ruta y modifica la clave "ruta" del diccionario recibido
    nueva_ruta = input("Ingresa la nueva ruta: ")
    perfil["ruta"] = nueva_ruta
    return perfil


def actualizar_horas(perfil):
    # Pide nuevas horas y las convierte a número entero
    # porque las horas deberían guardarse como número, no como texto
    nuevas_horas = int(input("Ingresa las nuevas horas semanales: "))

    # Actualiza la clave "horas_semana" del diccionario recibido
    perfil["horas_semana"] = nuevas_horas
    return perfil


def ejecutar_opcion(opcion, perfil):
    # Esta función recibe:
    # - opcion: lo que el usuario escribió en el menú
    # - perfil: el diccionario actual del usuario
    #
    # Según la opción, llama a una función distinta.

    if opcion == "1":
        mostrar_perfil(perfil)

    elif opcion == "2":
        # actualizar_ruta() devuelve el perfil modificado
        perfil = actualizar_ruta(perfil)
        mostrar_perfil(perfil)

    elif opcion == "3":
        # actualizar_horas() devuelve el perfil modificado
        perfil = actualizar_horas(perfil)
        mostrar_perfil(perfil)

    elif opcion == "4":
        # Cuando el usuario elige 4, el while dejará de repetirse
        print("Saliendo del programa...")

    else:
        print("Opción no válida")

    # Devolvemos el perfil para conservar cualquier cambio hecho
    return perfil


# Creamos el perfil inicial antes de empezar el menú
perfil_usuario = crear_perfil("Adrian", "QA Automation", 22)

# Esta variable guarda la opción elegida por el usuario
# Empieza vacía para que el while pueda arrancar
opcion_usuario = ""

# Mientras la opción elegida NO sea "4", el menú se repetirá
while opcion_usuario != "4":
    mostrar_menu()

    # input() devuelve texto, por eso comparamos con "1", "2", "3" y "4"
    opcion_usuario = input("Elige una opción: ")

    # ejecutar_opcion() puede modificar el perfil
    # Por eso guardamos el resultado otra vez en perfil_usuario
    perfil_usuario = ejecutar_opcion(opcion_usuario, perfil_usuario)

    # Línea vacía para separar visualmente cada vuelta del menú
    print()