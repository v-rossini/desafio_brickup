from typing import List
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException

from repositories import userRepository, fileRepository
from schemas import file, user
from database.dbConnection import get_db
from utils import oauth2

"""
router = APIRouter(
    prefix = "/users/{user_id}/files",
    tags=["Files"])


@router.post("/", status_code = 201, response_model=file.PDFFileResponse, 
                            dependencies=[Depends(get_db)] )
def create_file_for_user(user_id: int, file: file.PDFFileCreate, 
                    current_user: Annotated[user.User, Depends(oauth2.get_current_user)]):
#    db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_file = fileRepository.create_file_for_user(file, user_id)
    return db_file


@router.get("/",  response_model=List[file.PDFFileResponse], 
                                        dependencies=[Depends(get_db)])
def get_files_from_user(user_id: int, current_user: Annotated[user.User, Depends(oauth2.get_current_user)],):
    #db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_list = list(db_user.files)
    return db_list
"""

router = APIRouter(
    prefix = "/files",
    tags=["Files"])


@router.post("/", status_code = 201, response_model=file.PDFFileResponse, 
                            dependencies=[Depends(get_db)] )
def create_file_for_user(file: file.PDFFileCreate, 
                    current_user: Annotated[user.User, Depends(oauth2.get_current_user)]):
#    db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_file = fileRepository.create_file_for_user(file, db_user.id)
    return db_file


@router.get("/",  response_model=List[file.PDFFileResponse], 
                                        dependencies=[Depends(get_db)])
def get_files_from_user(current_user: Annotated[user.User, Depends(oauth2.get_current_user)],):
    #db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_list = list(db_user.files)
    return db_list