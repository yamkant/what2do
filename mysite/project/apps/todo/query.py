from sqlalchemy.orm import Query, Session
from typing import Callable, ContextManager, List

from apps.todo.repository import TodoRDBRepository
from apps.database import orm
from apps.user import schema as user_schema


class TodoQueryUseCase:
    def __init__(
            self,
            todo_repo: TodoRDBRepository,
            db_session: Callable[[], ContextManager[Session]]
    ):
        self.todo_repo = todo_repo
        self.db_session = db_session

    def get_todo(
        self,
        todo_id: int,
    ) -> orm.Todo:
        with self.db_session() as session:
            _todo = self.todo_repo.get_todo_by_todo_id(session=session, todo_id=todo_id)
        return _todo

    def get_todo_list(
        self,
        user: user_schema.UserSchema,
    ) -> list[orm.Todo]:
        with self.db_session() as session:
            _todo_list = self.todo_repo.get_todos_order_by_id(session=session, user_id=user.id)
        return _todo_list