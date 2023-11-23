from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time

class CreateTodoRequest(BaseModel):
    content: str

class UpdateTodoRequest(BaseModel):
    content: str
    completed: str

    started_at: Optional[time]
    ended_at: Optional[time]

class TodoSchema(BaseModel):
    id: int
    content: str
    completed: str

    started_at: Optional[datetime]
    ended_at: Optional[datetime]

    deleted_at: Optional[datetime]

    class Config:
        orm_mode = True