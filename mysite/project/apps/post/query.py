from sqlalchemy.orm import Session
from typing import Callable, ContextManager

from apps.post.repository import PostRDBRepository
from apps.database import orm
from apps.post import schema as post_schema


class PostQueryUseCase:
    def __init__(
        self,
        post_repo: PostRDBRepository,
        db_session: Callable[[], ContextManager[Session]]
    ):
        self.post_repo = post_repo
        self.db_session = db_session

    def get_post_list(
        self,
        params: post_schema.Page,
    ) -> list[post_schema.NewsPostResponse]:
        with self.db_session() as session:
            post_list = self.post_repo.get_post_list_order_by_id(session=session, skip=params.skip, limit=params.limit)
        print(post_list)
        return post_list