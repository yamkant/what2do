from fastapi import APIRouter, Depends, Body, HTTPException
from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import Session
from starlette import status

from apps.database import orm, connection
from apps.todo import schema, repository
from apps.todo.query import TodoQueryUseCase
from apps.todo.command import TodoCommandUseCase
from apps.shared_kernel.container import AppContainer
from apps.user.api import get_current_user

from apps.todo.exception import TodoContentException

router = APIRouter(prefix="/todos")


@router.get("/", response_model=list[schema.TodoSchema])
@inject
def get_todos(
    current_user: str = Depends(get_current_user),
    todo_query: TodoQueryUseCase = Depends(Provide[AppContainer.todo.todo_query]),
):
    _todo_list = todo_query.get_todo_list(current_user)
    return _todo_list


@router.post("/", response_model=schema.TodoSchema)
@inject
async def post_todos(
    current_user: str = Depends(get_current_user),
    todo: schema.CreateTodoRequest = Body(),
    todo_command: TodoCommandUseCase = Depends(Provide[AppContainer.todo.todo_command]),
):
    try:
        new_todo = todo_command.create_todo(todo, current_user)
    except TodoContentException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    return new_todo


@router.patch("/{todo_id}", response_model=schema.TodoSchema)
@inject
async def patch_todos(
    todo_id: int,
    update_todo_request: schema.UpdateTodoRequest = Body(),
    current_user: str = Depends(get_current_user),
    todo_command: TodoCommandUseCase = Depends(Provide[AppContainer.todo.todo_command]),
):
    try:
        print("DEBUG1=============================")
        updated_todo = todo_command.update_todo(todo_id=todo_id, request=update_todo_request, user=current_user)
    # TODO: start time보다 end time이 더 빠르면 예외 처리
    except TodoContentException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message
        )
    return updated_todo


@router.delete("/{todo_id}", response_model=schema.TodoSchema)
@inject
async def delete_todos(
    todo_id: int,
    current_user: str = Depends(get_current_user),
    todo_command: TodoCommandUseCase = Depends(Provide[AppContainer.todo.todo_command]),
):
    todo = todo_command.remove_todo(todo_id=todo_id, user=current_user)
    return todo