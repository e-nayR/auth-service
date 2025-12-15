from fastapi import APIRouter

router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"id":"1","name": "Rick","email":"teste@gmail.com"}]