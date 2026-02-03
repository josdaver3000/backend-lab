"""
Script para poblar la base de datos con datos de prueba
"""
from app.db import SessionLocal, ProductDB

def seed_database():
    """Insertar productos de prueba en la base de datos"""
    db = SessionLocal()
    
    try:
        # Verificar si ya hay productos
        count = db.query(ProductDB).count()
        if count > 0:
            print(f"La base de datos ya tiene {count} productos.")
            response = input("¿Deseas eliminar todos y recargar? (s/n): ")
            if response.lower() == 's':
                db.query(ProductDB).delete()
                db.commit()
                print("✓ Productos eliminados")
            else:
                print("Cancelado.")
                return
        
        # Productos de prueba
        productos = [
            ProductDB(
                nombre="Teclado mecánico",
                descripcion="Teclado mecánico con switches azules y retroiluminación RGB",
                precio=249.99,
                categoria="Periféricos",
                stock=15
            ),
            ProductDB(
                nombre="Mouse inalámbrico",
                descripcion="Mouse ergonómico inalámbrico con sensor óptico de alta precisión",
                precio=89.5,
                categoria="Periféricos",
                stock=30
            ),
            ProductDB(
                nombre="Monitor 24 pulgadas",
                descripcion="Monitor Full HD de 24 pulgadas con panel IPS",
                precio=699.99,
                categoria="Pantallas",
                stock=8
            ),
            ProductDB(
                nombre="Disco SSD 1TB",
                descripcion="Unidad de estado sólido SSD de 1TB para alto rendimiento",
                precio=459.0,
                categoria="Almacenamiento",
                stock=20
            ),
            ProductDB(
                nombre="Audífonos gaming",
                descripcion="Audífonos gaming con micrófono y sonido envolvente",
                precio=179.99,
                categoria="Audio",
                stock=0  # Producto agotado
            ),
            ProductDB(
                nombre="Laptop Gaming",
                descripcion="Laptop de alto rendimiento con RTX 4060 y 16GB RAM",
                precio=1299.99,
                categoria="Computadoras",
                stock=5
            ),
            ProductDB(
                nombre="Webcam HD",
                descripcion="Cámara web Full HD con micrófono incorporado",
                precio=79.99,
                categoria="Periféricos",
                stock=12
            )
        ]
        
        # Insertar productos
        db.add_all(productos)
        db.commit()
        
        print(f"✓ Se insertaron {len(productos)} productos exitosamente")
        
        # Mostrar productos insertados
        print("\nProductos en la base de datos:")
        print("-" * 80)
        all_products = db.query(ProductDB).all()
        for p in all_products:
            print(f"ID: {p.id:2} | {p.nombre:30} | ${p.precio:8.2f} | Stock: {p.stock:3}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    print("🌱 Poblando base de datos...")
    seed_database()
