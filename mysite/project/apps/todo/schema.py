from typing import List, Optional
from pydantic import BaseModel, validator

class CreateTodoRequest(BaseModel):
    content: str

    # @validator("content")
    # def validate_content(cls, content: str) -> str:
    #     if not content:
    #         raise ValueError("Content is required")
    #     return content

class UpdateTodoRequest(BaseModel):
    content: str
    completed: str

    # @validator("content")
    # def validate_content(cls, content: str) -> str:
    #     if not content:
    #         raise ValueError("Content is required")
    #     return content

class TodoSchema(BaseModel):
    id: int
    content: str
    completed: str

    class Config:
        orm_mode = True