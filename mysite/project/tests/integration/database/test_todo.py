from apps.database import orm

TEST_DATABASE_URL = "sqlite:///./test.db"

def test_투두리스트_추가(test_session):
    # given
    new_todo = orm.Todo(content="New", completed="N")

    # when
    test_session.add(new_todo)
    test_session.commit()

    # then
    assert test_session.query(orm.Todo).filter(
        orm.Todo.id == 1
    ).first()