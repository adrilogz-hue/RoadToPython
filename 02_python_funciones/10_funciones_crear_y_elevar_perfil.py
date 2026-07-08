def crear_perfil(nombre, ruta, horas_semana):
    # Crea y devuelve un diccionario usando los datos recibidos
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def evaluar_perfil(perfil): 
    # Lee las horas guardadas en el diccionario y devuelve una valoración
    if perfil["horas_semana"] >= 20:
        return "buen ritmo"
    elif perfil["horas_semana"] >= 10:
        return "ritmo aceptable"
    else:
        return "ritmo bajo"


nombre = input("Nombre: ")

# lower() normaliza la ruta para que "QA", "Qa" y "qa" se traten igual
ruta = input("Ruta: ").lower()

# int() convierte el texto del input en número para poder compararlo en evaluar_perfil()
horas_semana = int(input("Horas de estudio a la semana: "))

# La función devuelve un diccionario completo con los datos del usuario
perfil_usuario = crear_perfil(nombre, ruta, horas_semana)

# La función devuelve un texto según las horas del perfil
resultado = evaluar_perfil(perfil_usuario)

print(f"{perfil_usuario['nombre']} estudia {perfil_usuario['ruta']}")
print(f"Evaluación: {resultado}")