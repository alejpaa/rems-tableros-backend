"""
Rutas API para la gestión de Tableros Eléctricos.
Compatible con Neon PostgreSQL y SQLModel.
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.models import (
    TableroElectrico,
    TableroElectricoCreate,
    TableroElectricoRead,
    TableroElectricoUpdate,
)
from app.core.db import get_session

router = APIRouter(prefix="/api/v1/tableros", tags=["Tableros Eléctricos"])


# ============================
# 🔹 Crear Tablero Eléctrico
# ============================
@router.post(
    "/",
    response_model=TableroElectricoRead,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo tablero eléctrico",
)
def crear_tablero(
    tablero: TableroElectricoCreate,
    session: Session = Depends(get_session)
) -> TableroElectricoRead:
    """Crea un nuevo tablero eléctrico en la base de datos."""
    db_tablero = TableroElectrico.from_orm(tablero)
    session.add(db_tablero)
    session.commit()
    session.refresh(db_tablero)
    return db_tablero


# ============================
# 🔹 Listar todos los Tableros
# ============================
@router.get(
    "/",
    response_model=List[TableroElectricoRead],
    summary="Listar todos los tableros eléctricos",
)
def listar_tableros(session: Session = Depends(get_session)) -> List[TableroElectricoRead]:
    """Devuelve una lista de todos los tableros eléctricos registrados."""
    statement = select(TableroElectrico)
    results = session.exec(statement).all()
    return results


# ============================
# 🔹 Obtener un Tablero por ID
# ============================
@router.get(
    "/{tablero_id}",
    response_model=TableroElectricoRead,
    summary="Obtener un tablero eléctrico por ID",
)
def obtener_tablero(tablero_id: UUID, session: Session = Depends(get_session)) -> TableroElectricoRead:
    """Obtiene un tablero específico por su ID."""
    tablero = session.get(TableroElectrico, tablero_id)
    if not tablero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )
    return tablero


# ============================
# 🔹 Actualizar un Tablero
# ============================
@router.put(
    "/{tablero_id}",
    response_model=TableroElectricoRead,
    summary="Actualizar un tablero eléctrico existente",
)
def actualizar_tablero(
    tablero_id: UUID,
    tablero_update: TableroElectricoUpdate,
    session: Session = Depends(get_session)
) -> TableroElectricoRead:
    """Actualiza un tablero eléctrico existente por ID."""
    tablero = session.get(TableroElectrico, tablero_id)
    if not tablero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )

    # Solo actualiza los campos enviados
    update_data = tablero_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(tablero, key, value)

    session.add(tablero)
    session.commit()
    session.refresh(tablero)
    return tablero


# ============================
# 🔹 Eliminar un Tablero
# ============================
@router.delete(
    "/{tablero_id}",
    status_code=status.HTTP_200_OK,
    summary="Eliminar un tablero eléctrico",
)
def eliminar_tablero(tablero_id: UUID, session: Session = Depends(get_session)) -> dict:
    """Elimina un tablero eléctrico por ID."""
    tablero = session.get(TableroElectrico, tablero_id)
    if not tablero:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tablero con ID {tablero_id} no encontrado"
        )

    session.delete(tablero)
    session.commit()
    return {"mensaje": f"Tablero {tablero_id} eliminado correctamente"}
