persona = {
    "nombre": "Adrian",
    "edad": 30,
    "ruta": "Python"
}

# Accedemos a un valor usando su clave
print(persona["nombre"])
print(persona["edad"])
print(persona["ruta"])

# f-string permite mezclar texto con valores del diccionario
print(f"{persona['nombre']} está aprendiendo {persona['ruta']}")