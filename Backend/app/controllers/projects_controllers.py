from fastapi import HTTPException
from ..models.projects import Project
from ..models.user import User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def priority_checker(digit):
    """ This Functions is to check if the priority digit is high, medium or low, it takes a digit as it's input from 1 to 3"""
    try:
        if digit == '1':
            return "low"
        elif digit == '2':
            return "medium"
        elif digit == '3':
            return "high"
    except ValueError:
        return "Only Digits from 1 to 3"


def create_project(data, db):
    print(data.priority)
    result = priority_checker(data.priority)
    print(result)

    new_project = Project(
        title=data.title,
        description=data.description,
        priority=result,
        deadline=data.deadline
    )
    print(new_project)
    db.add(new_project)
    try:
        db.commit()
        db.refresh(new_project)
        return {"message": "Project successfully added"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Project title is conflicting")
    

def get_all_projects(user_id, db):
    user = db.query(User).filter(User.id == user_id).first()
    print(user.name)
    try:
        print(user.projects)
        user.projects
        return {"message": "Retrived user's task's successfully"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    
def get_specific_project(user_id, project_id, db):
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    try:
        print(user.projects[project_id])
        return {"message": "Retrived user's task's successfully"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    

def update_project_title(user_id, project_id, project_update, db):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="No User")

    print(user)
    try:
        project = user.projects[project_id].title()
        update_project = project_update.dict(exclude_unset=True)

        for key, value in update_project.items():
            setattr(project, key, value) 
        
    except SQLAlchemyError:
        raise HTTPException(status_code=401, detail="Database Error")


    


    











# Endpoint for Project
# POST /api/v1/projects saves project object
# GET /api/v1/projects returns all project for the user
# GET /api/v1/projects/{id} returns one project needed with all its metadata
# PATCH /api/v1/projects/{id} updatas/patch projects title or name(details)
# DELETE /api/v1/projects/{id}