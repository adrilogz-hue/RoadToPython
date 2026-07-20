def dividir(numero_1, numero_2):
    # Esta función intenta dividir dos números
    # Si el segundo número es 0, devuelve None para indicar que no hay resultado válido
    try:
        resultado = numero_1 / numero_2
        return resultado

    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0.")
        return None


try:
    # int() puede provocar ValueError si el usuario escribe texto
    numero_1 = int(input("Primer número: "))
    numero_2 = int(input("Segundo número: "))

    resultado = dividir(numero_1, numero_2)

    # Solo mostramos el resultado si la función devolvió un valor válido
    if resultado is not None:
        print(f"Resultado: {resultado}")

except ValueError:
    # Este error se controla fuera porque ocurre al convertir los input
    print("Error: debes escribir números.")