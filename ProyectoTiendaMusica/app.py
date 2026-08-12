# Importamos json para leer y escribir los pedidos en un archivo.
import json
from pathlib import Path

# Importamos Flask, que es la clase principal para crear la aplicación web.
# jsonify nos permite devolver respuestas en formato JSON.
# request nos permite acceder a los datos enviados por el cliente,
# por ejemplo el JSON de un POST o los parámetros de una URL.
from flask import Flask, jsonify, request

# Creamos la aplicación Flask.
# __name__ le indica a Flask cuál es el módulo actual
# y le ayuda a localizar recursos de la aplicación.
app = Flask(__name__)


# Archivo donde se almacenan los pedidos.
ARCHIVO_PEDIDOS = Path(__file__).with_name("pedidos.json")


# Cargamos los pedidos al iniciar la aplicación.
with ARCHIVO_PEDIDOS.open("r", encoding="utf-8") as archivo:
    pedidos = json.load(archivo)


def guardar_pedidos():
    """Guarda los pedidos actuales en el archivo JSON."""
    with ARCHIVO_PEDIDOS.open("w", encoding="utf-8") as archivo:
        json.dump(pedidos, archivo, ensure_ascii=False, indent=4)


# =========================================================
# FUNCIÓN AUXILIAR
# =========================================================

def buscar_pedido(pedido_id):
    """
    Busca un pedido por su ID.

    Recibe:
        pedido_id: ID numérico del pedido.

    Devuelve:
        El diccionario del pedido si existe.
        None si no encuentra ningún pedido.
    """

    # Recorremos todos los pedidos almacenados en la lista.
    for pedido in pedidos:

        # Comprobamos si el ID del pedido actual coincide
        # con el ID que estamos buscando.
        if pedido["id"] == pedido_id:

            # Si coincide, devolvemos ese pedido.
            # En cuanto usamos return, la función termina.
            return pedido

    # Si hemos recorrido toda la lista y no hemos encontrado
    # ningún pedido con ese ID, devolvemos None.
    return None


def validar_cliente(cliente):
    """Valida la estructura del cliente de un pedido."""
    if not isinstance(cliente, dict):
        return False, "El cliente debe ser un objeto JSON"

    campos_obligatorios = ["id", "nombre", "email"]
    for campo in campos_obligatorios:
        if campo not in cliente:
            return False, f"Falta el campo obligatorio del cliente: {campo}"

    if not isinstance(cliente["id"], int):
        return False, "El id del cliente debe ser un número entero"

    if not isinstance(cliente["nombre"], str) or not cliente["nombre"].strip():
        return False, "El nombre del cliente debe ser una cadena no vacía"

    email = cliente["email"]
    if not isinstance(email, str) or "@" not in email or "." not in email.split("@")[-1]:
        return False, "El email del cliente no tiene un formato válido"

    return True, None


def validar_direccion(direccion):
    """Valida la dirección de envío de un pedido."""
    if not isinstance(direccion, dict):
        return False, "La dirección de envío debe ser un objeto JSON"

    campos_obligatorios = ["calle", "ciudad", "codigo_postal", "pais"]
    for campo in campos_obligatorios:
        if campo not in direccion:
            return False, f"Falta el campo obligatorio de la dirección: {campo}"

        valor = direccion[campo]
        if not isinstance(valor, str) or not valor.strip():
            return False, f"El campo '{campo}' de la dirección debe ser una cadena no vacía"

    if len(direccion["codigo_postal"].strip()) < 3:
        return False, "El código postal debe tener al menos 3 caracteres"

    return True, None


def validar_producto(producto):
    """Valida un producto dentro de un pedido."""
    if not isinstance(producto, dict):
        return False, "Cada producto debe ser un objeto JSON"

    campos_obligatorios = ["id", "nombre", "categoria", "cantidad", "precio_unitario"]
    for campo in campos_obligatorios:
        if campo not in producto:
            return False, f"Falta el campo obligatorio del producto: {campo}"

    if not isinstance(producto["id"], int):
        return False, "El id del producto debe ser un número entero"

    if not isinstance(producto["nombre"], str) or not producto["nombre"].strip():
        return False, "El nombre del producto debe ser una cadena no vacía"

    if not isinstance(producto["categoria"], str) or not producto["categoria"].strip():
        return False, "La categoría del producto debe ser una cadena no vacía"

    if not isinstance(producto["cantidad"], int) or producto["cantidad"] <= 0:
        return False, "La cantidad del producto debe ser un entero mayor que cero"

    precio = producto["precio_unitario"]
    if not isinstance(precio, (int, float)) or precio < 0:
        return False, "El precio unitario del producto debe ser un número mayor o igual a cero"

    return True, None


def validar_pedido(datos, require_all=True):
    """Valida los datos completos o parciales de un pedido."""
    if not isinstance(datos, dict):
        return False, "Los datos del pedido deben ser un objeto JSON"

    campos_obligatorios = [
        "cliente",
        "estado",
        "fecha",
        "direccion_envio",
        "productos",
        "metodo_pago"
    ]

    campos_permitidos = set(campos_obligatorios)

    if require_all:
        for campo in campos_obligatorios:
            if campo not in datos:
                return False, f"Falta el campo obligatorio: {campo}"

    for campo in datos:
        if campo not in campos_permitidos:
            return False, f"No se puede procesar el campo desconocido: {campo}"

    if "cliente" in datos:
        valido, mensaje = validar_cliente(datos["cliente"])
        if not valido:
            return False, mensaje

    if "direccion_envio" in datos:
        valido, mensaje = validar_direccion(datos["direccion_envio"])
        if not valido:
            return False, mensaje

    if "productos" in datos:
        if not isinstance(datos["productos"], list) or not datos["productos"]:
            return False, "Productos debe ser una lista no vacía"
        for producto in datos["productos"]:
            valido, mensaje = validar_producto(producto)
            if not valido:
                return False, mensaje

    if "estado" in datos:
        if not isinstance(datos["estado"], str) or not datos["estado"].strip():
            return False, "El estado del pedido debe ser una cadena no vacía"

    if "fecha" in datos:
        if not isinstance(datos["fecha"], str) or not datos["fecha"].strip():
            return False, "La fecha del pedido debe ser una cadena no vacía"

    if "metodo_pago" in datos:
        if not isinstance(datos["metodo_pago"], str) or not datos["metodo_pago"].strip():
            return False, "El método de pago debe ser una cadena no vacía"

    return True, None


# =========================================================
# GET /
# =========================================================

# @app.route sirve para asociar una URL con una función.
#
# En este caso:
#
# URL:
# /
#
# Método permitido:
# GET
#
# Por ejemplo:
# http://localhost:5000/
@app.route("/", methods=["GET"])
def inicio():

    # Devolvemos información básica sobre nuestra API.
    #
    # jsonify convierte automáticamente este diccionario
    # de Python a JSON.
    return jsonify({
        "servicio": "API de pedidos",
        "version": "1.0",

        # Incluimos una pequeña documentación de los endpoints
        # disponibles en nuestra API.
        "endpoints": {
            "GET /pedidos":
                "Obtener todos los pedidos o filtrarlos por estado y categoría",

            "GET /pedidos/<id>":
                "Obtener un pedido concreto",

            "GET /clientes/<id>/pedidos":
                "Obtener pedidos de un cliente",

            "POST /pedidos":
                "Crear un pedido",

            "PUT /pedidos/<id>":
                "Modificar completamente un pedido",

            "PATCH /pedidos/<id>":
                "Modificar parcialmente un pedido",

            "DELETE /pedidos/<id>":
                "Eliminar un pedido"
        }
    })


# =========================================================
# GET /pedidos
# =========================================================

# Este endpoint permite obtener todos los pedidos.
#
# Ejemplo:
#
# GET http://localhost:5000/pedidos
#
# También permite filtrar por estado:
#
# GET http://localhost:5000/pedidos?estado=enviado
#
# También permite filtrar por categoría de producto:
#
# GET http://localhost:5000/pedidos?categoria=audio
@app.route("/pedidos", methods=["GET"])
def obtener_pedidos():

    # request.args permite acceder a los parámetros
    # enviados en la URL.
    #
    # Por ejemplo:
    #
    # /pedidos?estado=enviado
    #
    # request.args.get("estado")
    #
    # devolvería:
    #
    # "enviado"
    estado = request.args.get("estado")
    categoria = request.args.get("categoria")

    # Comprobamos si el usuario ha enviado algún filtro.
    if estado or categoria:

        # Creamos una nueva lista únicamente con los pedidos
        # cuyo estado coincida con el estado solicitado.
        #
        # Esto es una list comprehension.
        pedidos_filtrados = [
            pedido
            for pedido in pedidos

            # El estado debe coincidir si se ha solicitado.
            # La categoría coincide si aparece en alguno de los productos.
            # Usamos lower() para ignorar mayúsculas y minúsculas.
            if (
                (not estado or pedido["estado"].lower() == estado.lower())
                and (
                    not categoria
                    or any(
                        producto["categoria"].lower() == categoria.lower()
                        for producto in pedido["productos"]
                    )
                )
            )
        ]

        # Devolvemos los pedidos filtrados en formato JSON.
        return jsonify(pedidos_filtrados)

    # Si no se ha enviado ningún filtro,
    # devolvemos todos los pedidos.
    return jsonify(pedidos)


# =========================================================
# GET /pedidos/<id>
# =========================================================

# Este endpoint devuelve los detalles de un pedido concreto.
#
# <int:pedido_id> significa:
#
# Flask espera recibir un número entero en esa parte de la URL
# y lo guardará en la variable pedido_id.
#
# Ejemplo:
#
# GET /pedidos/1
#
# pedido_id tendrá el valor:
#
# 1
@app.route("/pedidos/<int:pedido_id>", methods=["GET"])
def obtener_pedido(pedido_id):

    # Utilizamos nuestra función auxiliar para buscar
    # el pedido correspondiente.
    pedido = buscar_pedido(pedido_id)

    # Si buscar_pedido devuelve None significa
    # que no existe ningún pedido con ese ID.
    if pedido is None:

        # Devolvemos un mensaje de error.
        #
        # El segundo valor del return:
        #
        # 404
        #
        # es el código HTTP.
        #
        # 404 significa "Not Found".
        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    # Si hemos encontrado el pedido,
    # lo devolvemos en formato JSON.
    #
    # Flask devolverá por defecto código HTTP 200.
    return jsonify(pedido)


# =========================================================
# GET /clientes/<id>/pedidos
# =========================================================

# Este endpoint permite consultar todos los pedidos
# pertenecientes a un cliente concreto.
#
# Ejemplo:
#
# GET /clientes/101/pedidos
@app.route("/clientes/<int:cliente_id>/pedidos", methods=["GET"])
def obtener_pedidos_cliente(cliente_id):

    # Creamos una lista con todos los pedidos cuyo
    # cliente tenga el ID solicitado.
    pedidos_cliente = [
        pedido
        for pedido in pedidos
        if pedido["cliente"]["id"] == cliente_id
    ]

    # Una lista vacía en Python se considera False.
    #
    # Por eso:
    #
    # if not pedidos_cliente:
    #
    # significa:
    #
    # "si no hemos encontrado ningún pedido".
    if not pedidos_cliente:

        # Devolvemos error 404.
        return jsonify({
            "error": "No se encontraron pedidos para ese cliente"
        }), 404

    # Si hemos encontrado pedidos,
    # devolvemos la lista en formato JSON.
    return jsonify(pedidos_cliente)


# =========================================================
# POST /pedidos
# =========================================================

# POST se utiliza para crear nuevos recursos.
#
# En nuestro caso sirve para crear un nuevo pedido.
#
# El cliente debe enviar los datos del pedido
# en el body de la petición utilizando JSON.
@app.route("/pedidos", methods=["POST"])
def crear_pedido():

    # request.get_json() obtiene el JSON enviado
    # en el cuerpo de la petición.
    #
    # Flask lo convierte automáticamente
    # en un diccionario de Python.
    datos = request.get_json()

    # Comprobamos que realmente se hayan enviado datos.
    if not datos:

        # 400 significa Bad Request.
        #
        # Se utiliza cuando la petición que ha realizado
        # el cliente no es válida.
        return jsonify({
            "error": "Debes enviar los datos del pedido en formato JSON"
        }), 400

    valido, mensaje = validar_pedido(datos)
    if not valido:
        return jsonify({"error": mensaje}), 400

    # Ahora necesitamos generar un ID para el nuevo pedido.
    #
    # Esta expresión obtiene el ID más alto existente.
    #
    # Por ejemplo, si tenemos:
    #
    # 1
    # 2
    # 3
    #
    # max() devolverá 3.
    #
    # Después sumamos 1.
    #
    # El nuevo ID será 4.
    nuevo_id = max(
        (pedido["id"] for pedido in pedidos),
        default=0
    ) + 1

    # Inicializamos el precio total del pedido en 0.
    total = 0

    # Recorremos todos los productos enviados
    # en el pedido.
    for producto in datos["productos"]:

        # Calculamos:
        #
        # cantidad * precio unitario
        #
        # y lo acumulamos en total.
        total += (
            producto["cantidad"]
            * producto["precio_unitario"]
        )

    # Construimos el nuevo pedido como un diccionario.
    nuevo_pedido = {

        # ID generado por el servidor.
        "id": nuevo_id,

        # Información del cliente.
        "cliente": datos["cliente"],

        # Estado inicial del pedido.
        "estado": datos["estado"],

        # Fecha del pedido.
        "fecha": datos["fecha"],

        # Dirección de envío.
        "direccion_envio": datos["direccion_envio"],

        # Lista de productos.
        "productos": datos["productos"],

        # Método utilizado para pagar.
        "metodo_pago": datos["metodo_pago"],

        # round(total, 2) redondea el total
        # a dos decimales.
        "total": round(total, 2)
    }

    # Añadimos el nuevo pedido a nuestra lista
    # de pedidos.
    pedidos.append(nuevo_pedido)
    guardar_pedidos()

    # Devolvemos el pedido recién creado.
    #
    # 201 significa:
    #
    # Created
    #
    # y es el código HTTP habitual cuando se crea
    # correctamente un recurso.
    return jsonify(nuevo_pedido), 201


# =========================================================
# PUT /pedidos/<id>
# =========================================================

# PUT se utiliza normalmente para sustituir completamente
# un recurso existente.
#
# Ejemplo:
#
# PUT /pedidos/1
#
# Aquí esperamos recibir todos los datos del pedido.
@app.route("/pedidos/<int:pedido_id>", methods=["PUT"])
def modificar_pedido(pedido_id):

    # Buscamos el pedido existente.
    pedido = buscar_pedido(pedido_id)

    # Si no existe, devolvemos 404.
    if pedido is None:

        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    # Obtenemos el JSON enviado por el cliente.
    datos = request.get_json()

    # Comprobamos que se hayan enviado datos.
    if not datos:

        return jsonify({
            "error": "No se han enviado datos"
        }), 400

    valido, mensaje = validar_pedido(datos)
    if not valido:
        return jsonify({"error": mensaje}), 400

    # Calculamos nuevamente el precio total
    # de todos los productos.
    #
    # En este caso utilizamos sum() junto con
    # una expresión generadora.
    total = sum(
        producto["cantidad"] * producto["precio_unitario"]
        for producto in datos["productos"]
    )

    # clear() elimina todo el contenido
    # actual del diccionario pedido.
    #
    # El diccionario sigue existiendo,
    # pero queda vacío.
    pedido.clear()

    # update() añade al diccionario
    # todos los nuevos valores.
    pedido.update({

        # Conservamos el ID original.
        "id": pedido_id,

        "cliente": datos["cliente"],

        "estado": datos["estado"],

        "fecha": datos["fecha"],

        "direccion_envio": datos["direccion_envio"],

        "productos": datos["productos"],

        "metodo_pago": datos["metodo_pago"],

        "total": round(total, 2)
    })

    guardar_pedidos()

    # Devolvemos el pedido actualizado.
    return jsonify(pedido)


# =========================================================
# PATCH /pedidos/<id>
# =========================================================

# PATCH permite modificar solamente algunos campos
# de un recurso.
#
# Esta es la diferencia principal con PUT.
#
# Por ejemplo:
#
# PATCH /pedidos/1
#
# JSON:
#
# {
#     "estado": "entregado"
# }
#
# Solo cambiaría el estado.
@app.route("/pedidos/<int:pedido_id>", methods=["PATCH"])
def modificar_parcialmente_pedido(pedido_id):

    # Buscamos el pedido.
    pedido = buscar_pedido(pedido_id)

    # Si no existe, devolvemos error 404.
    if pedido is None:

        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    # Leemos el JSON recibido.
    datos = request.get_json()

    # Comprobamos que existan datos.
    if not datos:

        return jsonify({
            "error": "No se han enviado datos"
        }), 400

    valido, mensaje = validar_pedido(datos, require_all=False)
    if not valido:
        return jsonify({"error": mensaje}), 400

    # Definimos qué campos permitimos modificar.
    #
    # Por ejemplo, no permitimos cambiar directamente:
    #
    # id
    # total
    #
    # porque esos valores los controla nuestro servidor.
    campos_permitidos = [
        "cliente",
        "estado",
        "fecha",
        "direccion_envio",
        "productos",
        "metodo_pago"
    ]

    # .items() nos permite recorrer un diccionario
    # obteniendo su clave y su valor.
    #
    # Por ejemplo:
    #
    # {
    #     "estado": "entregado"
    # }
    #
    # campo = "estado"
    # valor = "entregado"
    for campo, valor in datos.items():

        # Comprobamos que el campo esté permitido.
        if campo not in campos_permitidos:

            return jsonify({
                "error": f"No se puede modificar el campo '{campo}'"
            }), 400

        # Modificamos el campo correspondiente
        # dentro del pedido.
        pedido[campo] = valor

    # Si se han modificado los productos,
    # necesitamos volver a calcular el total.
    if "productos" in datos:

        # Calculamos el nuevo total.
        total = sum(
            producto["cantidad"] * producto["precio_unitario"]
            for producto in pedido["productos"]
        )

        # Actualizamos el total del pedido.
        pedido["total"] = round(total, 2)

    guardar_pedidos()

    # Devolvemos el pedido actualizado.
    return jsonify(pedido)


# =========================================================
# DELETE /pedidos/<id>
# =========================================================

# DELETE sirve para eliminar un recurso.
#
# Ejemplo:
#
# DELETE /pedidos/3
@app.route("/pedidos/<int:pedido_id>", methods=["DELETE"])
def eliminar_pedido(pedido_id):

    # Buscamos el pedido.
    pedido = buscar_pedido(pedido_id)

    # Comprobamos que exista.
    if pedido is None:

        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    # remove() elimina ese diccionario de nuestra
    # lista de pedidos.
    pedidos.remove(pedido)
    guardar_pedidos()

    # Respondemos indicando que se ha eliminado
    # correctamente.
    return jsonify({
        "mensaje": "Pedido eliminado correctamente",
        "pedido_id": pedido_id
    })


# =========================================================
# ARRANQUE DE LA APLICACIÓN
# =========================================================

# Esta condición comprueba si estamos ejecutando
# directamente este archivo:
#
# python app.py
#
# Si app.py fuera importado desde otro archivo,
# este bloque no se ejecutaría.
if __name__ == "__main__":

    # Arrancamos el servidor de desarrollo de Flask.
    app.run(

        # 0.0.0.0 permite que Flask escuche
        # conexiones desde cualquier interfaz de red
        # del ordenador.
        host="0.0.0.0",

        # Puerto en el que estará escuchando la aplicación.
        #
        # Nuestra URL será:
        #
        # http://localhost:5000
        port=5000,

        # debug=True activa el modo desarrollo.
        #
        # Entre otras cosas:
        # - Muestra errores detallados.
        # - Reinicia Flask automáticamente al cambiar código.
        #
        # No debería utilizarse así en producción.
        debug=True
    )