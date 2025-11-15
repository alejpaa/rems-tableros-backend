"""
Esquemas y modelo SQLModel para Tablero Eléctrico.
Incluye validación, creación, lectura y actualización.
"""

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone
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

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: str = Field(..., min_length=1, max_length=255, description="Nombre del tablero (ej. 'Tablero Piso 1 - Ala Norte')")
    ubicacion: str = Field(..., min_length=1, max_length=255, description="Ubicación del tablero (ej. 'Sala de máquinas, Sótano 1')")
    marca: Optional[str] = Field(None, max_length=255, description="Marca del tablero (opcional)")
    capacidad_amperios: float = Field(..., gt=0, description="Capacidad del tablero en amperios (ej. 100)")
    estado: str = Field(
        default="Operativo",
        description="Estado del tablero (Operativo, Mantenimiento o Fuera de Servicio)"
    )
    ano_fabricacion: int = Field(..., ge=1900, le=2100, description="Año de fabricación (ej. 2020)")
    ano_instalacion: int = Field(..., ge=1900, le=2100, description="Año de instalación (ej. 2021)")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),description="Fecha y hora de creación del registro"
)


# ==========================
# Esquemas Pydantic / API
# ==========================
class TableroElectricoBase(SQLModel):
    """Propiedades compartidas entre creación, lectura y actualización."""
    nombre: str = Field(..., min_length=1, max_length=255)
    ubicacion: str = Field(..., min_length=1, max_length=255)
    marca: Optional[str] = Field(None, max_length=255)
    capacidad_amperios: float = Field(..., gt=0)
    estado: Optional[str] = Field(default="Operativo")
    ano_fabricacion: int = Field(..., ge=1900, le=2100)
    ano_instalacion: int = Field(..., ge=1900, le=2100)


class TableroElectricoCreate(TableroElectricoBase):
    """Esquema para creación de un Tablero Eléctrico."""
    pass


class TableroElectricoUpdate(SQLModel):
    """Esquema para actualización parcial de un Tablero Eléctrico."""
    nombre: Optional[str] = Field(None, min_length=1, max_length=255)
    ubicacion: Optional[str] = Field(None, min_length=1, max_length=255)
    marca: Optional[str] = Field(None, max_length=255)
    capacidad_amperios: Optional[float] = Field(None, gt=0)
    estado: Optional[str] = None
    ano_fabricacion: Optional[int] = Field(None, ge=1900, le=2100)
    ano_instalacion: Optional[int] = Field(None, ge=1900, le=2100)


class TableroElectricoRead(TableroElectricoBase):
    """Esquema para lectura (respuesta en API)."""
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
