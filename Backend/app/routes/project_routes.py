from sqlalchemy.orm import Session
from ..controllers.projects_controllers import create_project, get_all_projects, get_specific_project
from fastapi import Depends, APIRouter, status
from ..schemas.projects_schema import ProjectCreate
from ..db import get_db


router = APIRouter(
    prefix="/api/v1",
    tags=["Project"]
)

@router.post("/projects", status_code=status.HTTP_201_CREATED) #Implement a model_response later
def create_new_project(data: ProjectCreate, db: Session=Depends(get_db)):
    return create_project(data, db)

@router.get("/projects", status_code=status.HTTP_200_OK)
def get_projects(user_id: int, db: Session=Depends(get_db)):
    return get_all_projects(user_id, db)

@router.get("/projects/{project_id}", status_code=status.HTTP_200_OK)
def getSpecificProject(user_id: str, project_id: int, db: Session=Depends(get_db)):
    return get_specific_project(user_id, project_id, db)


