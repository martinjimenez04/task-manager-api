from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings

# Configuración de bcrypt para hashear passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.
    Entrada: "python123"
    Salida: "$2b$12$KIXl.QT0xF7h3lP0mHhGOe..."
    """
    print(f"DEBUG: intentando hashear password de longitud {len(password)}")
    print(f"DEBUG: primeros 20 caracteres: {password[:20]}")
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con el hash.
    Retorna True si es correcta, False si no.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Crea un JWT token.
    
    Args:
        data: diccionario con los datos a incluir (ej: {"sub": "1", "email": "..."})
    
    Returns:
        string con el token JWT firmado
    """
    to_encode = data.copy()
    
    # Agregar tiempo de expiración
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Firmar el token con la SECRET_KEY
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt


def decode_access_token(token: str) -> dict | None:
    """
    Decodifica y verifica un JWT token.
    
    Returns:
        dict con los datos del token si es válido
        None si el token es inválido o expiró
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        return None