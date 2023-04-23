from typing import List, Optional
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException

from repositories import fileRepository, itemRepository
from schemas.user import User
from schemas.item import ItemCreate, ItemResponse, ItemQuery
from database.dbConnection import get_db
from utils import oauth2


router = APIRouter(
    prefix = "/files/{file_id}/items",
    tags=["Items"])

@router.post("/", status_code = 201, response_model=ItemResponse, 
                                                    dependencies=[Depends(get_db)] )
def insert_item_on_file( current_user: Annotated[User, Depends(oauth2.get_current_user)],
                 file_id: int, item: ItemCreate):
#   db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    db_file = fileRepository.get_file(file_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found") 
    if(db_user.id != db_file.user_id):
        raise HTTPException(status_code=401, detail="File does not belong to that user")
    
    db_item = itemRepository.insert_item_on_file(item, file_id)
    return db_item


@router.get("/", response_model=List[ItemResponse], 
                                                            dependencies=[Depends(get_db)])
def get_items_from_file( current_user: Annotated[User, Depends(oauth2.get_current_user)], 
                        file_id: int, item:Optional[int] = None, desc: Optional[str] = None, un: Optional[str] = None,
                        am_max: Optional[int] = None, am_min: Optional[int] = None):
    
    query = ItemQuery(item=item, description=desc, unit=un, am_max=am_max, am_min=am_min)
#    db_user = userRepository.get_user(user_id=user_id)
    db_user = current_user
    db_file = fileRepository.get_file(file_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found") 
    if(db_user.id != db_file.user_id):
        raise HTTPException(status_code=401, detail="File does not belong to that user")
    
    db_list = db_file.items
    filtered_list = itemRepository.filter_items(db_list, query)

    return list(filtered_list) 

    #db_list = list(db_file.items)
 #   return list(db_list)