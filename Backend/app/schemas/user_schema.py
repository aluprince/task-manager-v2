from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str 
    password: str
    # phone_number = Optional[str] | None = None

class LoginRequest(BaseModel):
    email: str
    password: str



