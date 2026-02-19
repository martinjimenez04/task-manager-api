from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    prioridad = Column(Integer, default=1)
    completada = Column(Boolean, default=False)
    
    # Nueva columna: foreign key al usuario
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relación: cada tarea pertenece a un usuario
    owner = relationship("User", back_populates="tasks")
    
    def __repr__(self):
        return f"<Task {self.id}: {self.titulo}>"