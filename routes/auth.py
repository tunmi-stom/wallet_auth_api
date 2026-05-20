from fastapi import APIRouter
from database.db_config import db_dependency
from services.auth_services import AuthService
from schemas.data import UserData, VerifyData

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/nonce")
async def get_message(db: db_dependency, data: UserData):
    """"""
    return_data = AuthService.authenticate(db, data)
    return return_data
    
@router.post("/verify")
async def verify_signature(db: db_dependency, data: VerifyData):
    token = AuthService.verify(db, data)
    return token
