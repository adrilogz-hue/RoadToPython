persona = {
    "nombre": "Adrian",
    "edad": 30,
    "ruta": "Python"
}

# Si la clave no existe, Python la crea dentro del diccionario
persona["horas_estudio"] = 4
persona["objetivo"] = "trabajar como junior"

print(persona)

print(f"{persona['nombre']} estudia {persona['horas_estudio']} horas al día")
print(f"Objetivo: {persona['objetivo']}")