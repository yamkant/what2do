from datetime import datetime, time
from typing import Callable, ContextManager, List

from sqlalchemy.orm import Query, Session

from apps.todo.repository import TodoRDBRepository
from apps.todo.query import TodoQueryUseCase
from apps.database import orm
from apps.todo import schema as todo_schema
from apps.user import schema as user_schema
from apps.shared_kernel.utils import now



class TodoCommandUseCase:
    def __init__(
        self,
        todo_repo: TodoRDBRepository,
        todo_query: TodoQueryUseCase,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.todo_repo = todo_repo
        self.todo_query = todo_query
        self.db_session = db_session


    def create_todo(
        self,
        request: todo_schema.TodoSchema,
        user: user_schema.UserSchema,
    ):
        new_todo = orm.Todo(content=request.content, completed="N", user_id=user.id)
        with self.db_session() as session:
            self.todo_repo.add(session=session, instance=new_todo)
            self.todo_repo.commit(session=session)
        return new_todo


    def update_todo(
        self,
        todo_id: int,
        request: todo_schema.UpdateTodoRequest,
        user: user_schema.UserSchema,
    ):
        todo = self.todo_query.get_todo(todo_id=todo_id)
        # TODO: 해당 유저가 todo_id의 todo를 가지는지 판단
        update_data = request.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            if isinstance(value, time):
                value = datetime.combine(datetime.today().date(), value)
            setattr(todo, key, value)
        with self.db_session() as session:
            self.todo_repo.add(session=session, instance=todo)
            self.todo_repo.commit(session=session)
        return todo


    def remove_todo(
        self,
        todo_id: int,
        user: user_schema.UserSchema = None,
    ) -> None:
        todo = self.todo_query.get_todo(todo_id=todo_id)
        # TODO: 해당 유저가 todo_id의 todo를 가지는지 판단
        todo.deleted_at = now()
        with self.db_session() as session:
            self.todo_repo.add(session=session, instance=todo)
            self.todo_repo.commit(session=session)