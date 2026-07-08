def crear_perfil(nombre, ruta, horas_semana): 
    # Crea un diccionario a partir de los iniciales del usuario
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana    
    }

def actualizar_ruta(perfil, nueva_ruta):
    # perfil representa el diccionario que recibe la función
    # nueva_ruta representa el nuevo valor que queremos guardar

    # Cambia el valor asociado a la clave "ruta"
    perfil["ruta"] = nueva_ruta

    # Devuelve el diccionario después de modificarlo
    return perfil

def mostrar_perfil(perfil):
    # Recibe un diccionario y muestra sus datos de forma ordenada
    print("Perfil actualizado")
    print("------------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


perfil_usuario = crear_perfil("Adrian", "QA Automation", 25)

perfil_usuario = actualizar_ruta(perfil_usuario, "python_backend")

mostrar_perfil(perfil_usuario)