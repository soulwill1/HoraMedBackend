from fastapi import APIRouter, Depends
from api.users.schemas.user_create_schema import UserResponse, UserCreate
from api.users.services.user_create_service import create_user_service, update_user_service, delete_user_service
from sqlalchemy.orm import Session
from db.database import get_db


api_users = APIRouter(
    prefix="/v1/accounts",
    tags=["api_users"]
)

@api_users.post("/signin", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user=user, db=db)

@api_users.put("/{user_id}", response_model=UserResponse)
def update_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_service(user_id=user_id, user=user, db=db)

@api_users.delete("/{user_id}", response_model=UserResponse)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    return delete_user_service(user_id=user_id, db=db)
