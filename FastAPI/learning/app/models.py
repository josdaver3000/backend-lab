from pydantic import BaseModel, Field  #! NUEVO: Field para validar datos en los modelos

class Product(BaseModel): #! TU CODIGO: permite crear modelos de datos (Entidades)
    
    #! NUEVO: Validaciones con Field - evita datos inválidos automáticamente
    #! Si alguien intenta enviar datos que no cumplen, FastAPI devuelve error 422 automático
    
    nombre: str = Field(
        min_length=1,        #! Mínimo 1 carácter (no puede estar vacío)
        max_length=50,       #! Máximo 50 caracteres
        description="Nombre del producto"  #! Aparece en la documentación /docs
    )
    descripcion: str = Field(
        min_length=1,
        max_length=200,
        description="Descripción del producto"
    )
    precio: float = Field(
        gt=0,                 #! Debe ser mayor que 0
        description="Precio del producto"
    )
    id: int = Field(
        gt=0,                 #! Debe ser mayor que 0
        description="ID único del producto"
    )
    categoria: str = Field(
        min_length=1,
        max_length=50,
        description="Categoría del producto"
    )
    stock: int = Field(
        ge=0,                 #! Debe ser mayor o igual a 0
        description="Cantidad en stock del producto"
    )



    #* ===============validations==================

    #? gt / ge → mayor (>) / mayor o igual (≥)

    #? lt / le → menor (<) / menor o igual (≤)

    #? min_length / max_length → tamaño de texto

    #? regex → patrón

    #? min_items / max_items → tamaño de listas

    #? EmailStr / HttpUrl / UUID → tipos inteligentes

    #? description → Swagger feliz