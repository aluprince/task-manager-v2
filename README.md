# Task Manager V2 (FastAPI + PostgreSQL)

A task manager backend built with FastAPI, PostgreSQL, and JWT authentication.

## Features
- Register
- Login (JWT-based, stored in cookies)
- Protected `/me` endpoint

## Setup
```bash
git clone <your-repo>
cd Task-Manager-V2
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
