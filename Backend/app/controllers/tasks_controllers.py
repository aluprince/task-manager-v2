from ..models.tasks import Task
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from ..utils import priority_checker

def create_task(data, db):
    new_task = Task(
        title=data.title,
        description=data.description,
        deadline=data.deadline,
        priority=priority_checker(data.priority),
        completed=data.completed,
    )
    db.add(new_task)
    try:
        db.commit()
        db.refresh(new_task)
        return {"message": "Task successfully added"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    
def get_all_tasks(user_id, db):
    try:
        tasks = db.query(Task).filter(Task.owner_id == user_id).all()
        if not tasks:
            raise HTTPException(status_code=404, detail="No Task Found")
        return {"tasks": tasks}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    
def update_task(user_id, task_id, task_update, db):
    try:
        task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="No Task Found")
        update_task = task_update.dict(exclude_unset=True)

        for key, value in update_task.items():
            setattr(task, key, value)
        
        db.commit()
        db.refresh(task)
        return {"message": "Task successfully updated"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")
    
def delete_task(user_id, task_id, db):
    try:
        task = db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="No Task Found")
        db.delete(task)
        db.commit()
        return {"message": "Task successfully deleted"}
    except SQLAlchemyError:
        raise HTTPException(status_code=500, detail="Database Error")