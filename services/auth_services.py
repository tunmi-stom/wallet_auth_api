from fastapi import HTTPException, status
from eth_account import Account
from web3 import Web3
from sqlalchemy.orm import Session
from eth_account.messages import encode_defunct
from utils.util import generate_nonce, build_message
from models.users import User
from core.auth.jwt_handler import create_jwt_token, token_response
from schemas.data import NonceData, VerifyData
from schemas.token import TokenData
from core.config import settings


class AuthService:
    @staticmethod   
    def authenticate(db: Session, data: NonceData) -> dict[str, str]:
        if data.chain_id not in settings.SUPPORTED_CHAINS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported Chain"
            )
        address = Web3.to_checksum_address(data.address)
        nonce = generate_nonce()
                
        try:
            existing_acct = db.query(User).filter(
                User.address == address,
                User.chain_id == data.chain_id
            ).first()
            if existing_acct:
                existing_acct.nonce = nonce
                db_user = existing_acct
            else:
                db_user = User(
                    address=address,
                    chain_id=data.chain_id,
                    chain_name=settings.SUPPORTED_CHAINS[data.chain_id],
                    nonce=nonce,
                )
                
                db.add(db_user)
            db.commit()
            
        except Exception as e:
            settings.LOGGER.error(str(e))
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error"
            )

            
        message = build_message(
            address=address,
            chain_id=data.chain_id,
            nonce=nonce
        )
        
        return {"message": message}
    
    @staticmethod
    def verify(db: Session, data: VerifyData):
        if data.chain_id not in settings.SUPPORTED_CHAINS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unsupported Chain"
            )
            
        address = Web3.to_checksum_address(data.address)
        
        acct = db.query(User).filter(
            User.address == address,
            User.chain_id == data.chain_id
            ).first()
        
        if not acct:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        nonce = acct.nonce
        
        if not nonce:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Nonce not found"
            )
            
        message = build_message(
            address=address,
            chain_id=data.chain_id,
            nonce=nonce,
        )
        
        message_hash = encode_defunct(text=message)
        
        try:
            recovered = Account.recover_message(message_hash, signature=data.signature)
            recovered_address = Web3.to_checksum_address(recovered)
        except Exception as e:
            settings.LOGGER.error(str(e))
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid Signature"
            )
        
        if recovered_address != address:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Address mismatch"            
                )
            
        
        token_data = TokenData(
            sub=str(recovered_address),
            chain_id=acct.chain_id,
            chain_name=acct.chain_name,
        )
        
        token = create_jwt_token(token_data)
        
        acct.nonce = generate_nonce()
        db.commit()
        
        return token_response(token, acct.chain_id)

