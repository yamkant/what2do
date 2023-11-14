from typing import Callable, ContextManager, List

from sqlalchemy.orm import Session

from apps.account.infra.repository import UserRDBRepository

from apps.account.domain.entity.user import User

class AccountQueryUseCase:
    def __init__(self, user_repo: UserRDBRepository, db_session: Callable[[], ContextManager[Session]]):
        self.user_repo = user_repo
        self.db_session = db_session
    
    def get_users(self) -> List[User]:
        with self.db_session() as session:
            users: List[User] = list(
                self.user_repo.get_users(session=session)
            )
        return users

