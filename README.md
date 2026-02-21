# Task Manager API v3

REST API for task management with JWT authentication, built with FastAPI, PostgreSQL, and SQLAlchemy.

## Tech Stack

- **FastAPI** — Modern, high-performance web framework
- **PostgreSQL** — Relational database
- **SQLAlchemy** — Object-Relational Mapping (ORM)
- **Alembic** — Database migration management
- **JWT** — Token-based authentication
- **Bcrypt** — Secure password hashing
- **Pydantic** — Automatic data validation
- **Uvicorn** — ASGI server

## Features

✅ Complete JWT authentication system  
✅ User registration and login  
✅ Bcrypt password hashing  
✅ Protected endpoints (require authentication)  
✅ User data isolation  
✅ Full CRUD operations for tasks  
✅ Query parameter filters  
✅ PostgreSQL persistence  
✅ Database migrations with Alembic  
✅ Pydantic data validation  
✅ Automatic interactive documentation (Swagger)

## Endpoints

### Authentication

| Method | Route | Description | Authentication |
|--------|-------|-------------|----------------|
| POST | `/auth/register` | Register new user | No |
| POST | `/auth/login` | Login (get token) | No |

### Tasks (authentication required)

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/tasks` | List user's tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create new task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

### Available filters for GET /tasks
```
GET /tasks?completada=true
GET /tasks?prioridad=2
GET /tasks?completada=false&prioridad=1
```

## Prerequisites

- Python 3.10+
- PostgreSQL 15+ installed and running

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/martinjimenez04/task-manager-api.git
cd task-manager-api
```

### 2. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/task_manager_db
SECRET_KEY=your_super_long_and_random_secret_key
```

**Note:** In production, generate a strong SECRET_KEY with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Create the database

In PostgreSQL (using pgAdmin or psql):
```sql
CREATE DATABASE task_manager_db;
```

### 6. Run migrations
```bash
alembic upgrade head
```

### 7. Start the server
```bash
uvicorn main:app --reload
```

### 8. Open interactive documentation
```
http://localhost:8000/docs
```

## API Usage

### 1. Register a user
```bash
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "secure_password"
}
```

### 2. Login
```bash
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com
password=secure_password
```

Response:
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

### 3. Use token in protected requests

Include the header in all requests to `/tasks`:
```
Authorization: Bearer eyJhbGci...
```

## Project Structure
```
task-manager-api/
├── alembic/              # Database migrations
│   └── versions/
├── app/
│   ├── core/
│   │   ├── config.py     # Configuration (SECRET_KEY, etc)
│   │   └── security.py   # JWT and bcrypt functions
│   ├── models/
│   │   ├── user.py       # User model
│   │   └── task.py       # Task model
│   ├── routers/
│   │   ├── auth.py       # Authentication endpoints
│   │   └── tasks.py      # Task endpoints
│   ├── schemas/
│   │   ├── user.py       # User Pydantic schemas
│   │   ├── task.py       # Task Pydantic schemas
│   │   └── token.py      # JWT schemas
│   ├── database.py       # SQLAlchemy configuration
│   └── dependencies.py   # get_current_user
├── .env                  # Environment variables
├── .gitignore
├── alembic.ini           # Alembic configuration
├── main.py              
└── requirements.txt     
```

## Security

- ✅ Passwords hashed with bcrypt (never stored in plain text)
- ✅ JWT tokens signed with SECRET_KEY
- ✅ Token expiration (7 days by default)
- ✅ Token validation on every protected request
- ✅ Data isolation: each user can only see their own tasks
- ✅ Sensitive variables in `.env` file

## Migrations

**Create a new migration:**
```bash
alembic revision --autogenerate -m "description of change"
```

**Apply migrations:**
```bash
alembic upgrade head
```

**Revert last migration:**
```bash
alembic downgrade -1
```

## Upcoming Features (v4)

- [ ] Refresh tokens
- [ ] Roles and permissions (admin/user)
- [ ] Tests with pytest
- [ ] Dockerization
- [ ] CI/CD with GitHub Actions
- [ ] Rate limiting
- [ ] Pagination for listings

## Author

**Martin Jimenez**  
Information Systems Engineering Student - UTN FRC

GitHub: [@martinjimenez04](https://github.com/martinjimenez04)