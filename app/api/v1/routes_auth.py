"""
SISCAL - Luz del Sur
Routes: Autenticación
"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import get_current_user
from app.services.auth_service import AuthService
from app.schemas.auth import UserCreate, UserOut, LoginIn, TokenOut, RefreshIn
from app.models.usuario import Usuario

router = APIRouter(prefix="/api/v1/auth", tags=["Autenticación"])


@router.post("/register", response_model=UserOut, status_code=201)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en el sistema.
    Por defecto asigna el rol CLIENTE.
    """
    service = AuthService(db)
    return service.register(user_data)


@router.post("/login", response_model=TokenOut)
def login(credentials: LoginIn, request: Request, db: Session = Depends(get_db)):
    """
    Autentica un usuario y retorna tokens de acceso y refresco.
    Registra la IP y user agent en el historial.
    """
    # Extraer IP y user agent
    ip = request.client.host if request.client else None
    user_agent = request.headers.get("user-agent", None)
    
    service = AuthService(db)
    return service.login(credentials, ip, user_agent)


@router.post("/refresh", response_model=TokenOut)
def refresh(refresh_data: RefreshIn, db: Session = Depends(get_db)):
    """
    Genera un nuevo access token usando un refresh token válido.
    """
    service = AuthService(db)
    return service.refresh(refresh_data.refresh_token)


@router.get("/me", response_model=UserOut)
def me(current_user: Usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Retorna la información del usuario autenticado actual.
    Requiere token de acceso válido.
    """
    from app.repositories.usuarios import UsuariosRepository
    
    repo = UsuariosRepository(db)
    roles = repo.obtener_roles(current_user.id_usuario)
    
    return UserOut(
        id_usuario=current_user.id_usuario,
        email=current_user.email,
        roles=roles,
        estado=current_user.estado
    )
