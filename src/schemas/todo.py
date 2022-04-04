from typing import Optional
from pydantic import BaseModel, Field


class TodoBase(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(
        gt=0,
        lt=6,
        description='The priority must be between 1 and 6')
    complete: bool
    owner_id: int

    class Config:
        orm_mode = True


class Todo(TodoBase):
    pass
