# Los endpoints

from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from typing import List, Optional

router = APIRouter(
    prefix="/tasks",   # todos los endpoints de este archivo arrancan con /tasks
    tags=["tasks"]     # agrupa los endpoints en la documentación /docs
)

# Base de datos temporal (en memoria — Fase 2 la reemplazamos con PostgreSQL)
db: List[dict] = []
counter = {"id": 1}  # simula el autoincrement de una DB


@router.get("/", response_model=List[TaskResponse])
def get_tasks(completada: Optional[bool] = None, prioridad: Optional[int] = None):
    
    """ Retorna todas las tareas.
    Filtros opcionales:
    - **completada**: true o false
    - **prioridad**: número (1, 2, 3...)"""
    
    resultado = db

    if completada is not None:
        resultado = [t for t in resultado if t["completada"] == completada]

    if prioridad is not None:
        resultado = [t for t in resultado if t["prioridad"] == prioridad]

    return resultado


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    """Retorna una tarea por ID"""
    tarea = next((t for t in db if t["id"] == task_id), None)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    """Crea una nueva tarea"""
    nueva = {
        "id": counter["id"],
        "titulo": task.titulo,
        "descripcion": task.descripcion,
        "prioridad": task.prioridad,
        "completada": False
    }
    db.append(nueva)
    counter["id"] += 1
    return nueva


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    """Actualiza una tarea existente"""
    tarea = next((t for t in db if t["id"] == task_id), None)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    # Actualiza solo los campos que llegaron (exclude_unset ignora los None)
    campos = task_update.model_dump(exclude_unset=True)
    tarea.update(campos)
    return tarea


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Elimina una tarea"""
    tarea = next((t for t in db if t["id"] == task_id), None)
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.remove(tarea)

