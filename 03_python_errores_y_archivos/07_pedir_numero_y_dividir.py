def pedir_numero(mensaje):
    # mensaje es el texto que se mostrará en el input()
    # Ejemplo: "Primer número: " o "Segundo número: "
    while True:
        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            # ValueError ocurre si int() no puede convertir el texto en número
            print("Error: debes escribir un número.")


def dividir(numero_1, numero_2):
    # Intenta dividir dos números
    # Si numero_2 es 0, controla el error y devuelve None
    try:
        resultado = numero_1 / numero_2
        return resultado

    except ZeroDivisionError:
        # ZeroDivisionError ocurre al intentar dividir entre 0
        print("Error: no se puede dividir entre 0.")
        return None


numero_1 = pedir_numero("Primer número: ")
numero_2 = pedir_numero("Segundo número: ")

resultado = dividir(numero_1, numero_2)

# Solo mostramos el resultado si dividir() devolvió un valor válido
if resultado is not None:
    print(f"Resultado: {resultado}")