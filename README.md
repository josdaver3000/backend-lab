# API de Gestión de Productos

API REST construida con FastAPI para gestionar un inventario de productos.

## Características

- ✅ CRUD completo de productos
- ✅ Búsqueda por ID, nombre y categoría
- ✅ Filtrado por rango de precios
- ✅ Control de stock
- ✅ Documentación automática con Swagger

## Instalación

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: http://127.0.0.1:8000

## Documentación

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Endpoints

### Productos
- `GET /productos` - Obtener todos los productos
- `GET /productos/{id}` - Obtener producto por ID
- `GET /productos/buscar/nombre/{nombre}` - Buscar por nombre
- `GET /productos/categoria/{categoria}` - Filtrar por categoría
- `GET /productos/rango_precio/?min_price=X&max_price=Y` - Filtrar por precio
- `GET /productos/low_stock?threshold=5` - Productos con stock bajo
- `GET /productos/{id}/stock` - Verificar stock de un producto
- `PATCH /productos/{id}/actualizar_stock` - Actualizar stock

## Estructura del Proyecto

```
app/
├── __init__.py
├── main.py          # Punto de entrada de la aplicación
├── models.py        # Modelos de datos (Pydantic)
├── routes.py        # Definición de endpoints
├── services.py      # Lógica de negocio
└── db.py           # Base de datos simulada
```

## Tecnologías

- FastAPI 0.128.0
- Uvicorn 0.40.0
- Pydantic 2.12.5
