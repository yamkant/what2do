from typing import Callable, ContextManager, List, Optional
from passlib.context import CryptContext

from sqlalchemy.orm import Session

from apps.user.repository import UserRDBRepository
from apps.user.query import UserQueryUseCase
from apps.database import orm
from apps.user import schema as user_schema
from apps.user.exception import AleadyRegisteredUserException, PasswordDoesNotMatchException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCommandUseCase:
    def __init__(
        self,
        user_repo: UserRDBRepository,
        user_query: UserQueryUseCase,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.user_repo = user_repo
        self.user_query = user_query
        self.db_session = db_session


    def create_user(
        self,
        request: user_schema.CreateUserRequest
    ) -> Optional[user_schema.UserSchema]:
        if request.password != request.check_password:
            raise PasswordDoesNotMatchException

        new_user = self.user_query.get_user(email=request.email)
        if new_user:
            raise AleadyRegisteredUserException

        password = pwd_context.hash(request.password)
        new_user = orm.User(email=request.email, hashed_password=password)
        with self.db_session() as session:
            self.user_repo.add(session=session, instance=new_user)
            self.user_repo.commit(session=session)
        return new_user
