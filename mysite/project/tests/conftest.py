import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apps.shared_kernel.server import app
from apps.database.connection import SessionFactory
from apps.database.orm import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

@pytest.fixture(scope="session")
def test_db():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    SessionFactory.configure(bind=engine)

    db = SessionFactory()
    Base.metadata.create_all(bind=engine)

    yield db
    db.close()

@pytest.fixture
def client(test_db):
    return TestClient(app)

@pytest.fixture(scope="function")
def create_test_user(client):
    response = client.post(
        "/users/",
        json={
            "email": "tester@example.com", 
            "password": "5933", 
            "check_password": "5933", 
        },
    )

@pytest.fixture(scope="function")
def get_logined_client(client, create_test_user):

    response = client.post(
        "users/login/",
        json={
            "email": "tester@example.com",  
            "password": "5933", 
        },
    )
    data = response.json()

    return {
        "client": client,
        "headers": {"Authorization": "Bearer " + data['access_token']},
    }