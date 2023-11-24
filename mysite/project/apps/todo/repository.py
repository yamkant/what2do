from sqlalchemy import text

from apps.database import orm
from apps.shared_kernel.repository import RDBRepository

class TodoRDBRepository(RDBRepository):
    @staticmethod
    def get_todo_by_todo_id(session, todo_id: int) -> orm.Todo:
        todo = session.query(orm.Todo).filter_by(
            id = todo_id, deleted_at = None
        ).first()
        return todo

    @staticmethod
    def get_todos_order_by_id(session, user_id: int) -> list[orm.Todo]:
        todo_list = session.query(orm.Todo).filter_by(
            deleted_at=None, 
            user_id=user_id,
        ).order_by(text("id desc")).all()
        return todo_list