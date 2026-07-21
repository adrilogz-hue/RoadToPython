def pedir_numero_positivo(mensaje):
    # mensaje es el texto que se mostrará en el input()
    while True:
        try:
            numero = int(input(mensaje))

            # Si el número es mayor que 0, lo aceptamos
            if numero > 0:
                return numero

            # Si llega aquí, el número era 0 o negativo
            print("Error: el número debe ser mayor que 0.")

        except ValueError:
            # ValueError ocurre si int() no puede convertir el texto en número
            print("Error: debes escribir un número.")


cantidad = pedir_numero_positivo("Cantidad: ")

print(f"Cantidad válida: {cantidad}")