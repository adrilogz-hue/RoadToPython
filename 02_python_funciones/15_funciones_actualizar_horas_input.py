def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con los datos iniciales del usuario
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def actualizar_horas(perfil, nuevas_horas):
    # Cambia las horas semanales del diccionario recibido
    perfil["horas_semana"] = nuevas_horas
    return perfil


def mostrar_perfil(perfil):
    # Muestra los datos actuales del perfil después de los cambios
    print("Perfil actualizado")
    print("------------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


perfil_usuario = crear_perfil("Adrian", "QA Automation", 20)

# int() convierte el input en número para guardar horas como entero
nuevas_horas = int(input("Nuevas horas semanales: "))

perfil_usuario = actualizar_horas(perfil_usuario, nuevas_horas)

mostrar_perfil(perfil_usuario)