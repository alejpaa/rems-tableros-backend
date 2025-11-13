"""
Esquemas y modelo SQLModel para Tablero Eléctrico.
Incluye validación, creación, lectura y actualización.
"""

from typing import Optional
from uuid import uuid4
from sqlmodel import SQLModel, Field


# ==========================
# Modelo principal (Tabla)
# ==========================
class TableroElectrico(SQLModel, table=True):
    """
    Modelo de base de datos para Tablero Eléctrico.
    Representa un tablero con sus especificaciones técnicas.
    """
    __tablename__ = "tableros_electricos"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    nombre: str = Field(..., min_length=1, max_length=255, description="Nombre del tablero")
    ubicacion: str = Field(..., min_length=1, max_length=255, description="Ubicación del tablero")
    marca: Optional[str] = Field(None, max_length=255, description="Marca del tablero")
    capacidad_amperios: float = Field(..., gt=0, description="Capacidad en amperios")
    estado: str = Field(
        default="Operativo",
        description="Estado: Operativo, Mantenimiento o Fuera de Servicio"
    )
    ano_fabricacion: int = Field(..., ge=1900, le=2100, description="Año de fabricación")
    ano_instalacion: int = Field(..., ge=1900, le=2100, description="Año de instalación")


# ==========================
# Esquemas Pydantic
# ==========================
class TableroElectricoBase(SQLModel):
    """Propiedades compartidas entre creación y lectura."""
    nombre: str = Field(..., min_length=1, max_length=255)
    ubicacion: str = Field(..., min_length=1, max_length=255)
    marca: Optional[str] = Field(None, max_length=255)
    capacidad_amperios: float = Field(..., gt=0)
    estado: Optional[str] = Field(default="Operativo")
    ano_fabricacion: int = Field(..., ge=1900, le=2100)
    ano_instalacion: int = Field(..., ge=1900, le=2100)


class TableroElectricoCreate(TableroElectricoBase):
    """Esquema para crear un nuevo Tablero Eléctrico."""
    pass


class TableroElectricoUpdate(SQLModel):
    """Esquema para actualizar un Tablero Eléctrico existente."""
    nombre: Optional[str] = Field(None, min_length=1, max_length=255)
    ubicacion: Optional[str] = Field(None, min_length=1, max_length=255)
    marca: Optional[str] = Field(None, max_length=255)
    capacidad_amperios: Optional[float] = Field(None, gt=0)
    estado: Optional[str] = None
    ano_fabricacion: Optional[int] = Field(None, ge=1900, le=2100)
    ano_instalacion: Optional[int] = Field(None, ge=1900, le=2100)


class TableroElectricoRead(TableroElectricoBase):
    """Esquema para lectura (respuesta en API)."""
    id: str

    class Config:
        from_attributes = True
