from datetime import datetime, timedelta
from typing import Any, Dict
from jose import jwt
from core.config import settings
from schemas.token import TokenData

def create_jwt_token(data: TokenData) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        
    to_encode = {
        "sub": str(data.sub),
        "exp": expire,
        "chain_id": data.chain_id,
        "chain_name": data.chain_name,
        "iat": datetime.utcnow()
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> Dict[str, Any]:
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    return payload

def token_response(token: str, chain_id: int):
    return {
        "token": token,
        "chain": settings.SUPPORTED_CHAINS[chain_id],
        "token_type": "bearer"
    }