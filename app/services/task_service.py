from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:

    # Get All Tasks by User ID (Owner ID) (User ID is the user who is getting the tasks)
    @staticmethod
    def get_tasks(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
        return db.query(Task).filter(Task.owner_id == owner_id).offset(skip).limit(limit).all()


    # Get Task by ID (Task ID is the task id) (User ID is the user who is getting the task)
    @staticmethod
    def get_task_by_id(db: Session, task_id: int, user_id: int):
        return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()


    # Create Task by User ID (Owner ID) (User ID is the user who is creating the task)
    @staticmethod
    def create_task(db: Session, task: TaskCreate, user_id: int):
        db_task = Task(**task.model_dump(), owner_id = user_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    # Update Task by ID (Partial Update)
    @staticmethod
    def update_task(db: Session, task_id: int, task_update: TaskUpdate, user_id: int):
        db_task = TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return None

        update_data = task_update.dict(exclude_unset = True)
        for field, value in update_data.items():
            setattr(db_task, field, value)

        db.commit()
        db.refresh(db_task)
        return db_task


    # Delete Task by ID (Soft Delete)
    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int):
        db_task = TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return False

        db.delete(db_task)
        db.commit()
        return True
        