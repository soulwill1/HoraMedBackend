from pydantic import BaseModel
from datetime import date
from uuid import UUID
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    date_of_birth: date
    password: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    phone: str
    date_of_birth: date
    is_active: bool
    is_admin: bool
    owner_id: UUID | None = None

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[date] = None
    password: Optional[str] = None