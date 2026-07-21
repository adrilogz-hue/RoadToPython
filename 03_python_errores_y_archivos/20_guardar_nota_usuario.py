nota = input("Escribe una nota: ")

# "a" significa append: añade contenido al final del archivo sin borrar lo anterior.
with open("nota.txt", "a", encoding="utf-8") as archivo:
    archivo.write(nota + "\n")

print("Nota guardada correctamente.")