from typing import List
from fastapi import APIRouter, Depends, HTTPException

from repositories import userRepository, fileRepository, itemRepository
from schemas import item
from database.dbConnection import get_db


router = APIRouter()

@router.post("/users/{user_id}/files/{file_id}/items", status_code = 201, response_model=item.ItemResponse, 
                                                    dependencies=[Depends(get_db)], tags=["Items"])
def insert_item_on_file(user_id:int, file_id: int, item: item.ItemCreate):
    db_user = userRepository.get_user(user_id=user_id)
    db_file = fileRepository.get_file(file_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found") 
    if(db_user.id != db_file.user_id):
        raise HTTPException(status_code=401, detail="File does not belong to that user")
    
    db_item = itemRepository.insert_item_on_file(item, file_id)
    return db_item


@router.get("/users/{user_id}/files/{file_id}/items", response_model=List[item.ItemResponse], 
                                                            dependencies=[Depends(get_db)], tags=["Items"])
def get_items_from_file(user_id: int, file_id: int):
    db_user = userRepository.get_user(user_id=user_id)
    db_file = fileRepository.get_file(file_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found") 
    if(db_user.id != db_file.user_id):
        raise HTTPException(status_code=401, detail="File does not belong to that user")
    
    db_list = list(db_file.items)
    return db_list