def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario con los datos recibidos
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def evaluar_perfil(perfil):
    # Devuelve una valoración según las horas guardadas en el perfil
    if perfil["horas_semana"] >= 20:
        return "buen ritmo"
    elif perfil["horas_semana"] >= 10:
        return "ritmo aceptable"
    else:
        return "ritmo bajo"


def mostrar_perfil(perfil, evaluacion):
    # Muestra de forma ordenada los datos del perfil y su evaluación
    print("Perfil de estudio")
    print("----------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")
    print(f"Evaluación: {evaluacion}")


nombre = input("Nombre: ")
ruta = input("Ruta: ").lower()
horas_semana = int(input("Horas de estudio a la semana: "))

perfil_usuario = crear_perfil(nombre, ruta, horas_semana)
resultado = evaluar_perfil(perfil_usuario)

mostrar_perfil(perfil_usuario, resultado)