from pydantic import BaseModel
from typing import Optional

class NonceData(BaseModel):
    address: str
    chain_id: int

class VerifyData(BaseModel):
    address: str
    chain_id: int
    signature: str
    
class UserData(BaseModel):
    address: str
    chain_id: int