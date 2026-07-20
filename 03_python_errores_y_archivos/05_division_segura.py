try:
    # int() puede provocar ValueError si el usuario escribe texto
    numero_1 = int(input("Primer número: "))
    numero_2 = int(input("Segundo número: "))

    # Dividir entre 0 provoca ZeroDivisionError
    resultado = numero_1 / numero_2

    print(f"Resultado: {resultado}")

except ValueError:
    # Se ejecuta si alguno de los input no se puede convertir a número
    print("Error: debes escribir números.")

except ZeroDivisionError:
    # Se ejecuta si numero_2 vale 0
    print("Error: no se puede dividir entre 0.")