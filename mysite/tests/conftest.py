import pytest
from fastapi.testclient import TestClient

from mysite.main import app

@pytest.fixture
def client():
    return TestClient(app)