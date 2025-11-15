"""
SISCAL - Luz del Sur
Repository: Historial de logins
"""
from typing import Optional
from sqlalchemy.orm import Session
from app.models.login_historial import LoginHistorial


class LoginsRepository:
    """Repositorio para el historial de inicios de sesión"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def registrar(self, id_usuario: int, ip: Optional[str] = None, user_agent: Optional[str] = None) -> LoginHistorial:
        """Registra un inicio de sesión"""
        login = LoginHistorial(
            id_usuario=id_usuario,
            ip=ip,
            user_agent=user_agent
        )
        self.db.add(login)
        self.db.commit()
        self.db.refresh(login)
        return login
