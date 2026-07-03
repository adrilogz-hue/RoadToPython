def mostrar_perfil(perfil):
    # La función recibe un diccionario completo como parámetro
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


perfil_usuario = {
    "nombre": "Adrian",
    "ruta": "QA Automation",
    "horas_semana": 20
}

mostrar_perfil(perfil_usuario)