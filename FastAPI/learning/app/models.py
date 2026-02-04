from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class Product(BaseModel):
    """Modelo Pydantic para validación de datos de productos"""
    model_config = ConfigDict(from_attributes=True)
    nombre: str = Field(
        min_length=1,
        max_length=150,
        description="Nombre del producto"
    )
    descripcion: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Descripción del producto"
    )
    precio: float = Field(
        gt=0,
        description="Precio del producto"
    )
    categoria: str = Field(
        min_length=1,
        max_length=80,
        description="Categoría del producto"
    )
    stock: int = Field(
        ge=0,
        description="Cantidad en stock del producto"
    )


class ProductResponse(BaseModel):
    """Modelo de respuesta que incluye campos de la BD"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    categoria: str
    stock: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None