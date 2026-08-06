class Personaje:
    def __init__(self, nombre, vida, nivel):
        # __init__ se ejecuta automáticamente al crear el objeto.
        # Guarda los datos iniciales dentro del personaje.
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def mostrar_info(self):
        # Un método es una función que pertenece a una clase.
        # self permite acceder a los atributos de este objeto concreto.
        print("Información del personaje")
        print("-------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")


personaje_1 = Personaje("Arthas", 100, 1)

personaje_1.mostrar_info()