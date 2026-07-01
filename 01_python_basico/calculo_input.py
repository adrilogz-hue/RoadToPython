horas_dia = input("¿cuantas horas estudias al dia?")
dias_semana = input("¿cuantos dias a la semana estudias?")

horas_dia = int(horas_dia)
dias_semana = int(dias_semana)

total = horas_dia * dias_semana

print(f"estudias {total} horas  a la semana")

if total >= 20:
    print("buen ritmo de estudio")

else:
    print("puedes mejorar el ritmo de estudio")