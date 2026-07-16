def pedir_numero(mensaje):
    # mensaje permite reutilizar esta función con preguntas distintas
    # Ejemplo: "Horas de estudio al día: " o "Días de estudio a la semana: "
    while True:
        try:
            # input(mensaje) pide el dato usando el texto recibido
            # int() intenta convertir la respuesta a número entero
            numero = int(input(mensaje))

            # Si la conversión funciona, return devuelve el número
            # y termina la función
            return numero

        except ValueError:
            # Captura el error concreto que aparece cuando int()
            # no puede convertir el texto a número.
            print("Error: debes escribir un número.")


horas_dia = pedir_numero("Horas de estudio al día: ")
dias_semana = pedir_numero("Días de estudio a la semana: ")

horas_semana = horas_dia * dias_semana

print(f"Estudias {horas_semana} horas a la semana.")