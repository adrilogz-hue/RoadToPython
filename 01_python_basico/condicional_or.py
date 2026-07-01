# lower() evita problemas si el usuario escribe "Data", "DATA" o "data"
ruta = input("¿Que ruta te interesa más? data, qa o backend?:").lower()

# or permite aceptar varias respuestas como válidas
if ruta == "data" or ruta == "qa":
    print("Ruta muy útil para entrar en consultoría tecnológica")
elif ruta == "backend":
    print("Ruta útil, especialmente si trabajas con APIs o automatización")
else:
    print("Ruta no reconocida")