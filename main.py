from fastapi import FastAPI
from app.routers import tasks, auth  

app = FastAPI(
    title="Task Manager API",
    description="API REST para gestión de tareas con autenticación JWT",
    version="2.0.0"
)

# Registrar routers
app.include_router(tasks.router)
app.include_router(auth.router)  


@app.get("/")
def root():
    return {
        "mensaje": "Task Manager API v2 con autenticación JWT ✓",
        "docs": "/docs"
    }