# "a" significa append, es decir, añadir al final.
# A diferencia de "w", no borra el contenido anterior del archivo.
with open("nota.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Nueva línea añadida con modo append.\n")

print("Línea añadida correctamente.")