from ..utils import create_access_token, generate_refresh_token_raw, decode_token
from fastapi import HTTPException, Cookie, status
from ..models.user import User
from ..models.tasks import Tasks
import bcrypt

def get_current_user(access_token: str = Cookie(None)):
    print(access_token)
    if not access_token:
        raise HTTPException(status_code=401, detail="Missings Token")
    
    user = decode_token(access_token)
    print(user)
    return user


def register_user(data, db):
    user = db.query(User).filter(User.email == data.email).first()
    print(user)
    try:
        if user:
            raise HTTPException(status_code=400, detail="Recheck your email")
            # Code for redirection
        #Extracting INFO from the arguments
        user_name = data.name
        email = data.email
        password = data.password 
        "Bcrypt generates a salt with a default value of 12 rounds"
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode("utf-8")
        print(hashed_password)
        #Adding a New User
        new_user = User(
            name=user_name,
            email=email,
            password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "Successfully registered"}, 201
    except Exception as e:
        print(f"This is the errors as {e}")


def login_user(data: dict, response, db):
    try:
        user = db.query(User).filter(User.email == data.email).first()
        print(user)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
    
        password = data.password #password the user inputted for check
        hashed_password = user.password #hashed password stored in the database

        is_correct = bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")) #return true or false
        print(is_correct)

        if not user or not is_correct:
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
        
        return {"message": "Login Successfull"}, 200

        
    except Exception as e:
        print(f"This is the error {e}")
    



# Later Features I'll be looking to Implement(Including GoogleOauth)
def reset_password():
    pass

