# Task Manager API

REST API para gestión de tareas construida con FastAPI y Python.

## Stack

- **FastAPI** — framework web moderno y de alto rendimiento
- **Pydantic** — validación automática de datos
- **Uvicorn** — servidor ASGI

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

**4. Correr el servidor**
```bash
uvicorn main:app --reload
```

**5. Abrir la documentación interactiva**
```
http://localhost:8000/docs
```

## Estructura del proyecto
```
task-manager-api/
├── main.py              
├── requirements.txt     
├── .gitignore           
└── app/
    ├── routers/
    │   └── tasks.py     
    └── schemas/
        └── task.py      
```

## Próximas mejoras

- [ ] Persistencia con PostgreSQL + SQLAlchemy
- [ ] Autenticación con JWT
- [ ] Tests con pytest
- [ ] Dockerización