from passlib.context import CryptContext
from fastapi import Request, Response
from itsdangerous import URLSafeSerializer
from .config import SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
COOKIE_NAME = "session"

serializer = URLSafeSerializer(SECRET_KEY, salt="cookie-session")

# Hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Cookies
def create_session_cookie(response: Response, user_id: int):
    data = serializer.dumps({"user_id": user_id})
    response.set_cookie(
        key=COOKIE_NAME,
        value=data,
        httponly=True,
        samesite="lax",
        secure=False,  # True se usar HTTPS
    )

def get_user_id_from_cookie(request: Request):
    cookie = request.cookies.get(COOKIE_NAME)
    if not cookie:
        return None
    try:
        data = serializer.loads(cookie)
        return data.get("user_id")
    except:
        return None

def clear_session_cookie(response: Response):
    response.delete_cookie(COOKIE_NAME)
