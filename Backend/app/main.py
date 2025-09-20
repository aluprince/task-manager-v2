from . import db
import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import auth_routes, user_routes, tasks_routes

app = FastAPI()
load_dotenv(find_dotenv())

base_url = os.getenv("BASE_URL") #Incase i want to change localhost in the future 
print(base_url)
# Middleware for solving CORS issue

# app.add_middleware(
#     CORSMiddleware,
#     allow_origin=["http://localhost:3000"],
#     allow_credentials=True, #allowing credentials since using cookies and jwt 
#     allow_methods=["*"], #will specify later when in prod
#     allow_headers=["*"] #will specify headers needed later
# )

# Registering routes in my servers
app.include_router(auth_routes.router)


@app.get("/")
def home():
    return {"welcome": "Welcome to the Task Manager V2 API"}


    