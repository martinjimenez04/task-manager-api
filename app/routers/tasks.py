# Los endpoints

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.models.task import Task
from app.database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    completada: bool | None = None,
    prioridad: int | None = None,
    db: Session = Depends(get_db)
):
    """
    Retorna todas las tareas con filtros opcionales.
    """
    # query = construye la consulta SQL, pero NO la ejecuta todavía
    query = db.query(Task)
    
    # Si vienen filtros, los agrega a la query
    if completada is not None:
        query = query.filter(Task.completada == completada)
    
    if prioridad is not None:
        query = query.filter(Task.prioridad == prioridad)
    
    # .all() ejecuta la query y retorna la lista
    return query.all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    """
    Retorna una tarea por ID.
    """
    # .first() ejecuta la query y retorna el primer resultado (o None)
    tarea = db.query(Task).filter(Task.id == task_id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    return tarea


@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Crea una nueva tarea.
    """
    # Convertir el schema Pydantic a modelo SQLAlchemy
    # **task.model_dump() = desempaqueta el dict como argumentos
    # Ejemplo: TaskCreate(titulo="X", prioridad=2) 
    #       →  Task(titulo="X", prioridad=2, completada=False)
    nueva = Task(**task.model_dump())
    
    # Agregar a la sesión (aún no se guarda en la DB)
    db.add(nueva)
    
    # Commit = ejecuta el INSERT en PostgreSQL
    db.commit()
    
    # Refresh = recarga el objeto desde la DB para obtener el ID generado
    db.refresh(nueva)
    
    return nueva


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    """
    Actualiza una tarea existente.
    """
    tarea = db.query(Task).filter(Task.id == task_id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    # exclude_unset=True ignora los campos que no vinieron en el request
    campos = task_update.model_dump(exclude_unset=True)
    
    # Actualizar solo los campos que llegaron
    for key, value in campos.items():
        setattr(tarea, key, value)  # tarea.titulo = "nuevo valor"
    
    db.commit()
    db.refresh(tarea)
    
    return tarea


@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    Elimina una tarea.
    """
    tarea = db.query(Task).filter(Task.id == task_id).first()
    
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea)
    db.commit()
    
    # 204 No Content = no devuelve nada en el body
    return None