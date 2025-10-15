import os
from dotenv import load_dotenv
load_dotenv()

# for auth service
API_V1_STR = "/api/v1"
AUTH_LOGIN_ENDPOINT = "/auth/login"

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
