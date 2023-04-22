from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenResponse(Token):
    id: int

class TokenData(BaseModel):
    username: Optional[str]