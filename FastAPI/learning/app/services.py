from app.db import products_db
from app.models import Product
from typing import Optional

def buscar_prod_int(id: int) -> Optional[Product]:
    for product in products_db:
        if product.id == id:
            return product
    return None

def buscar_prod_nombre(nombre: str) -> Optional[Product]:
    for product in products_db:
        if product.nombre.lower() == nombre.lower():
            return product
    return None

def buscar_prod_categoria(categoria: str) -> list[Product]:
    results = []
    for product in products_db:
        if product.categoria.lower() == categoria.lower():
            results.append(product)
    return results

def buscar_prod_rango_precio(min_price: float, max_price: float) -> list[Product]:
    results = []
    for product in products_db:
        if min_price <= product.precio <= max_price:
            results.append(product)
    return results

def producto_en_stock(id: int) -> bool:
    product = buscar_prod_int(id)
    if product and product.stock > 0:
        return True
    return False

def actualizar_stock(id: int, quantity: int) -> Optional[Product]:
    """Actualizar el stock de un producto.
    
    Args:
        id: ID del producto
        quantity: Cantidad a sumar (positivo) o restar (negativo)
        
    Returns:
        Product actualizado si fue exitoso, None si no se pudo actualizar
    """
    for index, product in enumerate(products_db):
        if product.id == id:
            nuevo_stock = product.stock + quantity
            if nuevo_stock >= 0:  #! No permitir stock negativo
                products_db[index].stock = nuevo_stock
                return products_db[index]
            return None  #! Stock resultante sería negativo
    return None  #! Producto no encontrado