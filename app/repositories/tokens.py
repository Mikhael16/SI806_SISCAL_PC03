"""
SISCAL - Luz del Sur
Repository: Tokens de refresco
"""
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshToken


class TokensRepository:
    """Repositorio para operaciones con tokens de refresco"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def guardar(self, id_usuario: int, token: str, expira_en: datetime) -> RefreshToken:
        """Guarda un refresh token en la base de datos"""
        refresh_token = RefreshToken(
            id_usuario=id_usuario,
            token=token,
            expira_en=expira_en
        )
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token
    
    def obtener_por_token(self, token: str) -> Optional[RefreshToken]:
        """Busca un refresh token"""
        return self.db.query(RefreshToken).filter(RefreshToken.token == token).first()
    
    def eliminar(self, token: str) -> None:
        """Elimina un refresh token (logout)"""
        self.db.query(RefreshToken).filter(RefreshToken.token == token).delete()
        self.db.commit()
    
    def limpiar_expirados(self) -> None:
        """Elimina tokens expirados"""
        self.db.query(RefreshToken).filter(RefreshToken.expira_en < datetime.utcnow()).delete()
        self.db.commit()
