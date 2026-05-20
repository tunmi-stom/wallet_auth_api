from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.engine import create_engine
from fastapi import Depends
from typing import Annotated
from core.config import settings

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

Base = declarative_base()