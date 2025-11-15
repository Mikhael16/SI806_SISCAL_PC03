"""
SISCAL - Luz del Sur
Routes: Información
"""
from typing import List, Dict, Any
from fastapi import APIRouter

from app.services.info_service import InfoService

router = APIRouter(prefix="/api/v1/info", tags=["Información"])


@router.get("/services", response_model=List[Dict[str, Any]])
def get_services():
    """
    Retorna el catálogo de servicios y endpoints de la arquitectura SISCAL.
    Endpoint público (no requiere autenticación).
    """
    return InfoService.obtener_servicios()
