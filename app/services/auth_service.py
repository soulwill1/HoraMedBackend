from sqlalchemy.orm import Session
from ..db.models import User
from ..core.security import verify_password, hash_password

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        return None
    return user

def create_user(db: Session, username: str, password: str):
    hashed_pw = hash_password(password)
    user = User(username=username, password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
