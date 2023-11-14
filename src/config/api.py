import os
from dotenv import load_dotenv

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000"
]

load_dotenv()


class Config ():
    """Class config api"""

    ENVIRONMENT: str = os.getenv('ENVIRONMENT')
    APP_NAME: str = os.getenv('APP_NAME')
    CORS_ORIGINS = origins
    CORS_HEADERS = '*'


settings = Config()
