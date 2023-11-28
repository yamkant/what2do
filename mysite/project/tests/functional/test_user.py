from schema import Schema, Or, And
from starlette import status

from apps.database import orm
from apps.shared_kernel.utils import now

## ==========================================================
#  회원가입 관련 테스트
#  ==========================================================

def test_유저가_새로_가입한다(client):
    # given

    # when
    response = client.post(
        "users/",
        json={
            "email": "test_user@example.com", 
            "password": "5933", 
            "check_password": "5933", 
        },
    )
    assert response.status_code == status.HTTP_200_OK

    # then
    schema = Schema({
        "id": 1,
        "email": "test_user@example.com", 
    })
    assert schema.is_valid(response.json())


def test_가입시_이미_존재하는_이메일을_사용할_수_없다(client, test_db):
    # given
    new_user = orm.User(email="unique_user@example.com", hashed_password="5933")
    test_db.add(new_user)
    test_db.commit()

    # when
    response = client.post(
        "users/",
        json={
            "email": "unique_user@example.com", 
            "password": "5933", 
            "check_password": "5933", 
        },
    )

    # then
    schema = Schema({
        "error_code": "USER__ALREADY_REGISTERED",
        "message": "email aleady registered",
    })
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert schema.is_valid(response.json())


def test_가입시_이메일을_입력해야한다(client):
    # given
    req_data = {
        "password": "5933", 
        "check_password": "5933", 
    }

    # when
    response = client.post(
        "users/",
        json=req_data
    )

    # then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_가입시_비밀번호를_입력해야한다(client):
    # given
    req_data = {
        "email": "unique_user@example.com", 
        "check_password": "5933", 
    }

    # when
    response = client.post(
        "users/",
        json=req_data
    )

    # then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_가입시_확인_비밀번호를_입력해야한다(client):
    # given
    req_data = {
        "email": "unique_user@example.com", 
        "password": "5933", 
    }

    # when
    response = client.post(
        "users/",
        json=req_data
    )

    # then
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


## ==========================================================
#  로그인 관련 테스트
#  ==========================================================

def test_정상적으로_로그인을_성공한다(client, create_test_user):
    # given
    req_data = {
        "email": "tester@example.com", 
        "password": "5933", 
    }

    # when
    response = client.post(
        "users/login",
        json=req_data,
    )

    # then
    schema = Schema({
        "access_token": And(str, len),
        "email": req_data["email"],
        "token_type": "bearer",
    })
    assert response.status_code == status.HTTP_200_OK
    assert schema.is_valid(response.json())


def test_로그인시_이메일이_제대로_입력되어야한다(client, create_test_user):
    # given
    req_data = {
        "email": "tester!@example.com", 
        "password": "5933", 
    }

    # when
    response = client.post(
        "users/login",
        json=req_data,
    )

    # then
    schema = Schema({
        'error_code': 'USER__INVALID_TOKEN',
        'message': 'Invalid token.',
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert schema.is_valid(response.json())


def test_로그인시_비밀번호가_제대로_입력되어야한다(client, create_test_user):
    # given
    req_data = {
        "email": "tester@example.com", 
        "password": "59334", 
    }

    # when
    response = client.post(
        "users/login",
        json=req_data,
    )

    # then
    schema = Schema({
        'error_code': 'USER__LOGIN_ERROR',
        'message': 'Incorrect username or password',
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert schema.is_valid(response.json())
