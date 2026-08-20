import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#==============================================================================================

load_dotenv()

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
engine = create_engine(
    DATABASE_URL,
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#==============================================================================================

class Base(DeclarativeBase):
    pass

#==============================================================================================

def get_db():
    with session_local() as db:
        try:
            yield db
        except Exception:
            db.rollback() # ONLY rolls back if an actual database error occurred
            raise