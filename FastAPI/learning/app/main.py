from fastapi import FastAPI
from app.routes import router  #! Importar desde app.routes

app = FastAPI(title="API de Productos", version="1.0")
app.include_router(router)

#? python.exe -m uvicorn app.main:app --reload