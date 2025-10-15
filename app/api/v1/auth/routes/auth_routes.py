from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.api.v1.auth.config.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.v1.auth.schemas.user_auth_schema import Token
from app.api.v1.users.schemas.user_create_schema import UserResponse
from app.db.models import User
from app.db.database import get_db
from app.api.v1.auth.services.auth_service import get_current_active_user, verify_token_endpoint, login_for_access_token
from app.api.v1.users.schemas.user_create_schema import UserCreate
from app.api.v1.users.services.user_create_service import create_user_service

api_auth = APIRouter(
    prefix="/auth", 
    tags=["auth"]
)

@api_auth.get("/profile", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_active_user)):
    return current_user

@api_auth.post("/signup", response_model=UserResponse)
def register_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user=user, db=db, current_user=None)

@api_auth.post("/login", response_model=Token)
def login_access_token_route(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_for_access_token(form_data=form_data, db=db)

@api_auth.get("/verify-token")
def verify_token_endpoint_route(current_user: User = Depends(get_current_active_user)):
    return verify_token_endpoint(current_user=current_user)