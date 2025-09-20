import os, hashlib, secrets
from datetime import datetime, timezone, timedelta #timedelta stores a length of time, such as a number of days, seconds, microseconds
from jose import jwt
from fastapi import Depends, HTTPException, status
from jose.exceptions import JWTError, ExpiredSignatureError
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "30"))

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """ This functions create an access token for authorization and authentication use"""
    to_encode = data.copy() #to take in user info
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire}) #JWT needs an expire claim
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALG)

    return encoded_jwt

def decode_token(token: str):
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[JWT_ALG]
        )
        user_id: str = payload.get("sub")
        if user_id == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="This User was not found, Unauthorized!"
            )
        # Checking if the Token has Expired
        exp = payload.get("exp")
        if exp is None or datetime.now(timezone.utc).timestamp() > exp:
            print('Token Time has Expired')
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired"
            )
        return user_id

    except ExpiredSignatureError:
        print("Expired Signature")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is Expired"
        )
    except JWTError:
        print("Invalid Token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )


def generate_refresh_token_raw():
    """ Generates a password-like refresh token, Not a JWT token custom-made """
    return secrets.token_urlsafe(64)

def hash_token(token: str) -> str:
    """This function hashes the refresh token"""
    return hashlib.sha256(token.encode()).hexdigest()










