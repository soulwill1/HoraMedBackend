import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("xableucraw", "fallback_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
