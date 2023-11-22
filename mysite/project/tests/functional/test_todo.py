from fastapi.testclient import TestClient
from project.apps.database import orm


def test_투두리스트_조회(authorized_client):
    # given
    user = authorized_client['user']
    new_todo = orm.Todo(content="New1", completed="N", user_id=user.id, deleted_at=None)
    authorized_client['session'].add(new_todo)
    authorized_client['session'].commit()

    # new_todo = orm.Todo(content="New2", completed="N", user_id=user.id)
    # test_session.add(new_todo)
    # test_session.commit()


    # when
    response = authorized_client["client"].get("/todos/")

    # then
    print(response)
    # assert response.json()[0]['content'] == new_todo.content
    # assert response.json()[0]['completed'] == new_todo.completed