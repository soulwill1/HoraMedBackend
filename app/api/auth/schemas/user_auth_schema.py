from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: int
    email: str
    is_active: bool
