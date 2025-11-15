"""
SISCAL - Luz del Sur
Modelo: Rol
"""
from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Rol(Base):
    __tablename__ = "rol"

    id_rol = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(40), unique=True, nullable=False, index=True)
    nombre = Column(String(80), nullable=False)
