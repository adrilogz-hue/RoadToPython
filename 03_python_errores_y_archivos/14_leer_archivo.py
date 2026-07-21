# "r" significa read, es decir, leer.
# El archivo debe existir antes de intentar leerlo.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print("----------------------")
print(contenido)