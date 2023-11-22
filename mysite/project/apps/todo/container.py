from dependency_injector import containers, providers

from apps.todo.repository import TodoRDBRepository
from apps.todo.query import TodoQueryUseCase
from apps.todo.command import TodoCommandUseCase
from apps.database.connection import get_db

class TodoContainer(containers.DeclarativeContainer):
    todo_repo = providers.Factory(TodoRDBRepository)

    todo_query = providers.Factory(
        TodoQueryUseCase,
        todo_repo=todo_repo,
        db_session=get_db,
    )

    todo_command = providers.Factory(
        TodoCommandUseCase,
        todo_repo=todo_repo,
        todo_query=todo_query,
        db_session=get_db,
    )