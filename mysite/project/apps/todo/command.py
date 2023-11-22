from sqlalchemy.orm import Query, Session
from typing import Callable, ContextManager, List

from apps.todo.repository import TodoRDBRepository
from apps.database import orm
from apps.todo import schema as todo_schema
from apps.user import schema as user_schema


class TodoCommandUseCase:
    def __init__(self, todo_repo: TodoRDBRepository, db_session: Callable[[], ContextManager[Session]]):
        self.todo_repo = todo_repo
        self.db_session = db_session

    def create_todo(
        self,
        todo: todo_schema.Todo,
        user: user_schema.User = None,
    ):
        with self.db_session() as session:
            new_todo = orm.Todo(content=todo.content, completed="N", user_id=user.id)
            session.add(new_todo)
            session.commit()
            session.refresh(new_todo)
        return new_todo


    # def update_todo(
    #     db: Session,
    #     todo_id: int,
    #     request: todo_schema.UpdateTodoRequest,
    #     user: user_schema.User = None,
    # ):
    #     todo = get_todo(db=db, todo_id=todo_id, user_id=user.id)

    #     update_data = request.dict(exclude_unset=True)
    #     for key, value in update_data.items():
    #         if isinstance(value, time):
    #             value = datetime.combine(datetime.today().date(), value)
    #         setattr(todo, key, value)
        
    #     db.commit()
    #     db.refresh(todo)
    #     return todo


    # def remove_todo(
    #     db: Session,
    #     todo_id: int,
    #     user: user_schema.User = None,
    # ):
    #     todo = get_todo(db=db, todo_id=todo_id, user_id=user.id)
    #     todo.deleted_at = now()
    #     db.commit()
    #     return todo