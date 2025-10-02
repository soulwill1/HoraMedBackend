from fastapi import APIRouter, Depends
from api.users.schemas.user_create_schema import UserResponse, UserCreate
from api.users.services.user_create_service import create_user_service, update_user_service, delete_user_service, get_user_service, get_all_users_service
from sqlalchemy.orm import Session
from api.auth.services.auth_service import get_current_active_user
from db.models import User
from db.database import get_db
from typing import List


api_users = APIRouter(
    prefix="/v1/accounts",
    tags=["api_users"]
)


@api_users.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return get_user_service(user_id=user_id, current_user=current_user, db=db)

@api_users.post("/signin", response_model=UserResponse)
def create_user_route(user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return create_user_service(user=user, current_user=current_user, db=db)

@api_users.put("/users/{user_id}", response_model=UserResponse)
def update_user_route(user_id: int, user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return update_user_service(user_id=user_id, current_user=current_user, user=user, db=db)

@api_users.delete("/users/{user_id}", response_model=UserResponse)
def delete_user_route(user_id: int, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return delete_user_service(user_id=user_id, current_user=current_user, db=db)

@api_users.get("/users/search", response_model=List[UserResponse])
def get_all_users(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return get_all_users_service(current_user=current_user, db=db)