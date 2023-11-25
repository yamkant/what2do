from sqlalchemy.orm import Session
from typing import Callable, ContextManager

from apps.news.repository import PostRDBRepository


class PostQueryUseCase:
    def __init__(
        self,
        post_repo: PostRDBRepository,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.post_repo = post_repo
        self.db_session = db_session

    pass