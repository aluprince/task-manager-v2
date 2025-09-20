from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Tasks(BaseModel):
    title: str
    description: str
    completed: bool
    deadline: str
    priority: str
    created_at: datetime
   
