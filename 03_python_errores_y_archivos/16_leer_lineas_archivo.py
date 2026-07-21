# Abrimos el archivo en modo lectura.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    # Recorremos el archivo línea por línea.
    for linea in archivo:
        print(linea)