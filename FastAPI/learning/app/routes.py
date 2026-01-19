from fastapi import APIRouter, HTTPException
from app.models import Product
from app.services import buscar_prod_int, buscar_prod_nombre, buscar_prod_categoria, buscar_prod_rango_precio, producto_en_stock, actualizar_stock
from app.db import products_db

router = APIRouter()

#* ======================= GET ======================== (para leer datos)

#! IMPORTANTE: Las rutas específicas DEBEN ir ANTES que las rutas con parámetros {id}
#! Si no, FastAPI interpretará "low_stock" como un ID

@router.get("/productos", response_model=list[Product])
def obtener_todos_productos():
    """Obtener lista de todos los productos"""
    return products_db

@router.get("/productos/low_stock", response_model=list[Product])
def obtener_productos_bajo_stock(threshold: int = 5):
    """Obtener productos con stock bajo (por defecto <= 5)"""
    low_stock_products = [product for product in products_db if product.stock <= threshold]
    return low_stock_products

@router.get("/productos/buscar/nombre/{nombre}", response_model=Product)
def obtener_producto_por_nombre(nombre: str):
    """Buscar producto por nombre exacto"""
    product = buscar_prod_nombre(nombre)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Producto no encontrado") #! 404 es no encontrado

@router.get("/productos/categoria/{categoria}", response_model=list[Product])
def obtener_productos_por_categoria(categoria: str):
    """Obtener todos los productos de una categoría"""
    products = buscar_prod_categoria(categoria)
    return products

@router.get("/productos/rango_precio/", response_model=list[Product])
def obtener_productos_por_rango_precio(min_price: float, max_price: float):
    """Buscar productos por rango de precio"""
    products = buscar_prod_rango_precio(min_price, max_price)
    return products

@router.get("/productos/{id}", response_model=Product)
def obtener_producto_por_id(id: int):
    """Obtener un producto por su ID"""
    product = buscar_prod_int(id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Producto no encontrado") #! 404 es no encontrado

@router.get("/productos/{id}/stock", response_model=dict)
def verificar_stock_producto(id: int):
    """Verificar si un producto tiene stock disponible"""
    product = buscar_prod_int(id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"id": id, "nombre": product.nombre, "stock": product.stock, "disponible": product.stock > 0}


@router.patch("/productos/{id}/actualizar_stock", response_model=Product)
def actualizar_stock_producto(id: int, quantity: int):
    updated_product = actualizar_stock(id, quantity)
    if updated_product:
        return updated_product
    raise HTTPException(status_code=400, detail="No se pudo actualizar el stock del producto") #! 400 es error de solicitud incorrecta