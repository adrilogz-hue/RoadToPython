def evaluar_perfil(perfil):
    # Accede al valor "horas_semana" del diccionario para tomar una decisión
    if perfil["horas_semana"] >= 20:
        return "buen ritmo"
    elif perfil["horas_semana"] >= 10:
        return "ritmo aceptable"
    else:
        return "ritmo bajo"


perfil_usuario = {
    "nombre": "Adrian",
    "ruta": "QA Automation",
    "horas_semana": 25
}

resultado = evaluar_perfil(perfil_usuario)

print(f"{perfil_usuario['nombre']} tiene {resultado}")