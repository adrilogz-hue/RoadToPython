# lower() normaliza la respuesta para aceptar "SI", "Si", "si", etc.
trabajando = input("¿Estás trabajando actualmente? si/no: ").lower()

# == compara texto; devuelve True si la respuesta es exactamente "si"
esta_trabajando = trabajando == "si"

# not invierte el valor booleano:
# si esta_trabajando es False, not esta_trabajando será True
if not esta_trabajando:
    print("Tienes más disponibilidad para estudiar")
else:
    print("Habrá que organizar mejor el tiempo de estudio")