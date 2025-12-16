from fastapi import APIRouter
from app.api.schemas.user import CreateUser, GetUser
from app.models.user import User, save, get_users, get_user

router = APIRouter()

@router.get("/users/", tags=["users"], response_model=list[GetUser])
async def read_users():
    return get_users()

@router.get("/users/{id}", tags=["users"], response_model=GetUser)
async def read_users(id:int):
    return get_user(id)

@router.post("/users/", tags=["users"], response_model=bool)
async def create(data: CreateUser):
    try:
        user = User(**data.model_dump())
        save(user)
        return True
    except Exception as e:
        print(e)
        return False