# input() devuelve texto, aunque el usuario escriba un número
horas = input("¿Cuántas horas estudias a la semana? ")

# lower() normaliza la respuesta para aceptar "SI", "Si", "si", etc.
ingles = input("¿Tienes nivel básico de inglés? si/no: ").lower()

# int() convierte "20" en 20 para poder comparar con >=
horas = int(horas)

# and solo devuelve True si las dos condiciones se cumplen
if horas >= 15 and ingles == "si":
    print("Buen perfil para empezar a prepararte para consultoría")
else:
    print("Hay que reforzar el perfil")