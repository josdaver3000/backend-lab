# 🔄 Guía de Migraciones con Alembic

Esta guía te explica cómo usar **Alembic** para gestionar cambios en tu base de datos automáticamente.

---

## 📚 ¿Qué es Alembic?

Alembic es una herramienta de **migraciones de base de datos** que:
- Detecta cambios en tus modelos SQLAlchemy automáticamente
- Genera scripts SQL para aplicar cambios
- Permite revertir cambios (rollback)
- Mantiene historial de versiones de tu esquema

---

## 🚀 Comandos básicos

### 1️⃣ Crear una migración automática

Cuando modificas tus modelos en `app/db.py` (agregar columna, tabla nueva, etc.):

```bash
alembic revision --autogenerate -m "Descripción del cambio"
```

**Ejemplo**:
```bash
# Si agregas una columna "marca" a ProductDB
alembic revision --autogenerate -m "Add marca column to products"
```

### 2️⃣ Aplicar migraciones (actualizar la BD)

```bash
alembic upgrade head
```

Esto aplica **todos** los cambios pendientes a la base de datos.

### 3️⃣ Revertir última migración (deshacer)

```bash
alembic downgrade -1
```

### 4️⃣ Ver historial de migraciones

```bash
alembic history
```

### 5️⃣ Ver migración actual de la BD

```bash
alembic current
```

---

## 📝 Flujo de trabajo típico

### **Escenario: Quieres agregar una columna "marca" a products**

#### Paso 1: Modificar el modelo en `app/db.py`

```python
class ProductDB(Base):
    __tablename__ = "products"
    # ... columnas existentes ...
    marca = Column(String(100), nullable=True)  # 👈 Nueva columna
```

#### Paso 2: Crear la migración

```bash
alembic revision --autogenerate -m "Add marca to products"
```

Alembic crea un archivo en `alembic/versions/` con código SQL automático.

#### Paso 3: Revisar la migración

Abre el archivo generado en `alembic/versions/` y verifica que esté correcto.

#### Paso 4: Aplicar la migración

```bash
alembic upgrade head
```

¡Listo! Tu base de datos ahora tiene la columna `marca`.

---

## 🛠️ Comandos avanzados

### Revertir a una versión específica

```bash
alembic downgrade <revision_id>
```

### Aplicar hasta una versión específica

```bash
alembic upgrade <revision_id>
```

### Ver SQL sin ejecutar

```bash
alembic upgrade head --sql
```

### Crear migración vacía (manual)

```bash
alembic revision -m "Custom migration"
```

---

## ⚠️ Buenas prácticas

1. **Siempre revisa** los archivos de migración antes de aplicarlos
2. **Haz backup** de tu BD antes de migraciones en producción
3. **Commitea** las migraciones en Git junto con los cambios de código
4. **No modifiques** migraciones ya aplicadas (crea una nueva)
5. **Prueba** las migraciones en desarrollo antes de producción

---

## 🐛 Solución de problemas

### Error: "Target database is not up to date"

Tu BD está desactualizada. Ejecuta:
```bash
alembic upgrade head
```

### Error: "Can't locate revision identified by"

Tu BD tiene migraciones que no existen en el código. Verifica con:
```bash
alembic current
alembic history
```

### Alembic no detecta cambios

1. Verifica que importaste el modelo en `alembic/env.py`
2. Asegúrate de que `target_metadata = Base.metadata` esté configurado
3. Revisa que el modelo herede de `Base`

---

## 📂 Estructura de archivos

```
alembic/
├── versions/          # Aquí se guardan las migraciones
│   └── fa1489732000_initial_migration_create_products_table.py
├── env.py            # Configuración (ya modificado para usar .env)
├── script.py.mako    # Template para nuevas migraciones
└── README

alembic.ini           # Configuración principal
```

---

## 🎯 Ejemplo completo: Agregar tabla "categorias"

### 1. Crear el modelo en `app/db.py`:

```python
class CategoriaDB(Base):
    __tablename__ = "categorias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(80), nullable=False, unique=True)
    descripcion = Column(Text)
```

### 2. Importar en `alembic/env.py`:

```python
from app.db import Base, ProductDB, CategoriaDB  # Agregar CategoriaDB
```

### 3. Generar migración:

```bash
alembic revision --autogenerate -m "Create categorias table"
```

### 4. Aplicar:

```bash
alembic upgrade head
```

---

## 📖 Recursos

- [Documentación oficial de Alembic](https://alembic.sqlalchemy.org/)
- [Tutorial de migraciones](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Auto-generate](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
