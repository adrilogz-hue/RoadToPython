def crear_perfil(nombre, ruta, horas_semana):
    # return devuelve un diccionario construido con los datos recibidos
    return {
        "nombre": nombre,
        "ruta": ruta,
        "horas_semana": horas_semana
    }


nombre = input("Nombre: ")
ruta = input("Ruta: ").lower()
horas_semana = int(input("Horas de estudio a la semana: "))

perfil = crear_perfil(nombre, ruta, horas_semana)

print(f"{perfil['nombre']} estudia {perfil['ruta']}")
print(f"Horas semanales: {perfil['horas_semana']}")