from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time

class CreateTodoRequest(BaseModel):
    content: str

class UpdateTodoRequest(BaseModel):
    content: str
    completed: str

    started_at: Optional[datetime]
    ended_at: Optional[datetime]

class TodoSchema(BaseModel):
    id: int
    content: str
    completed: str

    started_at: Optional[datetime]
    ended_at: Optional[datetime]

    deleted_at: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True