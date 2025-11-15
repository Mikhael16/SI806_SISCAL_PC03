"""
SISCAL - Luz del Sur
Modelo: Usuario_Rol (relación muchos a muchos)
"""
from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base


class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"), primary_key=True)
    id_rol = Column(Integer, ForeignKey("rol.id_rol", ondelete="RESTRICT"), primary_key=True)
