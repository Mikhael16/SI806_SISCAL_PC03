"""
SISCAL - Luz del Sur
Modelo: Usuario
"""
from sqlalchemy import Column, Integer, String, CHAR, TIMESTAMP
from sqlalchemy.sql import func
from app.db.base import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    estado = Column(CHAR(1), nullable=False, default='A', index=True)
    creado_en = Column(TIMESTAMP, nullable=False, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=False, server_default=func.now(), onupdate=func.now())
