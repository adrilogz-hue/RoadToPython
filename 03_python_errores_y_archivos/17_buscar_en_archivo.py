palabra_buscada = input("Palabra a buscar: ").lower()

encontrado = False

# Leemos el archivo línea por línea para revisar cada línea por separado.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # Convertimos la línea a minúsculas para que la búsqueda no dependa de mayúsculas.
        if palabra_buscada in linea.lower():
            print("Línea encontrada:")
            print(linea.strip())
            encontrado = True

if encontrado == False:
    print("No se encontró la palabra en el archivo.")