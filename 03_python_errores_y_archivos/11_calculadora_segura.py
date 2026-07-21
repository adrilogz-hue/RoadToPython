def pedir_numero(mensaje):
    # Repite la pregunta hasta que el usuario escriba un número válido.
    while True:
        try:
            numero = float(input(mensaje))
            return numero

        except ValueError:
            # ValueError ocurre si float() no puede convertir el texto en número.
            # Ejemplo: float("dos") produce ValueError.
            print("Error: debes escribir un número.")


def sumar(numero_1, numero_2):
    return numero_1 + numero_2


def restar(numero_1, numero_2):
    return numero_1 - numero_2


def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2


def dividir(numero_1, numero_2):
    try:
        resultado = numero_1 / numero_2
        return resultado

    except ZeroDivisionError:
        # ZeroDivisionError ocurre si intentamos dividir entre 0.
        print("Error: no se puede dividir entre cero.")
        return None


def mostrar_menu():
    print("Calculadora segura")
    print("------------------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def ejecutar_operacion(opcion):
    if opcion == "1":
        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")
        resultado = sumar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "2":
        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")
        resultado = restar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "3":
        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")
        resultado = multiplicar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "4":
        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")
        resultado = dividir(numero_1, numero_2)

        if resultado is not None:
            print(f"Resultado: {resultado}")

    elif opcion == "5":
        print("Saliendo de la calculadora...")

    else:
        print("Opción no válida.")


opcion_usuario = ""

while opcion_usuario != "5":
    mostrar_menu()

    opcion_usuario = input("Elige una opción: ")

    ejecutar_operacion(opcion_usuario)

    print()
    