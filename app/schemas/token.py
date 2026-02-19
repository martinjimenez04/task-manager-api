from pydantic import BaseModel


class Token(BaseModel):
    """Schema de respuesta del login"""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Datos extraídos del token"""
    user_id: int | None = None
    email: str | None = None