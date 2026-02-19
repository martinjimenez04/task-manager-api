from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.schemas.token import Token
from app.models.user import User
from app.database import get_db
from app.core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["authentication"]
)


@router.post("/register", response_model=UserResponse, status_code=201)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Registrar un nuevo usuario.
    
    - Verifica que el email no exista
    - Hashea la contraseña
    - Guarda el usuario en la DB
    """
    # Verificar si el email ya existe
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="El email ya está registrado"
        )
    
    # Crear el usuario
    new_user = User(
        email=user_data.email,
        password_hash=hash_password(user_data.password)  # hashear la contraseña
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),  # ← cambiar esto
    db: Session = Depends(get_db)
):
    """
    Iniciar sesión.
    
    - Verifica que el usuario exista
    - Verifica la contraseña
    - Devuelve un JWT token
    """
    # form_data.username en OAuth2 = el email en nuestro caso
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Email o contraseña incorrectos"
        )
    
    # Verificar la contraseña
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Email o contraseña incorrectos"
        )
    
    # Crear el token JWT
    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "email": user.email
        }
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
