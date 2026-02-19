from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.models.task import Task
from app.models.user import User
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    completada: bool | None = None,
    prioridad: int | None = None,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    """
    Retorna todas las tareas del usuario autenticado.
    """
    # Solo las tareas del usuario actual
    query = db.query(Task).filter(Task.user_id == current_user.id)
    
    if completada is not None:
        query = query.filter(Task.completada == completada)
    
    if prioridad is not None:
        query = query.filter(Task.prioridad == prioridad)
    
    return query.all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),  
    db: Session = Depends(get_db)
):
    """
    Retorna una tarea por ID (solo si pertenece al usuario).
    """
    tarea = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # verificar que sea del usuario
    ).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    return tarea


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),  
    db: Session = Depends(get_db)
):
    """
    Crea una nueva tarea asociada al usuario autenticado.
    """
    nueva = Task(
        **task.model_dump(),
        user_id=current_user.id  # asignar al usuario actual
    )
    
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    
    return nueva


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_user),  
    db: Session = Depends(get_db)
):
    """
    Actualiza una tarea (solo si pertenece al usuario).
    """
    tarea = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # verificar que sea del usuario
    ).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    campos = task_update.model_dump(exclude_unset=True)
    for key, value in campos.items():
        setattr(tarea, key, value)
    
    db.commit()
    db.refresh(tarea)
    
    return tarea


@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),  
    db: Session = Depends(get_db)
):
    """
    Elimina una tarea (solo si pertenece al usuario).
    """
    tarea = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # verificar que sea del usuario
    ).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea)
    db.commit()
    
    return None