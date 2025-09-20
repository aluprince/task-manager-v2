from fastapi import APIRouter, Depends, status, Response
from ..controllers.auth_controllers import register_user, login_user, get_current_user 
from ..models import User
from sqlalchemy.orm import Session
from ..db import get_db
from ..schemas.user_schema import UserCreate, LoginRequest

router = APIRouter(
    prefix="/api/auth", #We mount all authentication routes with /api/auth
    tags=["Auth"] #tags for swagger documentation
)

@router.get("/me", status_code=status.HTTP_200_OK)
def get_me(user=Depends(get_current_user)):
    return user

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, db: Session = Depends(get_db)):
    return register_user(data, db)

@router.post("/login", status_code=status.HTTP_200_OK)
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    return login_user(data, response, db)

# Kill token and redirect the to the home or login page
@router.post("/logout", status_code=status.HTTP_200_OK)
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logout Successfully"}

#Test Endpoint
@router.get('/tasks')
def tasks(user=Depends(get_current_user), db: Session=Depends(get_db)):
    user = db.query(User).filter(User.email == user).first()
    userName= user.name
    return {"message": f"This is {userName} Tasks"}





