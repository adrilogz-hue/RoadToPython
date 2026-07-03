def evaluar_ritmo(horas_semana):
    # return permite devolver textos diferentes según la condición
    if horas_semana >= 20:
        return "buen ritmo"
    elif horas_semana >= 10:
        return "ritmo aceptable"
    else:
        return "ritmo bajo"


horas = int(input("Horas de estudio a la semana: "))

resultado = evaluar_ritmo(horas)

print(f"Resultado: {resultado}")