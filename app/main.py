from fastapi import FastAPI, Depends, HTTPException
from typing import List
from schemas  import user, item, file
from database.dbConnection import start_db, get_db
from repositories import userRepository, fileRepository, itemRepository
from database import models

start_db()

app = FastAPI()

@app.get("/")
def index():
    return "olar!"

## @app.post("/user")
## def create_user(body: User):
##    return "bla"

@app.post("/users/", status_code = 201, response_model=user.User, 
                                response_model_exclude = {"files"}, dependencies=[Depends(get_db)])
def create_user(user: user.UserCreate):
    db_user = userRepository.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return userRepository.create_user(user=user)


@app.get("/users/{user_id}", response_model=user.User,
                            response_model_exclude = {"files"}, dependencies=[Depends(get_db)])
def get_user_by_id(user_id: int):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



@app.post("/users/{user_id}/files", status_code = 201, response_model=file.PDFFile,
                                            response_model_exclude = {"items"}, dependencies=[Depends(get_db)])
def create_file_for_user(user_id: int, file: file.PDFFileCreate):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_file = fileRepository.create_file_for_user(file, user_id)
    return db_file


@app.get("/users/{user_id}/files", response_model=List[file.PDFFile], 
                            response_model_exclude = {"items"}, dependencies=[Depends(get_db)])
def get_files_from_user(user_id: int):
    db_user = userRepository.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_list = list(db_user.files)
    return db_list


@app.post("/users/{user_id}/files/{file_id}/items", status_code = 201, 
                                        response_model=item.Item, dependencies=[Depends(get_db)])
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

@app.get("/users/{user_id}/files/{file_id}/items", response_model=List[item.Item], 
                                                            dependencies=[Depends(get_db)])
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

# @app.post("/file")
# def create_user(body: file.PDFFile):
#     return "bla"