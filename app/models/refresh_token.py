"""
SISCAL - Luz del Sur
Modelo: Refresh Token
"""
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from app.db.base import Base


class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id_token = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"), nullable=False, index=True)
    token = Column(String(512), unique=True, nullable=False)
    expira_en = Column(TIMESTAMP, nullable=False)
