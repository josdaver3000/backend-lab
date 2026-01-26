from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener URL de la base de datos desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:josdav@localhost:5432/api_db")

# Crear motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  #! echo=True muestra SQL en consola (útil para debugging)

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Modelo SQLAlchemy para la tabla 'products'
class ProductDB(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Float, nullable=False)
    categoria = Column(String(80), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Función para obtener sesión de base de datos
def get_db():
    """Dependency para obtener sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
