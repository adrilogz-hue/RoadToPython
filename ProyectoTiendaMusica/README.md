# API REST de Gestión de Pedidos

API REST desarrollada con **Python** y **Flask** para gestionar pedidos de clientes.

Este proyecto sirve como ejemplo para aprender a desarrollar servicios REST utilizando Flask y comprender el funcionamiento de los métodos HTTP más habituales.

---

## Características

- Obtener todos los pedidos.
- Obtener un pedido por su identificador.
- Obtener todos los pedidos de un cliente.
- Filtrar pedidos por estado.
- Crear nuevos pedidos.
- Modificar completamente un pedido.
- Modificar parcialmente un pedido.
- Eliminar pedidos.

Actualmente la aplicación utiliza una lista en memoria como almacenamiento de datos, por lo que cualquier modificación se perderá al reiniciar el servidor.

---

## Tecnologías

- Python 3.12+
- Flask 3.1

---

## Instalación

### Clonar el proyecto

```bash
git clone <url-del-repositorio>

cd pedidos_api
```

### Crear un entorno virtual

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar la aplicación

```bash
python app.py
```

La API quedará disponible en:

```
http://localhost:5000
```

---

# Estructura del proyecto

```
pedidos_api/
│
├── app.py
├── pedidos.json
├── requirements.txt
└── README.md
```

---

# Modelo de un pedido

```json
{
    "id": 1,
    "cliente": {
        "id": 101,
        "nombre": "Ana García",
        "email": "ana@email.com"
    },
    "estado": "enviado",
    "fecha": "2026-08-01",
    "direccion_envio": {
        "calle": "Calle Mayor 15",
        "ciudad": "Valladolid",
        "codigo_postal": "47001",
        "pais": "España"
    },
    "productos": [
        {
            "id": 501,
            "nombre": "Auriculares",
            "cantidad": 1,
            "precio_unitario": 79.99
        }
    ],
    "metodo_pago": "tarjeta",
    "total": 79.99
}
```

---

# Endpoints

## Obtener todos los pedidos

```
GET /pedidos
```

Respuesta:

```json
[
    {
        "id": 1,
        ...
    },
    {
        "id": 2,
        ...
    }
]
```

---

## Obtener un pedido

```
GET /pedidos/{id}
```

Ejemplo

```
GET /pedidos/1
```

---

## Obtener pedidos de un cliente

```
GET /clientes/{cliente_id}/pedidos
```

Ejemplo

```
GET /clientes/101/pedidos
```

---

## Filtrar por estado

```
GET /pedidos?estado=enviado
```

---

## Crear un pedido

```
POST /pedidos
```

Ejemplo de cuerpo:

```json
{
    "cliente": {
        "id": 103,
        "nombre": "Laura Martín",
        "email": "laura@email.com"
    },
    "estado": "pendiente",
    "fecha": "2026-08-07",
    "direccion_envio": {
        "calle": "Calle Santiago 20",
        "ciudad": "Valladolid",
        "codigo_postal": "47001",
        "pais": "España"
    },
    "productos": [
        {
            "id": 600,
            "nombre": "Monitor",
            "cantidad": 1,
            "precio_unitario": 250
        }
    ],
    "metodo_pago": "tarjeta"
}
```

Respuesta:

```
201 Created
```

---

## Modificar completamente un pedido

```
PUT /pedidos/{id}
```

Ejemplo

```
PUT /pedidos/2
```

---

## Modificar parcialmente un pedido

```
PATCH /pedidos/{id}
```

Ejemplo

```json
{
    "estado": "entregado"
}
```

---

## Eliminar un pedido

```
DELETE /pedidos/{id}
```

Ejemplo

```
DELETE /pedidos/3
```

Respuesta

```json
{
    "mensaje": "Pedido eliminado correctamente"
}
```

---

# Códigos HTTP utilizados

| Código | Descripción |
|---------|-------------|
| 200 | Operación realizada correctamente |
| 201 | Recurso creado |
| 400 | Petición incorrecta |
| 404 | Recurso no encontrado |

---

# Posibles mejoras

Este proyecto puede evolucionar fácilmente incorporando:

- SQLite o PostgreSQL.
- SQLAlchemy.
- Arquitectura por capas.
- Autenticación JWT.
- Docker.
- Docker Compose.
- Tests unitarios con pytest.
- Swagger/OpenAPI.
- Variables de entorno mediante `.env`.
- Logging.
- Validación de datos con Pydantic o Marshmallow.

Estas mejoras lo convertirían en un proyecto muy similar al que se desarrolla en un entorno profesional.