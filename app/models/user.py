from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base, SessionLocal, save
from app.core.security import hash_password, verify_password
from fastapi import HTTPException
import datetime
from app.core.configs import secret_key
from jose import jwt


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    
def create_user(obj):
    try:
        plain_pass = obj['password']
        obj['password'] = hash_password(plain_pass)
        user = User(**obj)
        save(user)
        return True
    except Exception as e:
        print(e)
        return False

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

def verify_user(data):
    email = data['email']
    password = data['password']
    db = SessionLocal()
    try:
        query = select(User).where(User.email == email)
        user = db.scalars(query).first()
        if user:
            if verify_password(password, user.password):
                return {"id":user.id, "email":user.email, "name":user.name}
            else:
                raise HTTPException(status_code=404, detail="User not found")
        else:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        db.close()

def auth_user(data):
    user_data = verify_user(data)
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    token_data = {
        **user_data,
        "exp": expire
    }
    
    token = jwt.encode(
        token_data, secret_key, algorithm='HS256'
    )
    
    return token