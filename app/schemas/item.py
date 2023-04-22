from pydantic import BaseModel
from typing import Optional

from .getterDict import PeeweeGetterDict

class ItemBase(BaseModel):
    item: int
    description: Optional[str] = None
    unit: Optional[str] = None
    amount: Optional[int] = None

class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class Item(ItemBase):
    id: int
    file_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict