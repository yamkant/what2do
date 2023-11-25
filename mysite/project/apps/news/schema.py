from typing import Optional
from pydantic import BaseModel
from datetime import datetime, time

class PostSchema(BaseModel):
    id: int
    published_at: str
    author: str
    body: str

    class Config:
        orm_mode = True