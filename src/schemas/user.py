import re

from typing import Optional
from pydantic import BaseModel, validator
from fastapi import Depends
from sqlalchemy.orm import Session

from schemas.core import IDModelMixin

from database import get_db
from constants import EMAIL_REGEX

import models


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: Optional[str] = None
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: str
    password: str

    @validator('email', pre=True)
    def validate_email(cls, value: str, ) -> str:
        if re.search(EMAIL_REGEX, value):
            return value
        raise ValueError('Email is not correct format!')


# Properties to receive via API on update
class UserUpdate(UserBase):
    ...


# Properties to receive via API login
class UserLogin(BaseModel):
    username: str
    password: str


class UserInDBBase(UserBase, IDModelMixin):
    class Config:
        orm_mode = True


# Additional properties stored in DB but not returned by API
class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
class User(UserInDBBase):
    ...
