from pydantic import BaseModel
from typing import Optional


class Notification(BaseModel):
    id: int
    task_id: int
    user_id: int
    status: str
    sent_at: bool = False

    