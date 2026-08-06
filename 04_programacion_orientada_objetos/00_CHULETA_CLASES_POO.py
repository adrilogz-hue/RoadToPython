# ============================================================
# CHULETA - PROGRAMACIÓN ORIENTADA A OBJETOS EN PYTHON
# ============================================================

# La Programación Orientada a Objetos permite crear nuestros propios tipos.
# Ejemplos:
# - Personaje
# - Inventario
# - Producto
# - Usuario
# - Coche
#
# Antes usábamos diccionarios:
#
# personaje = {
#     "nombre": "Arthas",
#     "vida": 100,
#     "nivel": 1
# }
#
# Con clases podemos crear una estructura más clara y organizada.


# ============================================================
# 1. CLASE
# ============================================================

# Una clase es una plantilla.
# Define cómo serán los objetos que creemos a partir de ella.

class Personaje:
    pass


# Aquí creamos un objeto usando la clase Personaje.
personaje_vacio = Personaje()


# ============================================================
# 2. OBJETO
# ============================================================

# Un objeto es una cosa concreta creada a partir de una clase.
#
# Clase  -> Personaje
# Objeto -> personaje_vacio

# Dicho de forma simple:
#
# class Personaje = la plantilla
# personaje_vacio = un personaje concreto creado con esa plantilla


# ============================================================
# 3. ATRIBUTOS
# ============================================================

# Los atributos son datos que pertenecen a un objeto.
# Por ejemplo:
# - nombre
# - vida
# - nivel

personaje_vacio.nombre = "Arthas"
personaje_vacio.vida = 100
personaje_vacio.nivel = 1

print(personaje_vacio.nombre)
print(personaje_vacio.vida)
print(personaje_vacio.nivel)


# ============================================================
# 4. CONSTRUCTOR __init__
# ============================================================

# __init__ es un método especial.
# Se ejecuta automáticamente cuando creamos un objeto.
#
# Sirve para dar valores iniciales al objeto.

class PersonajeConInit:
    def __init__(self, nombre, vida, nivel):
        # nombre, vida y nivel son parámetros.
        # Reciben los valores que pasamos al crear el objeto.

        # self.nombre, self.vida y self.nivel son atributos.
        # Guardan esos valores dentro del objeto concreto.
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel


personaje_1 = PersonajeConInit("Arthas", 100, 1)

print(personaje_1.nombre)
print(personaje_1.vida)
print(personaje_1.nivel)


# ============================================================
# 5. SELF
# ============================================================

# self representa el objeto concreto que está usando la clase.
#
# Si hacemos:
#
# personaje_1 = PersonajeConInit("Arthas", 100, 1)
#
# Dentro de la clase, self representa a personaje_1.
#
# Si hacemos:
#
# personaje_2 = PersonajeConInit("Jaina", 80, 3)
#
# Dentro de la clase, self representa a personaje_2.
#
# Por eso cada objeto puede tener sus propios datos.


personaje_2 = PersonajeConInit("Jaina", 80, 3)

print(personaje_1.nombre)  # Arthas
print(personaje_2.nombre)  # Jaina


# ============================================================
# 6. MÉTODOS
# ============================================================

# Un método es una función que pertenece a una clase.
#
# Las funciones normales se llaman así:
#
# mostrar_inventario(inventario)
#
# Los métodos se llaman desde un objeto:
#
# personaje.mostrar_info()

class PersonajeCompleto:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def mostrar_info(self):
        # Este método puede acceder a los atributos del objeto usando self.
        print("Información del personaje")
        print("-------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")


personaje_3 = PersonajeCompleto("Thrall", 120, 5)

personaje_3.mostrar_info()


# ============================================================
# 7. MÉTODOS QUE MODIFICAN ATRIBUTOS
# ============================================================

# Un método no solo puede mostrar información.
# También puede cambiar el estado del objeto.

class PersonajeConDanio:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Nivel: {self.nivel}")

    def recibir_danio(self, cantidad):
        # Reduce la vida del personaje.
        self.vida -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño.")


personaje_4 = PersonajeConDanio("Arthas", 100, 1)

personaje_4.mostrar_info()

personaje_4.recibir_danio(25)

personaje_4.mostrar_info()


# ============================================================
# 8. RESUMEN RÁPIDO
# ============================================================

# class Personaje:
#     Define una clase llamada Personaje.
#
# def __init__(self, nombre, vida, nivel):
#     Constructor. Se ejecuta al crear el objeto.
#
# self:
#     Representa el objeto concreto.
#
# self.nombre = nombre:
#     Guarda el parámetro nombre dentro del atributo nombre del objeto.
#
# def mostrar_info(self):
#     Método. Es una función dentro de una clase.
#
# personaje_1 = Personaje("Arthas", 100, 1):
#     Crea un objeto Personaje.
#
# personaje_1.mostrar_info():
#     Llama a un método del objeto.


# ============================================================
# 9. DIFERENCIA ENTRE DICCIONARIO Y CLASE
# ============================================================

# Con diccionario:
personaje_diccionario = {
    "nombre": "Arthas",
    "vida": 100,
    "nivel": 1
}

print(personaje_diccionario["nombre"])


# Con clase:
class PersonajeEjemplo:
    def __init__(self, nombre, vida, nivel):
        self.nombre = nombre
        self.vida = vida
        self.nivel = nivel


personaje_objeto = PersonajeEjemplo("Arthas", 100, 1)

print(personaje_objeto.nombre)


# Diferencia principal:
#
# Diccionario:
# - Guarda datos.
# - Es flexible.
# - Puede tener errores en las claves y Python no siempre avisa.
#
# Clase:
# - Crea un tipo propio.
# - Agrupa datos y acciones.
# - Organiza mejor programas grandes.