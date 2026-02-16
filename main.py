# Punto de entrada, arranca el servidor

from fastapi import FastAPI
from app.routers import tasks

app = FastAPI(
    title="Task Manager API",
    description="API REST para gestión de tareas — Proyecto de Martín Jiménez",
    version="1.0.0"
)

# Registrar el router de tareas
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"mensaje": "Task Manager API funcionando ✓", "docs": "/docs"}