from pydantic import BaseModel, Field  #! NUEVO: Field para validar datos en los modelos
from typing import Optional
from datetime import datetime

class Product(BaseModel): #! TU CODIGO: permite crear modelos de datos (Entidades)
    
    #! NUEVO: Validaciones con Field - evita datos inválidos automáticamente
    #! Si alguien intenta enviar datos que no cumplen, FastAPI devuelve error 422 automático
    
    nombre: str = Field(
        min_length=1,        #! Mínimo 1 carácter (no puede estar vacío)
        max_length=150,      #! Máximo 150 caracteres (acorde a la BD)
        description="Nombre del producto"  #! Aparece en la documentación /docs
    )
    descripcion: str = Field(
        min_length=1,
        max_length=500,
        description="Descripción del producto"
    )
    precio: float = Field(
        gt=0,                 #! Debe ser mayor que 0
        description="Precio del producto"
    )
    categoria: str = Field(
        min_length=1,
        max_length=80,        #! Acorde a la BD
        description="Categoría del producto"
    )
    stock: int = Field(
        ge=0,                 #! Debe ser mayor o igual a 0
        description="Cantidad en stock del producto"
    )

    class Config:
        from_attributes = True  #! Permite convertir desde modelos SQLAlchemy


class ProductResponse(BaseModel):
    """Modelo de respuesta que incluye campos de la BD"""
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    categoria: str
    stock: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  #! Permite convertir desde modelos SQLAlchemy


    #* ===============validations==================

    #? gt / ge → mayor (>) / mayor o igual (≥)

    #? lt / le → menor (<) / menor o igual (≤)

    #? min_length / max_length → tamaño de texto

    #? regex → patrón

    #? min_items / max_items → tamaño de listas

    #? EmailStr / HttpUrl / UUID → tipos inteligentes

    #? description → Swagger feliz