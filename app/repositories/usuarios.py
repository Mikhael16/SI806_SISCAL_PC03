"""
SISCAL - Luz del Sur
Repository: Usuarios
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.models.usuario_rol import UsuarioRol
from app.models.rol import Rol


class UsuariosRepository:
    """Repositorio para operaciones CRUD de usuarios"""
    
    def __init__(self, db: Session):
        self.db = db
    
    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        """Busca un usuario por email"""
        return self.db.query(Usuario).filter(Usuario.email == email).first()
    
    def obtener_por_id(self, id_usuario: int) -> Optional[Usuario]:
        """Busca un usuario por ID"""
        return self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
    
    def crear(self, email: str, password_hash: str) -> Usuario:
        """Crea un nuevo usuario"""
        usuario = Usuario(
            email=email,
            password_hash=password_hash,
            estado='A'
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario
    
    def obtener_roles(self, id_usuario: int) -> List[str]:
        """Obtiene los códigos de roles de un usuario"""
        roles = (
            self.db.query(Rol.codigo)
            .join(UsuarioRol, UsuarioRol.id_rol == Rol.id_rol)
            .filter(UsuarioRol.id_usuario == id_usuario)
            .all()
        )
        return [r[0] for r in roles]
