from app.db import ProductDB
from app.models import Product
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

def buscar_prod_int(db: Session, id: int) -> Optional[ProductDB]:
    """Buscar producto por ID en la base de datos"""
    return db.query(ProductDB).filter(ProductDB.id == id).first()

def buscar_prod_nombre(db: Session, nombre: str) -> Optional[ProductDB]:
    """Buscar producto por nombre exacto (case-insensitive)"""
    return db.query(ProductDB).filter(ProductDB.nombre.ilike(nombre)).first()

def buscar_prod_categoria(db: Session, categoria: str) -> list[ProductDB]:
    """Buscar productos por categoría (case-insensitive)"""
    return db.query(ProductDB).filter(ProductDB.categoria.ilike(categoria)).all()

def buscar_prod_rango_precio(db: Session, min_price: float, max_price: float) -> list[ProductDB]:
    """Buscar productos por rango de precio"""
    return db.query(ProductDB).filter(
        ProductDB.precio >= min_price,
        ProductDB.precio <= max_price
    ).all()

def producto_en_stock(db: Session, id: int) -> bool:
    """Verificar si un producto tiene stock disponible"""
    product = buscar_prod_int(db, id)
    if product and product.stock > 0:
        return True
    return False

def actualizar_stock(db: Session, id: int, quantity: int) -> Optional[ProductDB]:
    """Actualizar el stock de un producto.
    
    Args:
        db: Sesión de base de datos
        id: ID del producto
        quantity: Cantidad a sumar (positivo) o restar (negativo)
        
    Returns:
        Product actualizado si fue exitoso, None si no se pudo actualizar
    """
    product = buscar_prod_int(db, id)
    if product:
        nuevo_stock = product.stock + quantity
        if nuevo_stock >= 0:  #! No permitir stock negativo
            product.stock = nuevo_stock
            product.updated_at = datetime.utcnow()
            db.commit()
            db.refresh(product)
            return product
        return None  #! Stock resultante sería negativo
    return None  #! Producto no encontrado

def obtener_todos_productos(db: Session) -> list[ProductDB]:
    """Obtener todos los productos de la base de datos"""
    return db.query(ProductDB).all()

def crear_producto(db: Session, product: Product) -> ProductDB:
    """Crear un nuevo producto en la base de datos"""
    db_product = ProductDB(
        nombre=product.nombre,
        descripcion=product.descripcion,
        precio=product.precio,
        categoria=product.categoria,
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def eliminar_producto(db: Session, id: int) -> bool:
    """Eliminar un producto por su ID"""
    product = buscar_prod_int(db, id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False

def actualizar_producto(db: Session, id: int, product: Product) -> Optional[ProductDB]:
    """Actualizar un producto existente completamente"""
    db_product = buscar_prod_int(db, id)
    if db_product:
        db_product.nombre = product.nombre
        db_product.descripcion = product.descripcion
        db_product.precio = product.precio
        db_product.categoria = product.categoria
        db_product.stock = product.stock
        db_product.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_product)
        return db_product
    return None