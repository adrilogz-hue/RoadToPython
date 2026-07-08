def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con los datos iniciales del usuario
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def actualizar_ruta(perfil, nueva_ruta):
    # Cambia la ruta del diccionario recibido por la nueva ruta indicada
    perfil["ruta"] = nueva_ruta
    return perfil


def mostrar_perfil(perfil):
    # Muestra los datos actuales del perfil después de los cambios
    print("Perfil actualizado")
    print("------------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


perfil_usuario = crear_perfil("Adrian", "QA Automation", 25)

nueva_ruta = input("Nueva ruta: ")

perfil_usuario = actualizar_ruta(perfil_usuario, nueva_ruta)

mostrar_perfil(perfil_usuario)