# Postgres configuration
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

password = os.getenv("PASSWORD")
print(password)
DATABASE_NAME = os.getenv("DATABASE_NAME")

DATABASE_URL = f"postgresql+psycopg2://postgres:{password}@localhost:5432/task-manager-v2"


