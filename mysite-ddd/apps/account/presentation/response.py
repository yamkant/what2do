from typing import List

from pydantic import BaseModel

from project.presentation.response import BaseResponse


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    is_active: bool
    # items: list[Item] = []

    class Config:
        from_attributes = True

class UserResponse(BaseResponse):
    result: List[UserSchema]
