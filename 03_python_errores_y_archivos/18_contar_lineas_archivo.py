contador_lineas = 0

# Abrimos el archivo en modo lectura.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    # Recorremos el archivo línea por línea.
    for linea in archivo:
        contador_lineas += 1

print(f"El archivo tiene {contador_lineas} líneas.")