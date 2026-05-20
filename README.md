# Web3 Wallet Authentication API

A secure FastAPI-based backend for wallet authentication using signed nonces and JWT session management.

Supports Ethereum-compatible wallets and provides reusable authentication infrastructure for Web3 apps.

## Why This API Exists

Traditional authentication relies on emails and passwords.

Web3 applications instead authenticate users through wallet ownership using cryptographic signatures.

This API provides:
- nonce generation
- signature verification
- JWT issuance
- wallet session authentication

without requiring passwords.

## Authentication Flow

1. Client requests a nonce
2. Backend generates a unique nonce
3. Wallet signs the nonce
4. Backend verifies the signature
5. JWT access token is issued

## Features

- Ethereum wallet authentication
- Nonce-based login flow
- Signature verification
- JWT access tokens
- Replay attack prevention
- Multi-chain support
- FastAPI async architecture
- PostgreSQL persistence

## Tech Stack
- FastAPI
- SQLAlchemy
- Uvicorn
- Postgresql
- JWT Authentication
- Pydantic
- eth_account
- web3.py

## Installation

git clone https://github.com/tunmi-stom/wallet_auth_api.git

cd wallet_auth_api

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

## Environment Variables
## Environment Variables

Create a `.env` file:

DATABASE_URL=
SECRET_KEY=
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

## Request Nonce

Endpoint: POST /auth/nonce

# Requests
{
  "address": "0xabc12345...",
  "chain_id: 1
}
# Returns
{
  "message": "backend-generated-message"
}
The nonce is stored server-side and must be signed by the wallet owner.

## Verify Wallet Signature

Endpoint: POST /auth/verify

# Requests
{
  "address": "0x123...",
  "signature": "0xabcd...",
  "chain_id": 1
}
# Returns
{
  "token": "...",
  "chain_name": "Ethereum",
  "token_type": "bearer"
}
The token generated is used to authenticate sessions of connection to the wallet.

## Error Responses

401 Unauthorized
400 Invalid Signature
500 Internal Server Error

## Security Considerations

- Nonces are single-use
- Expired JWT tokens are rejected
- Signature verification uses wallet recovery
- Replay attacks are prevented
- Wallet addresses are checksum validated

## Use Cases

- NFT marketplaces
- DAO platforms
- DeFi dashboards
- Wallet-gated communities
- Web3 SaaS products
- Blockchain analytics tools

## Future Improvements

- Refresh tokens
- SIWE (Sign-In With Ethereum)
- Redis nonce storage
- Rate limiting
- OAuth wallet linking
- Multi-wallet accounts

## Running the Server
Run on root directory:
"uvicorn main:app --reload"

## API Documentation

Swagger UI:
http://localhost:8000/docs

ReDoc:
http://localhost:8000/redoc

## Deployment

Production deployment supported on:
- Render
- Railway
- Docker
- VPS

## Testing
pytest
## Contributing

## License
