from pydantic import BaseModel
from typing import List

from .getterDict import PeeweeGetterDict
from .file import PDFFile


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str

class UserAuth(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict

class User(UserBase):
    id: int
    files: List[PDFFile]

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict