from api.users.schemas.user_create_schema import UserCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models import User

def create_user_service(user: UserCreate, db: Session):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code = 409, detail= "User already exist!")
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_service(user_id: int, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!")

    # Update user
    for field, value in user.dict().items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_service(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!")
    
    db.delete(db_user)
    db.commit()
    return {"Message":"User deleted!"}