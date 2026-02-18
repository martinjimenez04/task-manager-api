from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Leer la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# create_engine = crea la conexión a PostgreSQL
# echo=True muestra en la terminal el SQL que genera
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal = una "sesión" es como abrir una transacción con la DB
# Cada request HTTP va a tener su propia sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = clase padre de todos los modelos SQLAlchemy
# Todos los modelos van a heredar de esta clase
Base = declarative_base()


# Dependency para FastAPI
# Cada endpoint que necesite la DB va a llamar a esta función
def get_db():
    db = SessionLocal()
    try:
        yield db  # "yield" = devuelve la sesión pero no termina la función
    finally:
        db.close()  # siempre cierra la conexión, incluso si hubo un error