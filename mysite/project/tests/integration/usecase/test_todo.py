import pytest
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, Session

from apps.todo.query import TodoQueryUseCase
from apps.todo.repository import TodoRDBRepository
from apps.user.repository import UserRDBRepository
from apps.database import orm
from apps.shared_kernel.utils import get_current_time


TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

@contextmanager
def db_session():
    db = SessionFactory()

    if not database_exists(TEST_DATABASE_URL):
        create_database(TEST_DATABASE_URL)

    engine = create_engine(TEST_DATABASE_URL)
    orm.Base.metadata.create_all(engine)
    try:
        yield db
    finally:
        # orm.Base.metadata.drop_all(engine)
        db.close()


@pytest.fixture(scope="function")
def test_user():
    user_repo = UserRDBRepository()

    test_user = orm.User(email="test@gmail.com", hashed_password="5933")
    with db_session() as session:
        user_repo.add(session=session, instance=test_user)
        user_repo.commit(session=session)
    return test_user

# class TestTodoQueryUseCase:
todo_repo = TodoRDBRepository()
todo_query = TodoQueryUseCase(
    todo_repo=TodoRDBRepository,
    db_session=db_session
)

def test_get_todo():
    # given
    new_todo = orm.Todo(content="New", completed="N")
    with db_session() as session:
        todo_repo.add(session=session, instance=new_todo)
        todo_repo.commit(session=session)

    # when
    todo = todo_query.get_todo(new_todo.id)

    # then
    assert todo.id == new_todo.id
    assert todo.content == new_todo.content
    assert todo.completed == "N"
    orm.Base.metadata.drop_all(engine)


def test_get_todo_list(test_user):
    # given
    TODO_COUNT = 3
    for i in range(TODO_COUNT):
        new_todo = orm.Todo(content="New", completed="N", user_id=test_user.id)
        with db_session() as session:
            todo_repo.add(session=session, instance=new_todo)
            todo_repo.commit(session=session)

    # when
    todo_list = todo_query.get_todo_list(test_user)

    # then
    assert len(todo_list) == TODO_COUNT
    orm.Base.metadata.drop_all(engine)


def test_get_todo_list_삭제된_todo가_있는_경우(test_user):
    # given
    TODO_COUNT = 3
    for i in range(TODO_COUNT):
        new_todo = orm.Todo(content="New", completed="N", user_id=test_user.id)
        with db_session() as session:
            todo_repo.add(session=session, instance=new_todo)
            todo_repo.commit(session=session)
    deleted_todo = orm.Todo(
        content="New",
        completed="N",
        deleted_at=get_current_time(),
        user_id=test_user.id
    )
    with db_session() as session:
        todo_repo.add(session=session, instance=deleted_todo)
        todo_repo.commit(session=session)

    # when
    todo_list = todo_query.get_todo_list(test_user)
    for todo in todo_list:
        print(todo.deleted_at)

    # then
    assert len(todo_list) == TODO_COUNT
    orm.Base.metadata.drop_all(engine)