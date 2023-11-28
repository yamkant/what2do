from schema import Schema, Or, And
from starlette import status

from apps.database import orm
from apps.shared_kernel.utils import now


## ==========================================================
#  권한이 있는 유저의 투두 관련 테스트
#  ==========================================================

def test_로그인유저_todo_생성하다(get_logined_client):
    # given
    client = get_logined_client.get("client")

    # when
    response = client.post(
        "todos/",
        json={
            "content": "new_todo",  
        },
        headers=get_logined_client["headers"]
    )
    assert response.status_code == 200

    # then
    schema = Schema({
        "id": int,
        "content": "new_todo",
        "completed": "N",
        "started_at": None,
        "ended_at": None,
        "deleted_at": None,
    })
    assert schema.is_valid(response.json())


def test_로그인유저_todo_완료하다(get_logined_client, test_db):
    # given
    client = get_logined_client.get("client")
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    UPDATED_COMPLETED = "Y"
    response = client.patch(
        "todos/" + str(todo.id),
        json={
            "content": todo.content,
            "completed": UPDATED_COMPLETED, 
            "started_at": todo.started_at, 
            "ended_at": todo.ended_at, 
        },
        headers=get_logined_client["headers"]
    )

    # then
    schema = Schema(
        {
            "id": todo.id,
            "content": todo.content,
            "completed": UPDATED_COMPLETED,
            "started_at": todo.started_at,
            "ended_at": todo.ended_at,
            "deleted_at": todo.deleted_at,
        }
    )

    assert response.status_code == 200
    assert schema.is_valid(response.json())


def test_로그인유저_todo_내용을_변경하다(get_logined_client, test_db):
    # given
    client = get_logined_client.get("client")
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    UPDATED_CONTENT = "UPDATED TODO"
    response = client.patch(
        "todos/" + str(todo.id),
        json={
            "content": UPDATED_CONTENT,
            "completed": todo.completed, 
            "started_at": todo.started_at, 
            "ended_at": todo.ended_at, 
        },
        headers=get_logined_client["headers"]
    )

    # then
    schema = Schema(
        {
            "id": todo.id,
            "content": UPDATED_CONTENT,
            "completed": todo.completed, 
            "started_at": todo.started_at,
            "ended_at": todo.ended_at,
            "deleted_at": todo.deleted_at,
        }
    )

    assert response.status_code == 200
    assert schema.is_valid(response.json())


def test_로그인유저_todo_시작시간을_설정한다(get_logined_client, test_db):
    # given
    client = get_logined_client.get("client")
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    UPDATED_TIME_NOW = now()
    response = client.patch(
        "todos/" + str(todo.id),
        json={
            "content": todo.content,
            "completed": todo.completed, 
            "started_at": UPDATED_TIME_NOW.strftime("%H:%M:%S"), 
            "ended_at": todo.ended_at, 
        },
        headers=get_logined_client["headers"]
    )

    # then
    schema = Schema(
        {
            "id": todo.id,
            "content": todo.content,
            "completed": todo.completed, 
            "started_at": UPDATED_TIME_NOW.isoformat()[:19],
            "ended_at": todo.ended_at,
            "deleted_at": todo.deleted_at,
        }
    )

    assert response.status_code == 200
    assert schema.is_valid(response.json())


def test_로그인유저_todo_끝시간을_설정한다(get_logined_client, test_db):
    # given
    client = get_logined_client.get("client")
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    UPDATED_TIME_NOW = now()
    response = client.patch(
        "todos/" + str(todo.id),
        json={
            "content": todo.content,
            "completed": todo.completed, 
            "started_at": todo.started_at, 
            "ended_at": UPDATED_TIME_NOW.strftime("%H:%M:%S"), 
            "deleted_at": todo.deleted_at,
        },
        headers=get_logined_client["headers"]
    )

    # then
    schema = Schema(
        {
            "id": todo.id,
            "content": todo.content,
            "completed": todo.completed, 
            "started_at": todo.started_at,
            "ended_at": UPDATED_TIME_NOW.isoformat()[:19],
            "deleted_at": todo.deleted_at,
        }
    )

    assert response.status_code == 200
    assert schema.is_valid(response.json())


def test_로그인유저_todo_제거한다(get_logined_client, test_db):
    # given
    client = get_logined_client.get("client")
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    UPDATED_TIME_NOW = now()
    response = client.delete(
        "todos/" + str(todo.id),
        headers=get_logined_client["headers"]
    )

    # then
    schema = Schema(
        {
            "id": todo.id,
            "content": todo.content,
            "completed": todo.completed, 
            "started_at": todo.started_at,
            "ended_at": todo.ended_at, 
            "deleted_at": UPDATED_TIME_NOW.isoformat()[:19],
        }
    )

    assert response.status_code == 200
    assert schema.is_valid(response.json())


## ==========================================================
#  권한이 없는 유저의 투두 관련 테스트
#  ==========================================================

def test_로그인하지_않고_todo_생성할_수_없다(client):
    # given
    req_data = {
        "content": "new_todo",  
    }

    # when
    response = client.post(
        "todos/",
        json=req_data,
    )

    # then
    schema = Schema({
        "detail": "Not authenticated",
    })

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert schema.is_valid(response.json())


def test_로그인하지_않고_todo_수정할_수_없다(client, test_db):
    # given
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()
    req_data = {
        "content": todo.content,
        "completed": "Y", 
        "started_at": todo.started_at, 
        "ended_at": todo.ended_at, 
    }

    # when
    response = client.patch(
        "todos/" + str(todo.id),
        json=req_data,
    )

    # then
    schema = Schema({
        "detail": "Not authenticated",
    })

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert schema.is_valid(response.json())


def test_로그인하지_않고_todo_제거할_수_없다(client, test_db):
    # given
    todo = orm.Todo(content="New", completed="N", user_id=1)
    test_db.add(todo)
    test_db.commit()

    # when
    response = client.delete(
        "todos/" + str(todo.id),
    )

    # then
    schema = Schema({
        "detail": "Not authenticated",
    })

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert schema.is_valid(response.json())
