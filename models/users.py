from database.db_config import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "wallets_address"
    
    id = Column(Integer, primary_key=True, index=True)
    nonce = Column(String, nullable=True)
    address = Column(String, nullable=False, index=True)
    chain_id = Column(Integer, nullable=False, index=True)
    chain_name = Column(String, nullable=True)
