from pydantic import BaseModel
from typing import Optional

class TokenPayload(BaseModel):
    sub: str
    exp: str
    iat: str 
    chain_id: int
    chain_name: str

class TokenData(BaseModel):
    sub: str
    chain_id: int
    chain_name: str