from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from app.api.v1.auth.services.auth_service import get_pwd_hash
from app.db.models import User
from app.api.v1.users.schemas.user_create_schema import UserCreate, UserUpdate


def get_user_service(name: str, current_user: User, db: Session):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can search patients!")
    
    user = db.query(User).filter(User.owner_id == current_user.id, User.name.ilike(f"%{name}%")).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found!")
    return user

def create_user_service(user: UserCreate, db: Session, current_user: Optional[User] = None):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="User already exists!")

    safe_password = user.password[:72]
    hashed_password = get_pwd_hash(safe_password)

    total_users = db.query(User).count()

    # Case 1: No users exist yet → first admin
    if total_users == 0:
        db_user = User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            date_of_birth=user.date_of_birth,
            hashed_pwd=hashed_password,
            is_admin=True
        )

    # Case 2: Created via public signup (no current_user) → new independent admin
    elif current_user is None:
        db_user = User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            date_of_birth=user.date_of_birth,
            hashed_pwd=hashed_password,
            is_admin=True
        )

    # Case 3: Created by an admin → patient account
    elif current_user.is_admin:
        db_user = User(
            name=user.name,
            email=user.email,
            phone=user.phone,
            date_of_birth=user.date_of_birth,
            hashed_pwd=hashed_password,
            is_admin=False,
            owner_id=current_user.id
        )

    # Case 4: A regular user tries to create another user → not allowed
    else:
        raise HTTPException(status_code=403, detail="Only admins can create new users!")

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_service(user_id: str, update_data: UserUpdate, current_user: User, db: Session):
    # Convert string to UUID
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    db_user = db.query(User).filter(User.id == user_uuid).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exist!")

    # Permission check
    if (not current_user.is_admin and db_user.id != current_user.id) or \
       (current_user.is_admin and db_user.owner_id not in [current_user.id, None] and db_user.id != current_user.id):
        raise HTTPException(status_code=403, detail="You don't have permission to update this user")

    # Map of fields to update
    update_fields = {
        "name": update_data.name,
        "email": update_data.email,
        "phone": update_data.phone,
        "date_of_birth": update_data.date_of_birth,
        "password": get_pwd_hash(update_data.password) if update_data.password else None
    }

    # Apply updates dynamically
    for field, value in update_fields.items():
        if value is not None:
            if field == "password":
                db_user.hashed_pwd = value
            else:
                setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_service(user_id: str, current_user: User, db: Session):
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = db.query(User).filter(User.id == user_uuid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User does not exist!")

    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can delete accounts.")

    # Admin can delete own account or their patients
    is_own_account = user.id == current_user.id
    is_patient = user.owner_id == current_user.id

    if not (is_own_account or is_patient):
        raise HTTPException(status_code=403, detail="You can only delete your own account or your patients.")

    # Soft delete for admin deleting own account
    if is_own_account:
        if user.is_deleted:
            raise HTTPException(status_code=400, detail="This account is already scheduled for deletion.")

        user.is_deleted = True
        user.deletion_date = datetime.utcnow() + timedelta(days=30)

        # Soft delete all patients of this admin
        db.query(User).filter(User.owner_id == user.id).update(
            {"is_deleted": True, "deletion_date": datetime.utcnow() + timedelta(days=30)}
        )

        db.commit()
        return {"message": "Account scheduled for deletion in 30 days."}

    # Hard delete if it's a patient
    db.delete(user)
    db.commit()
    return {"message": "Patient account permanently deleted."}


def get_all_users_service(current_user: User, db: Session):
    if current_user.is_admin:
        return db.query(User).filter(User.owner_id == current_user.id).all()
    else:
        return [current_user]
