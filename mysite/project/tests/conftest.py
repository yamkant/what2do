from fastapi import Depends
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.pool import StaticPool

from datetime import datetime, timedelta
from jose import JWTError, jwt
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")


import os

from ..apps.database import orm, connection
from ..apps.user import repository as user_repository
from main import app, get_db, get_current_user

TEST_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def test_db():
    test_db_url = TEST_DATABASE_URL
    if not database_exists(test_db_url):
        create_database(test_db_url)

    engine = create_engine(test_db_url)
    orm.Base.metadata.create_all(engine)
    # metadata.create_all(engine)
    try:
        yield engine
    finally:
        orm.Base.metadata.drop_all(engine)
        # metadata.drop_all(engine)


@pytest.fixture(scope="function")
def test_session(test_db):
    connection = test_db.connect()

    trans = connection.begin()
    session = sessionmaker()(bind=connection)

    session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(session, transaction):
        """
        Each time that SAVEPOINT ends, reopen it
        """
        if transaction.nested and not transaction._parent.nested:
            session.begin_nested()

    yield session

    session.close()
    trans.rollback()
    connection.close()


@pytest.fixture
def client():
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    orm.Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.fixture
def authorized_client(client, test_session):
    test_user = orm.User(email="test@gmail.com", hashed_password="5933")
    test_session.add(test_user)
    test_session.commit()
    data = {
        "sub": test_user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    client.headers = {
        "Authorization": f"Bearer {access_token}"
    }

    return {
        "client": client,
        "user": test_user,
        "session": test_session,
    }

