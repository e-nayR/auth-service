from fastapi import APIRouter
from app.api.schemas.user import CreateUser, GetUser, LoginSchema
from app.models.user import get_users, get_user, create_user, auth_user

router = APIRouter()

@router.get("/users/", tags=["users"], response_model=list[GetUser])
async def read_users():
    return get_users()

@router.get("/users/{id}", tags=["users"], response_model=GetUser)
async def read_users(id:int):
    return get_user(id)

@router.post("/users/", tags=["users"], response_model=bool)
async def create(data: CreateUser):
    return create_user(data.model_dump())

@router.post("/login/", tags=["auth"])
async def login(data: LoginSchema):
    return auth_user(data.model_dump())