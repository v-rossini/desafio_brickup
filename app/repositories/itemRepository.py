from database import models
from typing import Optional
from schemas.item import ItemCreate, ItemQuery
from repositories.fileRepository import get_file

def insert_item_on_file(item: ItemCreate, file: int):
    db_item = models.Item(**item.dict(),   file_id=file)
    db_item.save()
    return db_item

def filter_items(db_list: object, query: Optional[ItemQuery]):


    #models.PDFFile.filter(models.PDFFile.id == file_id)
    if query.item:
       db_list = db_list.select().where(models.Item.item == query.item)
    if query.description:
        db_list = db_list.select().where(models.Item.description.contains(query.description))
    if query.unit:
        db_list = db_list.select().where(models.Item.unit == query.unit)
    if query.am_max:
        db_list = db_list.select().where(models.Item.amount <= query.am_max)
    if query.am_min:
        db_list = db_list.select().where(models.Item.amount >= query.am_min)

    return list(db_list)
