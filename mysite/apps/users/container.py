from dependency_injector import containers, providers
from apps.users.repository import UserRDBRepository
from apps.users.query import UserQueryUseCase
from apps.sql_app.database import get_db_session

class UserContainer(containers.DeclarativeContainer):
    user_repo = providers.Factory(UserRDBRepository)

    query = providers.Factory(
        UserRDBRepository,
        UserQueryUseCase,
        db_session=get_db_session,
    )