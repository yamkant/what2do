from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time

class CreatePostResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True

class PostSchema(BaseModel):
    id: int
    title: str
    published_at: str
    author: str
    body: str

    class Config:
        orm_mode = True