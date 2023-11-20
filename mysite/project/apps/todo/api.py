from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from database import orm, connection
from todo import schema, repository
from user.api import get_current_user

router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[schema.TodoSchema])
def get_todos(
    skip: int = 0,
    limit: int = 10,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(connection.get_db),
):
    _todo_list = repository.get_todo_list(db, skip, limit, current_user)
    return _todo_list


@router.post("/", response_model=schema.TodoSchema)
async def post_todos(
    todo: schema.CreateTodoRequest = Body(),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(connection.get_db),
):
    new_todo = repository.create_todo(db, todo, current_user)
    return new_todo


@router.patch("/{todo_id}", response_model=schema.TodoSchema)
async def patch_todos(
    todo_id: int,
    todo_data: schema.UpdateTodoRequest = Body(),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(connection.get_db),
):
    new_todo = repository.update_todo(db, todo_id, todo_data, current_user)
    return new_todo


@router.delete("/{todo_id}", response_model=schema.TodoSchema)
async def delete_todos(
    todo_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(connection.get_db),
):
    new_todo = repository.remove_todo(db, todo_id, current_user)
    return new_todo