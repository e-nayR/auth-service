from app.core.configs import db_url
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def save(obj):
    db = SessionLocal()
    db.add(obj)
    db.commit()
    db.close()