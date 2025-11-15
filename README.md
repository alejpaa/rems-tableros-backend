# API Gestión de Tableros Eléctricos - Backend

> Sistema de gestión de tableros eléctricos con API RESTful

Una API backend moderna y robusta construida con **FastAPI** y **SQLModel** para la gestión completa de tableros eléctricos, incluyendo operaciones CRUD, validaciones de datos y persistencia en base de datos PostgreSQL (Neon).

---

## Características

- ✅ **API RESTful completa** con operaciones CRUD
- ✅ **Validaciones automáticas** de datos de entrada con Pydantic
- ✅ **Base de datos PostgreSQL** (Neon) con SQLModel/SQLAlchemy
- ✅ **Documentación interactiva** automática con Swagger UI
- ✅ **CORS configurado** para permitir integraciones frontend
- ✅ **Manejo de errores** consistente y detallado
- ✅ **Arquitectura modular** y escalable
- ✅ **Type hints completos** para mejor desarrollo y mantenimiento

---

## Tecnologías

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.11+ | Lenguaje de programación |
| **FastAPI** | 0.121.1 | Framework web moderno y rápido |
| **SQLModel** | 0.0.27 | ORM con integración Pydantic |
| **PostgreSQL** | - | Base de datos (Neon) |
| **Pydantic** | 2.12.4 | Validación de datos |
| **Uvicorn** | 0.38.0 | Servidor ASGI |

---

## Requisitos Previos

- **Python 3.11** o superior
- **PostgreSQL** (o acceso a Neon Database)
- **Git**

---


## 📡 API Endpoints

### Base URL: `/api/v1/tableros`

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/` | Crear un nuevo tablero eléctrico |
| `GET` | `/` | Listar todos los tableros (ordenados por fecha de creación) |
| `GET` | `/{tablero_id}` | Obtener un tablero específico por ID |
| `PUT` | `/{tablero_id}` | Actualizar un tablero existente |
| `DELETE` | `/{tablero_id}` | Eliminar un tablero |

### Ejemplo de Petición (Crear Tablero)

```bash
curl -X POST "http://localhost:8000/api/v1/tableros/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Tablero Principal Piso 1",
    "ubicacion": "Sala de máquinas",
    "marca": "Schneider Electric",
    "capacidad_amperios": 200.0,
    "estado": "Operativo",
    "ano_fabricacion": 2022,
    "ano_instalacion": 2023
  }'
```

### Ejemplo de Respuesta

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "nombre": "Tablero Principal Piso 1",
  "ubicacion": "Sala de máquinas",
  "marca": "Schneider Electric",
  "capacidad_amperios": 200.0,
  "estado": "Operativo",
  "ano_fabricacion": 2022,
  "ano_instalacion": 2023,
  "created_at": "2025-11-15T10:30:00.000Z"
}
```

---

## 📁 Estructura del Proyecto

```
rems-tableros-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── models.py               # Modelos SQLModel y esquemas Pydantic
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes_root.py      # Router principal
│   │   └── route_tableros.py   # Endpoints de tableros eléctricos
│   └── core/
│       ├── __init__.py
│       ├── config.py           # Configuración de la aplicación
│       └── db.py               # Configuración de base de datos
├── requirements.txt            # Dependencias Python
└── README.md                   # Documentación
```

---

## Modelo de Datos

### Tablero Eléctrico

| Campo | Tipo | Requerido | Validaciones | Descripción |
|-------|------|-----------|--------------|-------------|
| `id` | UUID | Auto | Primary Key | Identificador único |
| `nombre` | String | Sí | 1-255 caracteres | Nombre del tablero |
| `ubicacion` | String | Sí | 1-255 caracteres | Ubicación física |
| `marca` | String | No | Max 255 caracteres | Marca del fabricante |
| `capacidad_amperios` | Float | Sí | > 0 | Capacidad en amperios |
| `estado` | String | No | Default: "Operativo" | Estado actual |
| `ano_fabricacion` | Integer | Sí | 1900-2025 | Año de fabricación |
| `ano_instalacion` | Integer | Sí | 1900-2025 | Año de instalación |
| `created_at` | DateTime | Auto | - | Fecha de creación del registro |

**Estados válidos**: `Operativo`, `Mantenimiento`, `Fuera de Servicio`

---


