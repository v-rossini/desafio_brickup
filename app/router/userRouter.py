from fastapi import APIRouter, Depends, HTTPException
from typing_extensions import Annotated

from repositories import userRepository
from schemas import user
from database.dbConnection import get_db
from utils import oauth2



router = APIRouter(
    prefix = "/users",
    tags=["User"])


@router.post("/", status_code = 201, response_model = user.UserResponse, 
                            dependencies=[Depends(get_db)])
def create_user(user: user.UserCreate):
    db_user = userRepository.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return userRepository.create_user(user=user)


@router.get("/me", response_model=user.UserResponse, 
                                dependencies=[Depends(get_db)])
def get_current_user(current_user: Annotated[user.User, Depends(oauth2.get_current_user)]):
#    db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user