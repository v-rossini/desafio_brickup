from database import models
from schemas.item import ItemCreate

def insert_item_on_file(item: ItemCreate, file: int):
    db_item = models.Item(**item.dict(),   file_id=file)
    db_item.save()
    return db_item