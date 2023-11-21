from typing import List, Optional
from pydantic import BaseModel, validator

class CreateTodoRequest(BaseModel):
    content: str

class UpdateTodoRequest(BaseModel):
    content: str
    completed: str

class TodoSchema(BaseModel):
    id: int
    content: str
    completed: str

    class Config:
        orm_mode = True