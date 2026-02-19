from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    """Schema para registrar un nuevo usuario"""
    email: EmailStr  # valida que sea un email válido
    password: str


class UserResponse(BaseModel):
    """Schema de respuesta (sin password)"""
    id: int
    email: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """Schema para login"""
    email: EmailStr
    password: str