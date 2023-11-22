from dependency_injector import containers, providers

from apps.user.repository import UserRDBRepository
from apps.user.query import UserQueryUseCase
from apps.user.command import UserCommandUseCase
from apps.database.connection import get_db

class UserContainer(containers.DeclarativeContainer):
    user_repo = providers.Factory(UserRDBRepository)

    user_query = providers.Factory(
        UserQueryUseCase,
        user_repo=user_repo,
        db_session=get_db,
    )

    user_command = providers.Factory(
        UserCommandUseCase,
        user_repo=user_repo,
        user_query=user_query,
        db_session=get_db,
    )