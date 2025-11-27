from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.api.dependencies import get_current_user
from app.models.user import User
from app.services.task_service import TaskService

# Task Router
router = APIRouter()


@router.get('/tasks', response_model=List[TaskResponse])
def get_tasks(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: User = Depends(get_current_user)
):
    tasks = TaskService.get_tasks(db, owner_id=current_user, skip=skip, limit=limit)

    return tasks


@router.post('/', response_model=TaskResponse)
def create_task(
        task: TaskCreate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return TaskService.create_task(db, task=task, user_id=current_user.id)


@router.get('/{task_id}', response_model=TaskResponse)
def get_task(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    task = TaskService.get_task_by_id(db, task_id=task_id,user_id=current_user.id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found")

    return task


@router.put('/{task_id}', response_model=TaskResponse)
def update_task(
        task_id: int,
        task: TaskUpdate,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    task = TaskService.get_task_by_id(db, task_id=task_id, user_id=current_user.id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task


@router.delete('/{task_id}', response_model=TaskResponse)
def delete_task(
        task_id: int,
        current_user: User = Depends(get_current_user),
        db: Session = Depends(get_db)
):
    success = TaskService.delete_task(db, task_id=task_id, user_id=current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task Not Found"
        )

    return { "message" : "Task deleted successfully" }
