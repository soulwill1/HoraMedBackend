from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: str
    phone: int
    date_of_birth: date
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: int
    date_of_birth: date
    is_active: bool

    class Config:
        from_attributes = True