from api.users.schemas.user_create_schema import UserCreate
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from api.auth.services.auth_service import get_pwd_hash
from db.models import User


def get_user_service(user_id: int, current_user: User, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

def create_user_service(user: UserCreate, current_user: User, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code = 409, detail= "User already exist!")
    
    hashed_password = get_pwd_hash(user.password)
    db_user = User(
        name = user.name,
        email = user.email,
        phone = user.phone,
        date_of_birth = user.date_of_birth,
        hashed_pwd = hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_service(user_id: int, update_user: UserCreate, current_user: User, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!")

    # Update user
    db_user.name = update_user.name,
    db_user.email = update_user.email,
    db_user.phone = update_user.phone,
    db_user.date_of_birth = update_user.date_of_birth,
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_service(user_id: int, current_user: User, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist!")
    
    if user.id == current_user.id:
        raise HTTPException(status_code=400, detail="You can not delete yourself!")
    
    db.delete(user)
    db.commit()
    return {"Message":"User deleted!"}

def get_all_users_service(current_user: User, db: Session):
    return db.query(User).all()