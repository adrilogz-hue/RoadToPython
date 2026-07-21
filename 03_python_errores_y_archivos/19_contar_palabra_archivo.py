palabra_buscada = input("Palabra a contar: ").lower()

contador = 0

# Abrimos el archivo en modo lectura.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    # Recorremos el archivo línea por línea.
    for linea in archivo:
        # Convertimos cada línea a minúsculas para ignorar mayúsculas/minúsculas.
        linea_minuscula = linea.lower()

        # count() cuenta cuántas veces aparece un texto dentro de otro texto.
        contador += linea_minuscula.count(palabra_buscada)

print(f"La palabra '{palabra_buscada}' aparece {contador} veces.")