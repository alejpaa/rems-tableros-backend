from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.routes_root import api_router
from app.core.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Maneja el ciclo de vida de la aplicación:
    - En startup: inicializa la base de datos
    - En shutdown: libera recursos si es necesario
    """
    print("🚀 Iniciando aplicación...")
    init_db()  # crea tablas si no existen
    yield
    print("🛑 Cerrando aplicación...")


app = FastAPI(
    title="REMS Tableros Backend",
    version="1.0.0",
    description="API para gestionar tableros eléctricos",
    lifespan=lifespan
)

# Montar rutas
app.include_router(api_router)
