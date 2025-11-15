"""
SISCAL - Luz del Sur
Configuración de la aplicación
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Configuración general de la aplicación"""
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "un_valor_aleatorio_largo_cambiar_en_produccion")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7  # Tokens de refresco duran 7 días
    
    # Base de datos
    DB_ENGINE: str = os.getenv("DB_ENGINE", "postgres")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "si806")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "123456")


settings = Settings()
