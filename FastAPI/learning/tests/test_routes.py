import pytest
from app.db import ProductDB


def test_obtener_todos_productos_vacio(client):
    """Test: GET /productos cuando no hay productos"""
    response = client.get("/productos")
    assert response.status_code == 200
    assert response.json() == []


def test_crear_producto(client):
    """Test: POST /productos - crear producto exitoso"""
    nuevo_producto = {
        "nombre": "Laptop Test",
        "descripcion": "Laptop de prueba",
        "precio": 999.99,
        "categoria": "Electrónica",
        "stock": 10
    }
    response = client.post("/productos", json=nuevo_producto)
    assert response.status_code == 201
    data = response.json()
    assert data["nombre"] == "Laptop Test"
    assert data["precio"] == 999.99
    assert "id" in data


def test_crear_producto_precio_invalido(client):
    """Test: POST /productos - precio negativo debe fallar"""
    producto_invalido = {
        "nombre": "Producto Malo",
        "descripcion": "Test",
        "precio": -10.0,  # Precio inválido
        "categoria": "Test",
        "stock": 5
    }
    response = client.post("/productos", json=producto_invalido)
    assert response.status_code == 422  # Validation error


def test_obtener_producto_por_id(client, db_session):
    """Test: GET /productos/{id} - obtener producto existente"""
    # Crear producto en la BD de prueba
    producto = ProductDB(
        nombre="Mouse",
        descripcion="Mouse inalámbrico",
        precio=25.50,
        categoria="Periféricos",
        stock=50
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    # Hacer request
    response = client.get(f"/productos/{producto.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Mouse"
    assert data["id"] == producto.id


def test_obtener_producto_inexistente(client):
    """Test: GET /productos/999 - producto que no existe"""
    response = client.get("/productos/999")
    assert response.status_code == 404
    assert "no encontrado" in response.json()["detail"].lower()


def test_actualizar_producto(client, db_session):
    """Test: PUT /productos/{id} - actualizar producto"""
    # Crear producto
    producto = ProductDB(
        nombre="Teclado",
        descripcion="Teclado mecánico",
        precio=100.0,
        categoria="Periféricos",
        stock=20
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    # Actualizar
    datos_actualizados = {
        "nombre": "Teclado RGB",
        "descripcion": "Teclado mecánico con luces",
        "precio": 150.0,
        "categoria": "Gaming",
        "stock": 15
    }
    response = client.put(f"/productos/{producto.id}", json=datos_actualizados)
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Teclado RGB"
    assert data["precio"] == 150.0


def test_eliminar_producto(client, db_session):
    """Test: DELETE /productos/{id} - eliminar producto"""
    # Crear producto
    producto = ProductDB(
        nombre="Monitor",
        descripcion="Monitor 24 pulgadas",
        precio=200.0,
        categoria="Pantallas",
        stock=5
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    # Eliminar
    response = client.delete(f"/productos/{producto.id}")
    assert response.status_code == 204
    
    # Verificar que ya no existe
    response = client.get(f"/productos/{producto.id}")
    assert response.status_code == 404


def test_actualizar_stock(client, db_session):
    """Test: PATCH /productos/{id}/actualizar_stock"""
    # Crear producto con stock inicial
    producto = ProductDB(
        nombre="Audífonos",
        descripcion="Audífonos bluetooth",
        precio=50.0,
        categoria="Audio",
        stock=100
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    # Reducir stock
    response = client.patch(
        f"/productos/{producto.id}/actualizar_stock?quantity=-10"
    )
    assert response.status_code == 200
    data = response.json()
    assert data["stock"] == 90


def test_buscar_por_categoria(client, db_session):
    """Test: GET /productos/categoria/{categoria}"""
    # Crear varios productos
    productos = [
        ProductDB(nombre="Laptop", descripcion="", precio=1000, categoria="Computadoras", stock=5),
        ProductDB(nombre="PC", descripcion="", precio=1500, categoria="Computadoras", stock=3),
        ProductDB(nombre="Mouse", descripcion="", precio=20, categoria="Periféricos", stock=10),
    ]
    for p in productos:
        db_session.add(p)
    db_session.commit()
    
    # Buscar por categoría
    response = client.get("/productos/categoria/Computadoras")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(p["categoria"] == "Computadoras" for p in data)