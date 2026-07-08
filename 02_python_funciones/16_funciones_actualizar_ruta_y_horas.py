def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con los datos iniciales del usuario
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def actualizar_ruta(perfil, nueva_ruta):
    # Cambia la ruta del perfil por el nuevo valor recibido
    perfil["ruta"] = nueva_ruta
    return perfil


def actualizar_horas(perfil, nuevas_horas):
    # Cambia las horas semanales del perfil por el nuevo valor recibido
    perfil["horas_semana"] = nuevas_horas
    return perfil


def mostrar_perfil(perfil):
    # Muestra el estado actual del perfil después de las actualizaciones
    print("Perfil actualizado")
    print("------------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


perfil_usuario = crear_perfil("Adrian", "QA Automation", 20)

nueva_ruta = input("Nueva ruta: ")
nuevas_horas = int(input("Nuevas horas semanales: "))

perfil_usuario = actualizar_ruta(perfil_usuario, nueva_ruta)
perfil_usuario = actualizar_horas(perfil_usuario, nuevas_horas)

mostrar_perfil(perfil_usuario)