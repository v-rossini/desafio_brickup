from typing import List, Optional
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException, UploadFile

from repositories import fileRepository, itemRepository
from schemas import file, user
from schemas.item import ItemCreate, ItemQuery
from database.dbConnection import get_db
from utils import oauth2

from utils.pdfParser import parsePdf




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


@router.post("/pdf",  
             #response_model=List[file.PDFFileResponse], 
                                        dependencies=[Depends(get_db)])
async def create_file_from_pdf(uploaded_file: UploadFile,
                    current_user: Annotated[user.User, Depends(oauth2.get_current_user)]):
    
    pdf_binary = await uploaded_file.read()

    pdffile = file.PDFFileCreate(filename = uploaded_file.filename)
    db_user = current_user
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_file = fileRepository.create_file_for_user(pdffile, db_user.id)

    tables = parsePdf(pdf_binary)
    item_list = []

    for table in tables:
        columns = table.columns
        table[columns[3]] = table[columns[3]].fillna(0)
        table[columns[2]] = table[columns[2]].fillna("")
        table[columns[1]] = table[columns[1]].fillna("")
        table[columns[0]] = table[columns[0]].fillna(-1)
        for entry in range(table.size):
                try:
                    db_item_create = ItemCreate(item = table[columns[0]][entry],
                                                description = table[columns[1]][entry], 
                                                unit=table[columns[2]][entry],
                                                amount=int(table[columns[3]][entry]))
                    print(db_item_create)
                    db_item = itemRepository.insert_item_on_file(db_item_create, db_file.id)
                    item_list.append(db_item)
                except:
                    pass
    return {"filename": uploaded_file.filename, "amount_of_items": len(item_list), "items_added": item_list}
