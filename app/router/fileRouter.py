from typing import List
from fastapi import APIRouter, Depends, HTTPException

from repositories import userRepository, fileRepository
from schemas import file
from database.dbConnection import get_db


router = APIRouter()


@router.post("/users/{user_id}/files", status_code = 201, response_model=file.PDFFileResponse, 
                            dependencies=[Depends(get_db)], tags=["Files"])
def create_file_for_user(user_id: int, file: file.PDFFileCreate):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_file = fileRepository.create_file_for_user(file, user_id)
    return db_file


@router.get("/users/{user_id}/files", response_model=List[file.PDFFileResponse], 
                                        dependencies=[Depends(get_db)], tags=["Files"])
def get_files_from_user(user_id: int):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_list = list(db_user.files)
    return db_list