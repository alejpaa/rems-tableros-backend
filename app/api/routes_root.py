"""
Rutas principales de la API
Agrupa y monta todos los módulos de rutas (tableros, usuarios, etc.)
"""

from fastapi import APIRouter

# Importa los routers individuales
from app.api.route_tableros import router as tableros_router
# from app.api.routes_users import router as users_router  # Ejemplo futuro

# Crea el router raíz
api_router = APIRouter()

# Monta cada router con su prefijo
api_router.include_router(tableros_router)
# api_router.include_router(users_router)

# (Opcional) Rutas globales o de salud del sistema
@api_router.get("/", tags=["Root"])
def root():
    """
    Endpoint raíz de la API
    """
    return {"message": "🚀 API de REMS - Backend activo"}

@api_router.get("/health")
def health():
    return {"status": "ok"}

