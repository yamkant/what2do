from datetime import time
from typing import Callable, ContextManager, List

from sqlalchemy.orm import Query, Session

from apps.news.repository import PostRDBRepository
from apps.news.query import PostQueryUseCase
from apps.database import orm

class PostCommandUseCase:
    def __init__(
        self,
        post_repo: PostRDBRepository,
        post_query: PostQueryUseCase,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.post_repo = post_repo
        self.post_query = post_query
        self.db_session = db_session