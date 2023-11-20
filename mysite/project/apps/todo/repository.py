from sqlalchemy.orm import Session
from database import orm
from user import schema

def get_todo_list(
    db: Session,
    skip: int = 0,
    limit: int = 10,
):
    _todo_list = db.query(orm.Todo).offset(skip).limit(limit).all()
    return _todo_list


def create_todo(
    db: Session,
    todo: schema.TodoSchema
):
    new_todo = orm.Todo(content=todo.content, completed="N")
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(
    db: Session,
    todo_id: int,
    todo_data: schema.TodoSchema
):
    todo = db.query(orm.Todo).filter(orm.Todo.id == todo_id).first()
    todo.completed = todo_data.completed
    db.commit()
    return todo