
from apps.database import orm

from apps.shared_kernel.repository import RDBRepository


class TodoRDBRepository(RDBRepository):
    @staticmethod
    def get_todo_by_todo_id(session, todo_id: int) -> orm.Todo:
        todo = session.query(orm.Todo).filter(
            orm.Todo.id == todo_id, orm.Todo.deleted_at == None
        ).first()
        print("TODO:============", todo)
        return todo

