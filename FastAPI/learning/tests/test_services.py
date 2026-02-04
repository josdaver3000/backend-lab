import pytest
from app.services import buscar_prod_int, crear_producto, actualizar_stock
from app.models import Product
from app.db import ProductDB


def test_buscar_prod_int_existente(db_session):
    """Test: buscar producto por ID que existe"""
    producto = ProductDB(
        nombre="Test",
        descripcion="Descripción test",
        precio=50.0,
        categoria="Test",
        stock=10
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    resultado = buscar_prod_int(db_session, producto.id)
    assert resultado is not None
    assert resultado.nombre == "Test"


def test_buscar_prod_int_inexistente(db_session):
    """Test: buscar producto que no existe"""
    resultado = buscar_prod_int(db_session, 999)
    assert resultado is None


def test_crear_producto_service(db_session):
    """Test: crear producto desde service"""
    nuevo_producto = Product(
        nombre="Producto Service",
        descripcion="Test service",
        precio=100.0,
        categoria="Test",
        stock=5
    )
    
    resultado = crear_producto(db_session, nuevo_producto)
    assert resultado.id is not None
    assert resultado.nombre == "Producto Service"


def test_actualizar_stock_exitoso(db_session):
    """Test: actualizar stock correctamente"""
    producto = ProductDB(
        nombre="Stock Test",
        descripcion="Test",
        precio=10.0,
        categoria="Test",
        stock=50
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    resultado = actualizar_stock(db_session, producto.id, -20)
    assert resultado is not None
    assert resultado.stock == 30


def test_actualizar_stock_negativo(db_session):
    """Test: no permitir stock negativo"""
    producto = ProductDB(
        nombre="Stock Test",
        descripcion="Test",
        precio=10.0,
        categoria="Test",
        stock=10
    )
    db_session.add(producto)
    db_session.commit()
    db_session.refresh(producto)
    
    # Intentar restar más de lo disponible
    resultado = actualizar_stock(db_session, producto.id, -20)
    assert resultado is None  # Debe fallar