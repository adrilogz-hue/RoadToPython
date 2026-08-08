from flask import Flask, jsonify, request
from pedidos import pedidos

app = Flask(__name__)


# ---------------------------------------------------------
# Función auxiliar
# ---------------------------------------------------------

def buscar_pedido(pedido_id):
    for pedido in pedidos:
        if pedido["id"] == pedido_id:
            return pedido

    return None


# ---------------------------------------------------------
# GET /
# ---------------------------------------------------------

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "servicio": "API de pedidos",
        "version": "1.0",
        "endpoints": {
            "GET /pedidos": "Obtener todos los pedidos",
            "GET /pedidos/<id>": "Obtener un pedido concreto",
            "GET /clientes/<id>/pedidos": "Obtener pedidos de un cliente",
            "POST /pedidos": "Crear un pedido",
            "PUT /pedidos/<id>": "Modificar completamente un pedido",
            "PATCH /pedidos/<id>": "Modificar parcialmente un pedido",
            "DELETE /pedidos/<id>": "Eliminar un pedido"
        }
    })


# ---------------------------------------------------------
# GET /pedidos
# Obtener todos los pedidos
# ---------------------------------------------------------

@app.route("/pedidos", methods=["GET"])
def obtener_pedidos():

    estado = request.args.get("estado")

    if estado:
        pedidos_filtrados = [
            pedido
            for pedido in pedidos
            if pedido["estado"].lower() == estado.lower()
        ]

        return jsonify(pedidos_filtrados)

    return jsonify(pedidos)


# ---------------------------------------------------------
# GET /pedidos/<id>
# Obtener los detalles de un pedido concreto
# ---------------------------------------------------------

@app.route("/pedidos/<int:pedido_id>", methods=["GET"])
def obtener_pedido(pedido_id):

    pedido = buscar_pedido(pedido_id)

    if pedido is None:
        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    return jsonify(pedido)


# ---------------------------------------------------------
# GET /clientes/<id>/pedidos
# Obtener todos los pedidos de un cliente
# ---------------------------------------------------------

@app.route("/clientes/<int:cliente_id>/pedidos", methods=["GET"])
def obtener_pedidos_cliente(cliente_id):

    pedidos_cliente = [
        pedido
        for pedido in pedidos
        if pedido["cliente"]["id"] == cliente_id
    ]

    if not pedidos_cliente:
        return jsonify({
            "error": "No se encontraron pedidos para ese cliente"
        }), 404

    return jsonify(pedidos_cliente)


# ---------------------------------------------------------
# POST /pedidos
# Crear un nuevo pedido
# ---------------------------------------------------------

@app.route("/pedidos", methods=["POST"])
def crear_pedido():

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "Debes enviar los datos del pedido en formato JSON"
        }), 400

    campos_obligatorios = [
        "cliente",
        "estado",
        "fecha",
        "direccion_envio",
        "productos",
        "metodo_pago"
    ]

    for campo in campos_obligatorios:
        if campo not in datos:
            return jsonify({
                "error": f"Falta el campo obligatorio: {campo}"
            }), 400

    nuevo_id = max(
        (pedido["id"] for pedido in pedidos),
        default=0
    ) + 1

    total = 0

    for producto in datos["productos"]:
        total += (
            producto["cantidad"]
            * producto["precio_unitario"]
        )

    nuevo_pedido = {
        "id": nuevo_id,
        "cliente": datos["cliente"],
        "estado": datos["estado"],
        "fecha": datos["fecha"],
        "direccion_envio": datos["direccion_envio"],
        "productos": datos["productos"],
        "metodo_pago": datos["metodo_pago"],
        "total": round(total, 2)
    }

    pedidos.append(nuevo_pedido)

    return jsonify(nuevo_pedido), 201


# ---------------------------------------------------------
# PUT /pedidos/<id>
# Sustituir completamente un pedido
# ---------------------------------------------------------

@app.route("/pedidos/<int:pedido_id>", methods=["PUT"])
def modificar_pedido(pedido_id):

    pedido = buscar_pedido(pedido_id)

    if pedido is None:
        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "No se han enviado datos"
        }), 400

    campos_obligatorios = [
        "cliente",
        "estado",
        "fecha",
        "direccion_envio",
        "productos",
        "metodo_pago"
    ]

    for campo in campos_obligatorios:
        if campo not in datos:
            return jsonify({
                "error": f"Falta el campo obligatorio: {campo}"
            }), 400

    total = sum(
        producto["cantidad"] * producto["precio_unitario"]
        for producto in datos["productos"]
    )

    pedido.clear()

    pedido.update({
        "id": pedido_id,
        "cliente": datos["cliente"],
        "estado": datos["estado"],
        "fecha": datos["fecha"],
        "direccion_envio": datos["direccion_envio"],
        "productos": datos["productos"],
        "metodo_pago": datos["metodo_pago"],
        "total": round(total, 2)
    })

    return jsonify(pedido)


# ---------------------------------------------------------
# PATCH /pedidos/<id>
# Modificar solo algunos campos
# ---------------------------------------------------------

@app.route("/pedidos/<int:pedido_id>", methods=["PATCH"])
def modificar_parcialmente_pedido(pedido_id):

    pedido = buscar_pedido(pedido_id)

    if pedido is None:
        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    datos = request.get_json()

    if not datos:
        return jsonify({
            "error": "No se han enviado datos"
        }), 400

    campos_permitidos = [
        "cliente",
        "estado",
        "fecha",
        "direccion_envio",
        "productos",
        "metodo_pago"
    ]

    for campo, valor in datos.items():

        if campo not in campos_permitidos:
            return jsonify({
                "error": f"No se puede modificar el campo '{campo}'"
            }), 400

        pedido[campo] = valor

    # Recalculamos el total si se modifican los productos
    if "productos" in datos:

        total = sum(
            producto["cantidad"] * producto["precio_unitario"]
            for producto in pedido["productos"]
        )

        pedido["total"] = round(total, 2)

    return jsonify(pedido)


# ---------------------------------------------------------
# DELETE /pedidos/<id>
# Eliminar pedido
# ---------------------------------------------------------

@app.route("/pedidos/<int:pedido_id>", methods=["DELETE"])
def eliminar_pedido(pedido_id):

    pedido = buscar_pedido(pedido_id)

    if pedido is None:
        return jsonify({
            "error": "Pedido no encontrado"
        }), 404

    pedidos.remove(pedido)

    return jsonify({
        "mensaje": "Pedido eliminado correctamente",
        "pedido_id": pedido_id
    })


# ---------------------------------------------------------
# Arrancar Flask
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )