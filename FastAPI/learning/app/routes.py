from fastapi import APIRouter, HTTPException, Depends
from app.models import Product, ProductResponse
from app.services import (
    buscar_prod_int, 
    buscar_prod_nombre, 
    buscar_prod_categoria, 
    buscar_prod_rango_precio, 
    producto_en_stock, 
    actualizar_stock,
    obtener_todos_productos,
    crear_producto,
    eliminar_producto,
    actualizar_producto
)
from app.db import get_db
from sqlalchemy.orm import Session
from app.db import ProductDB

router = APIRouter()

# IMPORTANTE: Las rutas específicas van ANTES que las rutas con parámetros {id}
# Si no, FastAPI interpretará "low_stock" como un ID

@router.get("/productos", response_model=list[ProductResponse]) 
def obtener_todos_productos_route(db: Session = Depends(get_db)):
    """Obtener lista de todos los productos"""
    return obtener_todos_productos(db)

@router.get("/productos/low_stock", response_model=list[ProductResponse])
def obtener_productos_bajo_stock(threshold: int = 5, db: Session = Depends(get_db)):
    """Obtener productos con stock bajo (por defecto <= 5)"""
    
    low_stock_products = db.query(ProductDB).filter(ProductDB.stock <= threshold).all()
    return low_stock_products

@router.get("/productos/buscar/nombre/{nombre}", response_model=ProductResponse)
def obtener_producto_por_nombre(nombre: str, db: Session = Depends(get_db)):
    """Buscar producto por nombre exacto"""
    product = buscar_prod_nombre(db, nombre)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.get("/productos/categoria/{categoria}", response_model=list[ProductResponse])
def obtener_productos_por_categoria(categoria: str, db: Session = Depends(get_db)):
    """Obtener todos los productos de una categoría"""
    products = buscar_prod_categoria(db, categoria)
    return products

@router.get("/productos/rango_precio/", response_model=list[ProductResponse])
def obtener_productos_por_rango_precio(min_price: float, max_price: float, db: Session = Depends(get_db)):
    """Buscar productos por rango de precio"""
    products = buscar_prod_rango_precio(db, min_price, max_price)
    return products

@router.get("/productos/{id}", response_model=ProductResponse)
def obtener_producto_por_id(id: int, db: Session = Depends(get_db)):
    """Obtener un producto por su ID"""
    product = buscar_prod_int(db, id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Producto no encontrado") 

@router.get("/productos/{id}/stock", response_model=dict)
def verificar_stock_producto(id: int, db: Session = Depends(get_db)):
    """Verificar si un producto tiene stock disponible"""
    product = buscar_prod_int(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"id": id, "nombre": product.nombre, "stock": product.stock, "disponible": product.stock > 0}

@router.post("/productos", response_model=ProductResponse, status_code=201)
def crear_producto_route(product: Product, db: Session = Depends(get_db)):
    """Crear un nuevo producto"""
    return crear_producto(db, product)

@router.put("/productos/{id}", response_model=ProductResponse)
def reemplazar_producto(id: int, nuevo_producto: Product, db: Session = Depends(get_db)):
    """Reemplazar un producto existente por completo"""
    updated = actualizar_producto(db, id, nuevo_producto)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.delete("/productos/{id}", status_code=204)
def eliminar_producto_route(id: int, db: Session = Depends(get_db)):
    """Eliminar un producto por su ID"""
    if eliminar_producto(db, id):
        return
    raise HTTPException(status_code=404, detail="Producto no encontrado")



@router.patch("/productos/{id}/actualizar_stock", response_model=ProductResponse)
def actualizar_stock_producto(id: int, quantity: int, db: Session = Depends(get_db)):
    updated_product = actualizar_stock(db, id, quantity)
    if updated_product:
        return updated_product
    raise HTTPException(status_code=400, detail="No se pudo actualizar el stock del producto")

