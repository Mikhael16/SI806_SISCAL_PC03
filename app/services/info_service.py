"""
SISCAL - Luz del Sur
Service: Información de servicios
"""
from typing import List, Dict, Any

# Catálogo de servicios y endpoints de la arquitectura SISCAL
CATALOGO_SERVICIOS = [
    {
        "name": "Load Balancer",
        "type": "infra",
        "endpoints": []
    },
    {
        "name": "API Gateway",
        "type": "infra",
        "endpoints": ["/api/v1/auth/*", "/api/v1/info/*"]
    },
    {
        "name": "MS Reclamos",
        "type": "microservice",
        "endpoints": ["/api/v1/reclamos (futuro)"]
    },
    {
        "name": "MS Notificaciones",
        "type": "microservice",
        "endpoints": ["/api/v1/notificaciones (futuro)"]
    },
    {
        "name": "MS Envío de Lotes",
        "type": "microservice",
        "endpoints": ["/api/v1/lotes (futuro)"]
    },
    {
        "name": "MS Logs & Auditoría",
        "type": "microservice",
        "endpoints": ["/api/v1/logs (futuro)"]
    },
    {
        "name": "IBM Informix (BD)",
        "type": "data",
        "endpoints": []
    },
    {
        "name": "OSINERGMIN Endpoint",
        "type": "external",
        "endpoints": ["HTTPS/TLS XML/JSON"]
    }
]


class InfoService:
    """Servicio de información de la arquitectura"""
    
    @staticmethod
    def obtener_servicios() -> List[Dict[str, Any]]:
        """
        Retorna el catálogo de servicios y endpoints de SISCAL.
        Los microservicios marcados como 'futuro' se implementarán progresivamente.
        """
        return CATALOGO_SERVICIOS
