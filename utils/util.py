import secrets
from datetime import datetime

# Create a function to generate random message(nonce)
def generate_nonce() -> str:
    return secrets.token_hex(16)

# Create a function that generates the message for signing
def build_message(address: str, chain_id: int, nonce: str):
    return f"Sign Message:{nonce}{address}{chain_id}"