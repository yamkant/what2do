from dependency_injector import containers, providers
from apps.account.infra.repository import UserRDBRepository
from apps.account.application.use_case.query import AccountQueryUseCase
from project.infra.database.connection import get_db_session

class AccountContainer(containers.DeclarativeContainer):
    user_repo = providers.Factory(UserRDBRepository)

    query = providers.Factory(
        AccountQueryUseCase,
        user_repo=user_repo,
        db_session=get_db_session,
    )