from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError

from app.database import get_db
from app.models.user import User
from app.core.security import decode_access_token

# OAuth2PasswordBearer le dice a FastAPI:
# "busca el token en el header Authorization: Bearer <token>"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependencia que extrae y valida el JWT token.
    
    Returns:
        El usuario autenticado
    
    Raises:
        HTTPException 401 si el token es inválido o el usuario no existe
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decodificar el token
    payload = decode_access_token(token)
    
    if payload is None:
        raise credentials_exception
    
    # Extraer el user_id del token
    user_id: str = payload.get("sub")
    if user_id is None:
        raise credentials_exception
    
    # Buscar el usuario en la DB
    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if user is None:
        raise credentials_exception
    
    return user