try:
    # Intentamos abrir el archivo en modo lectura.
    with open("nota.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    print("Contenido del archivo:")
    print("----------------------")
    print(contenido)

except FileNotFoundError:
    # FileNotFoundError ocurre si Python intenta abrir un archivo que no existe.
    # Ejemplo: open("archivo_inexistente.txt", "r") produce FileNotFoundError.
    print("Error: el archivo no existe.")