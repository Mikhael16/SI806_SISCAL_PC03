"""
SISCAL - Luz del Sur
Sesión de base de datos PostgreSQL
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Construir la URL de conexión con codificación explícita
import urllib.parse

# Codificar la contraseña para evitar problemas con caracteres especiales
password_encoded = urllib.parse.quote_plus(settings.DB_PASSWORD)

DATABASE_URL = (
    f"postgresql://{settings.DB_USER}:{password_encoded}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?client_encoding=utf8"
)

# Motor de base de datos con configuración de codificación
engine = create_engine(
    DATABASE_URL, 
    pool_pre_ping=True, 
    echo=False,
    isolation_level="AUTOCOMMIT"
)

# Sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    Dependencia para obtener sesión de BD.
    Uso: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
