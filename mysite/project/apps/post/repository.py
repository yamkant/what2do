from sqlalchemy import text

from apps.shared_kernel.repository import RDBRepository
from apps.database import orm

class PostRDBRepository(RDBRepository):
    @staticmethod
    def get_post_list_order_by_id(session, skip: int, limit: int) -> list[orm.Post]:
        post_list = session.query(orm.Post).order_by(text("id desc")).offset(skip).limit(limit)
        return post_list