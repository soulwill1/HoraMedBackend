from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from db.database import get_db
from api.auth.services.auth_service import authenticate_user
from api.auth.core.security import create_session_cookie, clear_session_cookie, get_user_id_from_cookie
from auth.schemas import UserCreate

api_auth = APIRouter(
    prefix="/v1/auth", 
    tags=["auth"]
)

@api_auth.post("/login")
def login(user: UserCreate, response: Response, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    create_session_cookie(response, auth_user.id)
    return {"message": "Login successful"}

@api_auth.post("/logout")
def logout(response: Response):
    clear_session_cookie(response)
    return {"message": "Logged out"}
