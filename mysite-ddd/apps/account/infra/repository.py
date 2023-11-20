from project.infra.database.repository import RDBRepository
from sqlalchemy.orm import Query, Session
from apps.account.domain.entity.user import User

class UserRDBRepository(RDBRepository):
    @staticmethod
    def get_users(session: Session) -> Query:
        return session.query(User)