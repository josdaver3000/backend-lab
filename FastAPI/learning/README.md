# API de Gestión de Productos

API REST construida con FastAPI para gestionar un inventario de productos.

## Características

- CRUD completo de productos
- Búsqueda por ID, nombre y categoría
- Filtrado por rango de precios
- Control de stock
- Documentación automática con Swagger

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
- SQLAlchemy 2.0.36
- PostgreSQL 14


## specifications of the project. 

main.py es el punto de entrada de la aplicación FastAPI.

db.py contiene la configuracion de la base de datos usando SQLAlchemy, migraciones con alembic, manejo de variables de entorno con python-dotenv, modelosDB con SQLAlchemy ORM.

models.py define los modelos de datos usando Pydantic para validación y serialización.

routes.py define los endpoints de la API y maneja las solicitudes http

services.py contiene la lógica de negocio para manejar productos, incluyendo operaciones CRUD y gestión de stock.

seed_data.py es un script para poblar la base de datos con datos iniciales para pruebas y desarrollo.

__init__.py marca el directorio app como un paquete Python.

.env.example proporciona un ejemplo de archivo de variables de entorno para configuración. (para no poner datos sensibles en el repositorio)

## alembic folder
- Contiene la configuración y scripts de migración de la base de datos usando Alembic.

- versions/: Directorio donde se almacenan los scripts de migración generados por Alembic.

- script.py.mako: Plantilla utilizada por Alembic para generar nuevos scripts de migración.
- env.py: Archivo de configuración de Alembic que establece la conexión a la base de datos y otras configuraciones necesarias para las migraciones.

- alembic.ini: Archivo de configuración principal de Alembic que define parámetros como la ubicación de los scripts de migración y la URL de la base de datos.





