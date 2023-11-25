from datetime import time
from typing import Callable, ContextManager, List

from sqlalchemy.orm import Query, Session

from apps.news.repository import PostRDBRepository
from apps.news.query import PostQueryUseCase
from apps.database import orm
from apps.news import schema as post_schema

class PostCommandUseCase:
    def __init__(
        self,
        post_repo: PostRDBRepository,
        post_query: PostQueryUseCase,
        db_session: Callable[[], ContextManager[Session]]
    ) -> post_schema.PostSchema:
        self.post_repo = post_repo
        self.post_query = post_query
        self.db_session = db_session

    def create_post(
        self,
        request: post_schema.PostSchema,
    ):
        new_post = orm.Post(**request)
        with self.db_session() as session:
            self.post_repo.add(session=session, instance=new_post)
            self.post_repo.commit(session=session)
        return new_post