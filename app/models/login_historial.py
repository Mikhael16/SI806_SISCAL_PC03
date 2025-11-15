"""
SISCAL - Luz del Sur
Modelo: Login Historial
"""
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base


class LoginHistorial(Base):
    __tablename__ = "login_historial"

    id_login = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"), nullable=False, index=True)
    ip = Column(String(64), nullable=True)
    user_agent = Column(String(256), nullable=True)
    creado_en = Column(TIMESTAMP, nullable=False, server_default=func.now(), index=True)
