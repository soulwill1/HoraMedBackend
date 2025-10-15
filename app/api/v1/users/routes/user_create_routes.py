from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from app.api.v1.users.schemas.user_create_schema import UserResponse, UserCreate, UserUpdate
from app.api.v1.users.services.user_create_service import create_user_service, update_user_service, delete_user_service, get_user_service, get_all_users_service
from app.api.v1.auth.services.auth_service import get_current_active_user
from app.db.models import User
from app.db.database import get_db


api_users = APIRouter(
    prefix="/accounts",
    tags=["api_users"]
)

@api_users.get("/users", response_model=List[UserResponse])
def get_all_users(current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return get_all_users_service(current_user=current_user, db=db)

@api_users.get("/users/search", response_model=UserResponse)
def get_user(name: str, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return get_user_service(name=name, current_user=current_user, db=db)

@api_users.put("/users/{user_id}", response_model=UserResponse)
def update_user_route(user_id: str, update_data: UserUpdate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return update_user_service(user_id=user_id, update_data=update_data, current_user=current_user, db=db)

@api_users.delete("/users/{user_id}", response_model=dict)
def delete_user_route(user_id: str, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return delete_user_service(user_id=user_id, current_user=current_user, db=db)

@api_users.post("/patients", response_model=UserResponse)
def register_patient_route(user: UserCreate, current_user: User = Depends(get_current_active_user), db: Session = Depends(get_db)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create patients!")
    return create_user_service(user=user, db=db, current_user=current_user)