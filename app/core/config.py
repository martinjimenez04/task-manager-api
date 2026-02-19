from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str  
    
    # JWT
    SECRET_KEY: str = "tu_clave_secreta_super_larga_y_aleatoria_cambiar_en_produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 días
    
    class Config:
        env_file = ".env"
        extra = "ignore"  

settings = Settings()