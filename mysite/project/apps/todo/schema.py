from typing import List, Optional
from pydantic import BaseModel, validator
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

    class Config:
        orm_mode = True