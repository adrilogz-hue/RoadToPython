def crear_perfil(nombre, ruta, horas_semana):
    # Crea un diccionario a partir de los datos recibidos
    # y lo devuelve para poder guardarlo en una variable
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


def actualizar_horas(perfil, nuevas_horas):
    # perfil representa el diccionario que recibe la función
    # nuevas_horas representa el nuevo valor que queremos guardar

    # Cambia el valor asociado a la clave "horas_semana"
    perfil["horas_semana"] = nuevas_horas

    # Devuelve el diccionario después de modificarlo
    return perfil


def mostrar_perfil(perfil):
    # Recibe un diccionario y muestra sus datos de forma ordenada
    print("Perfil actualizado")
    print("------------------")
    print(f"Nombre: {perfil['nombre']}")
    print(f"Ruta: {perfil['ruta']}")
    print(f"Horas semanales: {perfil['horas_semana']}")


# crear_perfil(...) devuelve un diccionario
# Ese diccionario se guarda en la variable perfil_usuario
perfil_usuario = crear_perfil("Adrian", "QA Automation", 20)


# actualizar_horas(...) recibe:
# - el diccionario perfil_usuario
# - el nuevo número de horas: 25
#
# La función devuelve el diccionario actualizado
# y lo guardamos otra vez en perfil_usuario
perfil_usuario = actualizar_horas(perfil_usuario, 25)


# Mostramos el diccionario ya actualizado
mostrar_perfil(perfil_usuario)