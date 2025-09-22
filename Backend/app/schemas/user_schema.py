from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str 
    password: str
    # phone_number = Optional[str] | None = None

class RegisterResponse(BaseModel):
    data: dict
    meta: str
    errors: str

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    data: dict
    meta: str
    errors: str

class currentUserSchema(BaseModel):
    data: dict
    meta: str
    errors: str


