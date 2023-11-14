from typing import Callable, ContextManager, List

from sqlalchemy.orm import Query, Session

from apps.users.entity import User
from apps.users.repository import UserRDBRepository


class UserQueryUseCase:
    def __init__(self, user_repo: UserRDBRepository, db_session: Callable[[], ContextManager[Session]]):
        self.user_repo = user_repo
        self.db_session = db_session
