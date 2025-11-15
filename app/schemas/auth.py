"""
SISCAL - Luz del Sur
Schemas Pydantic para autenticación
"""
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Schema para crear un usuario"""
    email: EmailStr
    password: str
    roles: Optional[List[str]] = ["CLIENTE"]  # Por defecto CLIENTE


class UserOut(BaseModel):
    """Schema de salida de usuario (sin contraseña)"""
    id_usuario: int
    email: str
    roles: List[str]
    estado: str
    
    class Config:
        from_attributes = True


class LoginIn(BaseModel):
    """Schema para login"""
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    """Schema de respuesta de tokens"""
    access_token: str
    token_type: str = "bearer"
    refresh_token: str
    expires_in: int  # Segundos hasta expiración del access_token


class RefreshIn(BaseModel):
    """Schema para refrescar token"""
    refresh_token: str
