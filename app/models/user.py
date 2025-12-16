from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base, engine, SessionLocal

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    
def save(obj):
    db = SessionLocal()
    db.add(obj)
    db.commit()
    db.close()

def get_users():
    db = SessionLocal()
    try:
        query = select(User)
        return db.scalars(query).all()
    finally:
        db.close()

def get_user(id):
    db = SessionLocal()
    try:
        query = select(User).where(User.id == id)
        return db.scalars(query).first()
    finally:
        db.close()