from app.models import Product


products_db = [Product(
        id=1,
        nombre="Teclado mecánico",
        descripcion="Teclado mecánico con switches azules y retroiluminación RGB",
        precio=249.99,
        categoria="Periféricos",
        stock=15
    ),
    Product(
        id=2,
        nombre="Mouse inalámbrico",
        descripcion="Mouse ergonómico inalámbrico con sensor óptico de alta precisión",
        precio=89.5,
        categoria="Periféricos",
        stock=30
    ),
    Product(
        id=3,
        nombre="Monitor 24 pulgadas",
        descripcion="Monitor Full HD de 24 pulgadas con panel IPS",
        precio=699.99,
        categoria="Pantallas",
        stock=8
    ),
    Product(
        id=4,
        nombre="Disco SSD 1TB",
        descripcion="Unidad de estado sólido SSD de 1TB para alto rendimiento",
        precio=459.0,
        categoria="Almacenamiento",
        stock=20
    ),
    Product(
        id=5,
        nombre="Audífonos gaming",
        descripcion="Audífonos gaming con micrófono y sonido envolvente",
        precio=179.99,
        categoria="Audio",
        stock=0  #! Producto agotado, caso real
    )
]  #! base de datos simulada
