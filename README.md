# Task Manager API v2

REST API para gestión de tareas construida con FastAPI, PostgreSQL y SQLAlchemy.

## Stack

- **FastAPI** — framework web moderno y de alto rendimiento
- **PostgreSQL** — base de datos relacional
- **SQLAlchemy** — ORM para mapeo objeto-relacional
- **Alembic** — manejo de migraciones de base de datos
- **Pydantic** — validación automática de datos
- **Uvicorn** — servidor ASGI

## Características

✅ CRUD completo de tareas  
✅ Filtros por query params  
✅ Persistencia en base de datos PostgreSQL  
✅ Migraciones con Alembic  
✅ Validación de datos con Pydantic  
✅ Documentación interactiva automática (Swagger)

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/tasks` | Listar todas las tareas |
| GET | `/tasks/{id}` | Obtener una tarea por ID |
| POST | `/tasks` | Crear una nueva tarea |
| PUT | `/tasks/{id}` | Actualizar una tarea |
| DELETE | `/tasks/{id}` | Eliminar una tarea |

### Filtros disponibles en GET /tasks
```
GET /tasks?completada=true
GET /tasks?prioridad=2
GET /tasks?completada=false&prioridad=1
```

## Requisitos previos

- Python 3.10+
- PostgreSQL 15+ instalado y corriendo

## Cómo correr el proyecto localmente

**1. Clonar el repositorio**
```bash
git clone https://github.com/martinjimenez04/task-manager-api.git
cd task-manager-api
```

**2. Crear y activar el entorno virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

**4. Configurar variables de entorno**

Crear un archivo `.env` en la raíz del proyecto:
```env
DATABASE_URL=postgresql://postgres:tu_password@localhost:5432/task_manager_db
```

Reemplazar `tu_password` con tu contraseña de PostgreSQL.

**5. Crear la base de datos**

En PostgreSQL (usando pgAdmin o psql):
```sql
CREATE DATABASE task_manager_db;
```

**6. Ejecutar las migraciones**
```bash
alembic upgrade head
```

**7. Correr el servidor**
```bash
uvicorn main:app --reload
```

**8. Abrir la documentación interactiva**
```
http://localhost:8000/docs
```

## Estructura del proyecto
```
task-manager-api/
├── alembic/              # Migraciones de base de datos
│   └── versions/
├── app/
│   ├── database.py       # Configuración de SQLAlchemy
│   ├── models/
│   │   └── task.py       # Modelo SQLAlchemy (tabla)
│   ├── routers/
│   │   └── tasks.py      # Endpoints de la API
│   └── schemas/
│       └── task.py       # Schemas Pydantic (validación)
├── .env                  # Variables de entorno (no se sube a GitHub)
├── .gitignore
├── alembic.ini           # Configuración de Alembic
├── main.py              
└── requirements.txt     
```

## Migraciones

**Crear una nueva migración:**
```bash
alembic revision --autogenerate -m "descripcion del cambio"
```

**Aplicar migraciones:**
```bash
alembic upgrade head
```

**Revertir última migración:**
```bash
alembic downgrade -1
```

## Próximas mejoras (v3)

- [ ] Autenticación con JWT
- [ ] Relación con tabla Users (cada usuario sus tareas)
- [ ] Tests con pytest
- [ ] Dockerización
- [ ] CI/CD con GitHub Actions