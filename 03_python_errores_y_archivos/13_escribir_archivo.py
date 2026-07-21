# "w" significa write, es decir, escribir.
# Si el archivo no existe, Python lo crea.
# Si el archivo ya existe, Python borra su contenido anterior y escribe el nuevo.
with open("nota.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera nota guardada desde Python.\n")
    archivo.write("Estoy aprendiendo a trabajar con archivos.\n")

print("Archivo creado correctamente.")