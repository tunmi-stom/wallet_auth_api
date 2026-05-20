import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "Wallet Authentication API"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    )
    ALGORITHM: str = os.getenv("ALGORITHM")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Logger
    LOGGER = logging.getLogger(__name__)

    # Supported Chains
    SUPPORTED_CHAINS = {
        1: "Ethereum",
        137: "Polygon",
        42161: "Arbitrum",
        8453: "Base",
        10: "Optimism",
    }


settings = Settings()