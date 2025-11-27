from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Base User Schema
# This schema is used to validate the user data that is sent to the API
class UserBase(BaseModel):
    email: EmailStr
    full_name: str


# User Create Schema
# This schema is used to create a new user
class UserCreate(UserBase):
    password: str


# User Update Schema
# This schema is used to update the user data that is sent to the API
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None


# User Response Schema
# This schema is used to return the user data to the client
# from_attributes = True is used to convert the SQLAlchemy model to a Pydantic model

class UserResponse(BaseModel):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[EmailStr] = None
    
