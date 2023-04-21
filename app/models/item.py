from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    item: int
    description: str
    unit: Optional[str]
    amount: Optional[int]