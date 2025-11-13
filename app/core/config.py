"""
Configuración de la aplicación usando Pydantic Settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Configuración de la aplicación"""
    
    # FastAPI Configuration
    environment: str = "development"
    debug: bool = True
    api_title: str = "API Gestión de Tableros Eléctricos"
    api_version: str = "1.0.0"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database Configuration - Neon PostgreSQL
    database_url: str = "postgresql+psycopg://user:password@host/dbname"
    
    # Logging
    log_level: str = "INFO"
    
    class Config:
        """Configuración de Pydantic"""
        env_file = ".env"
        case_sensitive = False


# Instancia global de configuración
settings = Settings()
