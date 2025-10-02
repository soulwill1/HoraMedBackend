from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.auth.config.config import ACCESS_TOKEN_EXPIRE_MINUTES
from api.auth.schemas.user_auth_schema import Token
from api.users.schemas.user_create_schema import UserResponse
from db.models import User
from db.database import get_db
from api.auth.services.auth_service import create_access_token, get_current_active_user, verify_password
from api.users.schemas.user_create_schema import UserCreate
from api.auth.services.auth_service import register_user

api_auth = APIRouter(
    prefix="/v1/auth", 
    tags=["auth"]
)

@api_auth.post("/register", response_model=UserResponse)
def register_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(user=user, db=db)

@api_auth.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or verify_password(form_data.password, user.hashed_pwd):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub":user.email}, expires_delta=access_token_expires
    )
    return {"access_token":access_token,"token_type":"bearer"}

@api_auth.get("/profile", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user

@api_auth.get("/verify-token")
def verify_token_endpoint(current_user: User = Depends(get_current_active_user)):
    return {
        "valid": True,
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email,
            "phone": current_user.phone,
            "date_of_birth": current_user.date_of_birth
        }
    }
