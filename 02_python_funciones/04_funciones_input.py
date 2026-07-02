def mostrar_perfil(nombre, ruta, horas_semana):
    #La funcion no pide datos, solo recibe valores y los muestra
    print(f"{nombre} esta aprendiendo {ruta}")
    print(f"Estudia {horas_semana} horas a la semana")

nombre = input("Nombre: ")
ruta = input("Ruta de aprendizaje: ").lower()

#int() convierte el texto introducido en numero
horas_semana = int(input("Horas de estudio a la semana: "))

mostrar_perfil(nombre, ruta, horas_semana)
