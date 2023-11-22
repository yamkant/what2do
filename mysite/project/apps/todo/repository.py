from sqlalchemy.orm import Session
from datetime import datetime, time

from apps.database import orm
from apps.user import schema as user_schema
from apps.todo import schema as todo_schema
from apps.shared_kernel.utils import now

from apps.shared_kernel.repository import RDBRepository


class TodoRDBRepository(RDBRepository):
    # @staticmethod
    # def get_reservation_by_reservation_number(session, reservation_number: ReservationNumber) -> Reservation | None:
    #     return session.query(Reservation).filter_by(reservation_number=reservation_number).first()

    # @staticmethod
    # def get_room_by_room_number(session, room_number: str) -> Room | None:
    #     return session.query(Room).filter_by(number=room_number).first()

    @staticmethod
    def get_todo_by_todo_id(session, todo_id: int):
        todo = session.query(orm.Todo).filter_by(
            orm.Todo.id == todo_id, orm.Todo.deleted_at == None
        ).first()
        return todo

