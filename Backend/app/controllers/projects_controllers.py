from fastapi import HTTPException
from ..models.projects import Project
from ..models.user import User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from ..utils import priority_checker


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
    try:
        project = db.query(Project).filter(Project.user_id == user_id).all()

        if not project:
            raise HTTPException(status_code=404, detail="No Project Found")
        return {"projects": project}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    

# Incomplete function
def get_specific_project(user_id, project_id, db):
    try:
        project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user_id).first()
        print(project)
        return {"message": "Retrived user's task's successfully"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    
    
def update_project(user_id, project_id, project_update, db):
    try:
        project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user_id).first()
        if not project:
            raise HTTPException(status_code=404, detail="No Project Found")
        update_project = project_update.dict(exclude_unset=True)

        for key, value in update_project.items():
            setattr(project, key, value)
        return {"message": "Project Updated Successfully"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")


def delete_project(user_id, project_id, db):
    try:
        project = db.query(Project).filter(Project.id == project_id, Project.owner_id == user_id).first()
        project.is_deleted = True
        db.add(project)
        db.commit()
        db.refresh(project)
        return {"message": "Successfully Deleted, you can still undo project"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")


    


    











# Endpoint for Project
# POST /api/v1/projects saves project object
# GET /api/v1/projects returns all project for the user
# GET /api/v1/projects/{id} returns one project needed with all its metadata
# PATCH /api/v1/projects/{id} updatas/patch projects title or name(details)
# DELETE /api/v1/projects/{id}