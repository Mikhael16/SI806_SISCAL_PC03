"""
SISCAL - Luz del Sur
Service: Autenticación
"""
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import (
    verify_password, 
    get_password_hash, 
    create_access_token,
    create_refresh_token
)
from app.repositories.usuarios import UsuariosRepository
from app.repositories.roles import RolesRepository
from app.repositories.tokens import TokensRepository
from app.repositories.logins import LoginsRepository
from app.schemas.auth import UserCreate, UserOut, LoginIn, TokenOut


class AuthService:
    """Servicio de autenticación"""
    
    def __init__(self, db: Session):
        self.db = db
        self.usuarios_repo = UsuariosRepository(db)
        self.roles_repo = RolesRepository(db)
        self.tokens_repo = TokensRepository(db)
        self.logins_repo = LoginsRepository(db)
    
    def register(self, user_data: UserCreate) -> UserOut:
        """
        Registra un nuevo usuario en el sistema.
        Por defecto asigna el rol CLIENTE si no se especifica otro.
        """
        # Verificar que el email no exista
        usuario_existente = self.usuarios_repo.obtener_por_email(user_data.email)
        if usuario_existente:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El email ya está registrado"
            )
        
        # Hashear contraseña
        password_hash = get_password_hash(user_data.password)
        
        # Crear usuario
        usuario = self.usuarios_repo.crear(
            email=user_data.email,
            password_hash=password_hash
        )
        
        # Asignar roles
        roles_codigos = user_data.roles or ["CLIENTE"]
        roles = self.roles_repo.obtener_por_codigos(roles_codigos)
        
        if not roles:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Los roles especificados no son válidos"
            )
        
        for rol in roles:
            self.roles_repo.asignar_rol_a_usuario(usuario.id_usuario, rol.id_rol)
        
        # Obtener roles asignados para respuesta
        roles_usuario = self.usuarios_repo.obtener_roles(usuario.id_usuario)
        
        return UserOut(
            id_usuario=usuario.id_usuario,
            email=usuario.email,
            roles=roles_usuario,
            estado=usuario.estado
        )
    
    def login(
        self, 
        credentials: LoginIn, 
        ip: Optional[str] = None, 
        user_agent: Optional[str] = None
    ) -> TokenOut:
        """
        Autentica un usuario y genera tokens de acceso y refresco.
        Registra el login en el historial.
        """
        # Buscar usuario
        usuario = self.usuarios_repo.obtener_por_email(credentials.email)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
        
        # Verificar estado
        if usuario.estado != 'A':
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario inactivo"
            )
        
        # Verificar contraseña
        if not verify_password(credentials.password, usuario.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos"
            )
        
        # Obtener roles
        roles = self.usuarios_repo.obtener_roles(usuario.id_usuario)
        
        # Generar access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": usuario.id_usuario, "email": usuario.email, "roles": roles},
            expires_delta=access_token_expires
        )
        
        # Generar refresh token
        refresh_token_expires = timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = create_refresh_token(
            data={"sub": usuario.id_usuario},
            expires_delta=refresh_token_expires
        )
        
        # Guardar refresh token en BD
        expira_en = datetime.utcnow() + refresh_token_expires
        self.tokens_repo.guardar(usuario.id_usuario, refresh_token, expira_en)
        
        # Registrar login en historial
        self.logins_repo.registrar(usuario.id_usuario, ip, user_agent)
        
        return TokenOut(
            access_token=access_token,
            token_type="bearer",
            refresh_token=refresh_token,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    
    def refresh(self, refresh_token: str) -> TokenOut:
        """
        Genera un nuevo access token usando un refresh token válido.
        """
        # Buscar token en BD
        token_db = self.tokens_repo.obtener_por_token(refresh_token)
        if not token_db:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token inválido"
            )
        
        # Verificar expiración
        if token_db.expira_en < datetime.utcnow():
            self.tokens_repo.eliminar(refresh_token)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token expirado"
            )
        
        # Obtener usuario
        usuario = self.usuarios_repo.obtener_por_id(token_db.id_usuario)
        if not usuario or usuario.estado != 'A':
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Usuario inválido o inactivo"
            )
        
        # Obtener roles
        roles = self.usuarios_repo.obtener_roles(usuario.id_usuario)
        
        # Generar nuevo access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": usuario.id_usuario, "email": usuario.email, "roles": roles},
            expires_delta=access_token_expires
        )
        
        return TokenOut(
            access_token=access_token,
            token_type="bearer",
            refresh_token=refresh_token,  # El mismo refresh token
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
