from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Task Base Schema
# This schema is used to validate the task data that is sent to the API
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False


# Task Create Schema
# This schema is used to create a new task
class TaskCreate(TaskBase):
    pass

 
# Task Update Schema
# This schema is used to update the task data that is sent to the API
class TaskUpdate(TaskBase):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskResponse(TaskBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True



