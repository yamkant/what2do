from pydantic import BaseModel

from apps.todo.schema import TodoSchema

class UserBase(BaseModel):
    email: str

class CreateUserRequest(UserBase):
    password: str

class LoginUser(UserBase):
    password: str

class UserSchema(UserBase):
    id: int
    # is_active: bool
    # todos: list[TodoSchema] = []

    class Config:
        orm_mode = True

class TokenSchema(BaseModel):
    access_token: str
    token_type: str
    email: str
