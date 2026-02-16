# Modelos Pydantic (cómo lucen los datos)

from pydantic import BaseModel
from typing import Optional

# Schema para CREAR una tarea (lo que manda el cliente)
class TaskCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None  # Optional = puede no venir
    prioridad: int = 1                 # valor por defecto: 1

# Schema para ACTUALIZAR (todos los campos opcionales)
class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    prioridad: Optional[int] = None
    completada: Optional[bool] = None

# Schema de RESPUESTA (lo que devuelve la API)
# Hereda de TaskCreate y agrega los campos que genera el servidor
class TaskResponse(TaskCreate):
    id: int
    completada: bool = False

    class Config:
        from_attributes = True  # necesario para compatibilidad con ORM (Fase 2)