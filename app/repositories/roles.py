"""
SISCAL - Luz del Sur
Repository: Roles
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.rol import Rol
from app.models.usuario_rol import UsuarioRol


class RolesRepository:
    """Repositorio para operaciones con roles"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def obtener_por_codigo(self, codigo: str) -> Optional[Rol]:
        """Busca un rol por código"""
        return self.db.query(Rol).filter(Rol.codigo == codigo).first()
    
    def obtener_por_codigos(self, codigos: List[str]) -> List[Rol]:
        """Busca múltiples roles por códigos"""
        return self.db.query(Rol).filter(Rol.codigo.in_(codigos)).all()
    
    def asignar_rol_a_usuario(self, id_usuario: int, id_rol: int) -> None:
        """Asigna un rol a un usuario"""
        usuario_rol = UsuarioRol(id_usuario=id_usuario, id_rol=id_rol)
        self.db.add(usuario_rol)
        self.db.commit()
