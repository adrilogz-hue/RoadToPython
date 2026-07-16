def pedir_numero(mensaje):
    # mensaje es el texto que se mostrará dentro del input()
    # Por ejemplo: "Edad: " o "Cantidad: "
    while True:
        try:
            # input(mensaje) muestra el texto recibido y espera una respuesta
            # int() intenta convertir esa respuesta en número entero
            numero = int(input(mensaje))

            # Si int() funciona, devolvemos el número y salimos de la función
            return numero

        except ValueError:
            # ValueError es el tipo de error que ocurre si int()
            # no puede convertir el texto en número.
            # Ejemplo: int("treinta") produce ValueError.
            print("Error: debes escribir un número.")


edad = pedir_numero("Edad: ")

print(f"Tienes {edad} años.")