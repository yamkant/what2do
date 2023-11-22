from sqlalchemy.orm import Query, Session
from typing import Callable, ContextManager, List

from apps.user.repository import UserRDBRepository
from apps.database import orm
from apps.user import schema as user_schema


class UserQueryUseCase:
    def __init__(
        self,
        user_repo: UserRDBRepository,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.user_repo = user_repo
        self.db_session = db_session
    
    def get_user(
        self,
        email: str
    ) -> orm.User:
        with self.db_session() as session:
            user = session.query(orm.User).filter(orm.User.email == email).first()
        return user
