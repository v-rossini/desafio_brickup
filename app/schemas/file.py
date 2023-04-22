from pydantic import BaseModel
from typing import List

from .getterDict import PeeweeGetterDict
from .item import Item

class PDFFIleBase(BaseModel):
    filename: str

class PDFFile(PDFFIleBase):
    id: int
    user_id: int
    items: List[Item]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict