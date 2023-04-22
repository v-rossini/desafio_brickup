from fastapi import APIRouter, Depends, HTTPException

from repositories import userRepository
from schemas import user
from database.dbConnection import get_db




router = APIRouter()


@router.post("/users/", status_code = 201, response_model = user.UserResponse, 
                            dependencies=[Depends(get_db)], tags=["User"])
def create_user(user: user.UserCreate):
    db_user = userRepository.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return userRepository.create_user(user=user)


@router.get("/users/{user_id}", response_model=user.UserResponse, 
                                dependencies=[Depends(get_db)], tags=["User"])
def get_user_by_id(user_id: int):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user