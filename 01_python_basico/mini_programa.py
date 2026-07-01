nombre = input("Nombre: ")
horas_semana = input("Horas de estudio por semana: ")
ruta = input("Ruta de aprendizaje: data, qa o backend: ").lower()

horas_semana = int(horas_semana) 

perfil = {
    "nombre": nombre,
    "horas_semana": horas_semana,
    "ruta": ruta
}

rutas_validas = ["data", "qa", "backend"]

if ruta not in rutas_validas:
     print("Ruta no válida")
elif horas_semana >= 20:
     print ("buen ritmo de estudio")
elif horas_semana >= 10: 
     print ("ritmo de estudio aceptable")
else: 
     print("Ritmo de estudio bajo")

if ruta in rutas_validas:
    print(f"{perfil['nombre']} está aprendiendo {perfil['ruta']} y estudia {perfil['horas_semana']} horas por semana")
else: 
    print("No se puede mostrar el perfil debido a una ruta no válida")