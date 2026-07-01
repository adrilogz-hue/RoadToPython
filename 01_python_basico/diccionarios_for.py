persona = {
    "nombre": "Adrian",
    "edad": 30,
    "ruta": "Python",
    "horas_estudio": 4,
    "objetivo": "trabajar como junior"
}

# items() permite recorrer clave y valor al mismo tiempo
for clave, valor in persona.items():
    print(f"{clave}: {valor}")