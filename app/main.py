"""
SISCAL - Luz del Sur
Aplicación principal FastAPI
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import routes_auth, routes_info

# Crear aplicación FastAPI
app = FastAPI(
    title="SISCAL - Luz del Sur",
    description="Sistema de Gestión de Reclamos - Luz del Sur",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers de API
app.include_router(routes_auth.router)
app.include_router(routes_info.router)

# Servir archivos estáticos del frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/health")
def health_check():
    """Endpoint de salud del servicio"""
    return {"status": "ok", "service": "SISCAL - Luz del Sur"}
