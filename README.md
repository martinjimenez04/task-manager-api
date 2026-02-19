# Task Manager API v3

REST API para gestión de tareas con autenticación JWT, construida con FastAPI, PostgreSQL y SQLAlchemy.

## Stack

- **FastAPI** — framework web moderno y de alto rendimiento
- **PostgreSQL** — base de datos relacional
- **SQLAlchemy** — ORM para mapeo objeto-relacional
- **Alembic** — manejo de migraciones de base de datos
- **JWT** — autenticación con tokens
- **Bcrypt** — hash seguro de contraseñas
- **Pydantic** — validación automática de datos
- **Uvicorn** — servidor ASGI

## Características

✅ Sistema completo de autenticación con JWT  
✅ Registro y login de usuarios  
✅ Hash de contraseñas con bcrypt  
✅ Endpoints protegidos (requieren autenticación)  
✅ Aislamiento de datos por usuario  
✅ CRUD completo de tareas  
✅ Filtros por query params  
✅ Persistencia en PostgreSQL  
✅ Migraciones con Alembic  
✅ Validación de datos con Pydantic  
✅ Documentación interactiva automática (Swagger)

## Endpoints

### Autenticación

| Método | Ruta | Descripción | Autenticación |
|--------|------|-------------|---------------|
| POST | `/auth/register` | Registrar nuevo usuario | No |
| POST | `/auth/login` | Iniciar sesión (obtener token) | No |

### Tareas (requieren autenticación)

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/tasks` | Listar tareas del usuario |
| GET | `/tasks/{id}` | Obtener una tarea por ID |
| POST | `/tasks` | Crear nueva tarea |
| PUT | `/tasks/{id}` | Actualizar tarea |
| DELETE | `/tasks/{id}` | Eliminar tarea |

### Filtros disponibles en GET /tasks
```
GET /tasks?completada=true
GET /tasks?prioridad=2
GET /tasks?completada=false&prioridad=1
```

## Requisitos previos

- Python 3.10+
- PostgreSQL 15+ instalado y corriendo

## Instalación y configuración

### 1. Clonar el repositorio
```bash
git clone https://github.com/martinjimenez04/task-manager-api.git
cd task-manager-api
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:
```env
DATABASE_URL=postgresql://postgres:tu_password@localhost:5432/task_manager_db
SECRET_KEY=tu_clave_secreta_super_larga_y_aleatoria
```

**Nota:** En producción, genera una SECRET_KEY fuerte con:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Crear la base de datos

En PostgreSQL (usando pgAdmin o psql):
```sql
CREATE DATABASE task_manager_db;
```

### 6. Ejecutar las migraciones
```bash
alembic upgrade head
```

### 7. Correr el servidor
```bash
uvicorn main:app --reload
```

### 8. Abrir la documentación interactiva
```
http://localhost:8000/docs
```

## Uso de la API

### 1. Registrar un usuario
```bash
POST /auth/register
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "contraseña_segura"
}
```

### 2. Iniciar sesión
```bash
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=usuario@example.com
password=contraseña_segura
```

Respuesta:
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

### 3. Usar el token en requests protegidos

Incluir el header en todas las peticiones a `/tasks`:
```
Authorization: Bearer eyJhbGci...
```

## Estructura del proyecto
```
task-manager-api/
├── alembic/              # Migraciones de base de datos
│   └── versions/
├── app/
│   ├── core/
│   │   ├── config.py     # Configuración (SECRET_KEY, etc)
│   │   └── security.py   # Funciones de JWT y bcrypt
│   ├── models/
│   │   ├── user.py       # Modelo User
│   │   └── task.py       # Modelo Task
│   ├── routers/
│   │   ├── auth.py       # Endpoints de autenticación
│   │   └── tasks.py      # Endpoints de tareas
│   ├── schemas/
│   │   ├── user.py       # Schemas Pydantic de User
│   │   ├── task.py       # Schemas Pydantic de Task
│   │   └── token.py      # Schemas de JWT
│   ├── database.py       # Configuración de SQLAlchemy
│   └── dependencies.py   # get_current_user
├── .env                  # Variables de entorno
├── .gitignore
├── alembic.ini           # Configuración de Alembic
├── main.py              
└── requirements.txt     
```

## Seguridad

- ✅ Contraseñas hasheadas con bcrypt
- ✅ Tokens JWT firmados con SECRET_KEY
- ✅ Tokens con expiración (7 días por defecto)
- ✅ Validación de tokens en cada request protegido
- ✅ Aislamiento de datos: cada usuario solo ve sus propias tareas
- ✅ Variables sensibles en `.env` 

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

## Próximas mejoras (v4)

- [ ] Refresh tokens
- [ ] Roles y permisos (admin/user)
- [ ] Tests con pytest
- [ ] Dockerización
- [ ] CI/CD con GitHub Actions
- [ ] Rate limiting
- [ ] Paginación en listados

## Autor

**Martin Jimenez**  
Estudiante de Ingeniería en Sistemas de Información - UTN FRC

GitHub: [@martinjimenez04](https://github.com/martinjimenez04)