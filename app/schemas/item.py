from pydantic import BaseModel
from typing import Optional
import numpy as np

from .getterDict import PeeweeGetterDict

class ItemBase(BaseModel):
    item: int
    description: Optional[str] = None
    unit: Optional[str] = None
    amount: Optional[int] = 0

class ItemCreate(ItemBase):
    pass

class ItemQuery(BaseModel):
    item: Optional[int]
    description: Optional[str] = None
    unit: Optional[str] = None
    am_max: Optional[int] = None
    am_min: Optional[int] = None

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