from typing import Optional
from pydantic import BaseModel, Field


class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
