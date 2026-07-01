persona = {
    "nombre": "Adrian",
    "edad": 30,
    "ruta": "Python"
}

# Accedemos al valor original usando la clave "ruta"
print(f"Ruta inicial: {persona['ruta']}")

# Si asignamos un nuevo valor a una clave existente, el valor se actualiza
persona["ruta"] = "Data e IA"

print(f"Ruta actualizada: {persona['ruta']}")