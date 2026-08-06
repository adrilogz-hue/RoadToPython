class Personaje:
    def __init__(self, nombre, vida, nivel):
        # __init__ se ejecuta automáticamente al crear un objeto.
        # Sirve para dar valores iniciales a sus atributos.

        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel


personaje_1 = Personaje("Arthas", 100, 1)

print(f"Nombre: {personaje_1.nombre}")
print(f"Vida: {personaje_1.vida}")
print(f"Nivel: {personaje_1.nivel}")