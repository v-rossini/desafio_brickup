from pydantic import BaseModel
from typing import List

from .getterDict import PeeweeGetterDict
from .item import Item

class PDFFileBase(BaseModel):
    filename: str

class PDFFileCreate(PDFFileBase):
    pass

class PDFFileResponse(PDFFileBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class PDFFile(PDFFileBase):
    id: int
    user_id: int
    items: List[Item]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict