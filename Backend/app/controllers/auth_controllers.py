from ..utils import create_access_token, generate_refresh_token_raw, decode_token
from fastapi import HTTPException, Cookie, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..db import get_db
from ..models.user import User
import bcrypt

def get_current_user(access_token: str=Cookie(None), db: Session=Depends(get_db)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Missings Token")
    
    user_email = decode_token(access_token)
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not Found")
    return {
        "data": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        },
        "meta": "current user",
        "errors": ""
    }


def register_user(data, db):
    user = db.query(User).filter(User.email == data.email).first()
    print(user)
    if user:
        # Code to Redirect to login page
        raise HTTPException(status_code=409, detail="Email Already Registered")
        # Code for redirection
    #Extracting INFO from the arguments
    user_name = data.name
    email = data.email
    password = data.password 
    "Bcrypt generates a salt with a default value of 12 rounds"
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("utf-8")
    #Adding a New User
    new_user = User(
        name=user_name,
        email=email,
        password=hashed_password
    )
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        
        return {
            "data": {
                "id": new_user.id,
                "name": new_user.name,
                "email": new_user.email
            },
            "meta": "User Created Successfully",
            "errors": ""
        }

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email Already Exist")
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database Error")

def login_user(data: dict, response, db):
    try:
        user = db.query(User).filter(User.email == data.email).first()
        print(user)
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    password = data.password #password the user inputted for check
    hashed_password = user.password #hashed password stored in the database

    is_correct = bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")) #return true or false
    print(is_correct)

    if not is_correct:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
            #give them access and refresh token for authentication
    access_token = create_access_token(data={"sub": data.email})
    print(access_token)
        #refresh_token = generate_refresh_token_raw()

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True, #Javascript can't access it
        samesite="strict", #prevent CSRF
        max_age=900 # Only for 15minutes(900/60 = 15)
        ) #will later user secure=True when in prod
        
    return {
        "data": {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        },
        "meta": "Logged in Successfuly",
        "errors": ""
    }  
    

# Later Features I'll be looking to Implement(Including GoogleOauth)
def reset_password():
    pass

