while True:
    try:
        # Intentamos convertir el input en número
        edad = int(input("Edad: "))

        print(f"Tienes {edad} años.")

        # Si no hubo error, salimos del bucle
        break

    except ValueError:
        # Si el usuario escribe texto no numérico, mostramos error
        # y el while vuelve a pedir la edad
        print("Error: debes escribir un número.")