from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str
