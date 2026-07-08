def validar_ruta(ruta):
    # Lista de rutas aceptadas por el programa
    rutas_validas = ["python", "qa", "data", "backend"]

    # Comprueba si la ruta recibida está dentro de la lista
    if ruta in rutas_validas:
        return True
    else:
        return False


ruta_usuario = input("Ruta: ").lower()

ruta_valida = validar_ruta(ruta_usuario)

if ruta_valida:
    print("Ruta válida")
else:
    print("Ruta no válida")