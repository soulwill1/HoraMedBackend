from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session
from ...db.database import get_db
from .services.auth_service import authenticate_user, create_user
from ...core.security import create_session_cookie, clear_session_cookie, get_user_id_from_cookie
from auth.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = create_user(db, user.username, user.password)
    return new_user

@router.post("/login")
def login(user: UserCreate, response: Response, db: Session = Depends(get_db)):
    auth_user = authenticate_user(db, user.username, user.password)
    if not auth_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    create_session_cookie(response, auth_user.id)
    return {"message": "Login successful"}

@router.post("/logout")
def logout(response: Response):
    clear_session_cookie(response)
    return {"message": "Logged out"}

@router.get("/me")
def me(request: Request):
    user_id = get_user_id_from_cookie(request)
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"user_id": user_id}
