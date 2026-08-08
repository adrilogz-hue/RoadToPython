pedidos = [
    {
        "id": 1,
        "cliente": {
            "id": 101,
            "nombre": "Ana García",
            "email": "ana.garcia@email.com"
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
                "nombre": "Auriculares Bluetooth",
                "cantidad": 1,
                "precio_unitario": 79.99
            },
            {
                "id": 502,
                "nombre": "Cable USB-C",
                "cantidad": 2,
                "precio_unitario": 12.50
            }
        ],
        "metodo_pago": "tarjeta",
        "total": 104.99
    },
    {
        "id": 2,
        "cliente": {
            "id": 102,
            "nombre": "Carlos López",
            "email": "carlos.lopez@email.com"
        },
        "estado": "procesando",
        "fecha": "2026-08-04",
        "direccion_envio": {
            "calle": "Avenida Salamanca 42",
            "ciudad": "Valladolid",
            "codigo_postal": "47014",
            "pais": "España"
        },
        "productos": [
            {
                "id": 503,
                "nombre": "Teclado mecánico",
                "cantidad": 1,
                "precio_unitario": 89.90
            }
        ],
        "metodo_pago": "paypal",
        "total": 89.90
    },
    {
        "id": 3,
        "cliente": {
            "id": 101,
            "nombre": "Ana García",
            "email": "ana.garcia@email.com"
        },
        "estado": "entregado",
        "fecha": "2026-07-20",
        "direccion_envio": {
            "calle": "Calle Mayor 15",
            "ciudad": "Valladolid",
            "codigo_postal": "47001",
            "pais": "España"
        },
        "productos": [
            {
                "id": 504,
                "nombre": "Ratón inalámbrico",
                "cantidad": 1,
                "precio_unitario": 39.99
            },
            {
                "id": 505,
                "nombre": "Alfombrilla",
                "cantidad": 1,
                "precio_unitario": 19.99
            }
        ],
        "metodo_pago": "tarjeta",
        "total": 59.98
    }
]