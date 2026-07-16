try:
    # Intentamos convertir el texto del input en número entero
    edad = int(input("Edad: "))

    print(f"Tienes {edad} años.")

except ValueError:
    # Este bloque se ejecuta si int() no puede convertir el texto en número
    print("Error: debes escribir un número.")