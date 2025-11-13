"""
Configuración de la base de datos Neon PostgreSQL.
Usa el driver psycopg2 para conexiones sincrónicas con SQLModel.
"""

from sqlmodel import SQLModel, create_engine, Session
from config import settings

# Crear engine sincrónico para Neon PostgreSQL
# SQLModel internamente usa SQLAlchemy, por lo tanto `create_engine` es compatible.
engine = create_engine(
    settings.database_url,
    echo=settings.debug,        # Muestra las consultas SQL si debug=True
    future=True,                # Activa el estilo moderno de SQLAlchemy
    pool_size=5,                # Tamaño del pool de conexiones
    max_overflow=10,            # Conexiones extra si se satura el pool
    connect_args={              # Argumentos adicionales
        "connect_timeout": 10,
    }
)


def init_db() -> None:
    """
    Inicializa la base de datos:
    crea todas las tablas definidas en los modelos SQLModel.
    """
    SQLModel.metadata.create_all(engine)
    print("Tablas creadas/verificadas exitosamente en Neon PostgreSQL.")


def get_session():
    """
    Dependencia para FastAPI:
    devuelve una sesión de base de datos y la cierra al finalizar.
    """
    with Session(engine) as session:
        yield session
