from pydantic import BaseModel

class UploadNewsPostResponse(BaseModel):
    id: int
    title: str

class NewsPostResponse(BaseModel):
    id: int
    title: str

class Page(BaseModel):
    skip: int = 0
    limit: int = 10

class PostSchema(BaseModel):
    id: int
    title: str
    published_at: str
    author: str
    body: str
    url: str

    class Config:
        orm_mode = True