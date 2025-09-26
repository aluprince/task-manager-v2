from pydantic import BaseModel
from typing import Optional


class ProjectCreate(BaseModel):
    title: str
    description: str
    priority: str
    deadline: str

class newProject(BaseModel):
    title: Optional[str]
    description: Optional[str]
    deadline: Optional[str]

class ProjectUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    priority: Optional[str]
    deadline: Optional[str]

    
    