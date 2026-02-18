from sqlalchemy import Column, Integer, String, Boolean, Text
from app.database import Base


class Task(Base):
    __tablename__ = "tasks"  # nombre de la tabla en PostgreSQL

    # Columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    prioridad = Column(Integer, default=1)
    completada = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.id}: {self.titulo}>"