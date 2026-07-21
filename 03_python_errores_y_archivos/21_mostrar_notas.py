contador = 1

print("Notas guardadas")
print("---------------")

# Abrimos el archivo en modo lectura.
with open("nota.txt", "r", encoding="utf-8") as archivo:
    # Recorremos el archivo línea por línea.
    for linea in archivo:
        # strip() elimina el salto de línea final para que print() no añada líneas en blanco extra.
        nota = linea.strip()

        print(f"{contador}. {nota}")

        contador += 1