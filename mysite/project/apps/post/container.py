from dependency_injector import containers, providers

from apps.post.repository import PostRDBRepository
from apps.post.query import PostQueryUseCase
from apps.post.command import PostCommandUseCase
from apps.database.connection import get_db

class PostContainer(containers.DeclarativeContainer):
    post_repo = providers.Factory(PostRDBRepository)

    post_query = providers.Factory(
        PostQueryUseCase,
        post_repo=post_repo,
        db_session=get_db,
    )

    post_command = providers.Factory(
        PostCommandUseCase,
        post_repo=post_repo,
        post_query=post_query,
        db_session=get_db,
    )