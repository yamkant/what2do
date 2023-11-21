from sqlalchemy.orm import Session

from apps.database import orm
from apps.user import schema
from apps.shared_kernel.utils import now

def get_todo_list(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    user: schema.User = None,
):
    _todo_list = db.query(orm.Todo).filter(
        orm.Todo.deleted_at == None, orm.Todo.owner_id==user.id
    ).offset(skip).limit(limit)
    return _todo_list


def create_todo(
    db: Session,
    todo: schema.TodoSchema,
    user: schema.User = None,
):
    new_todo = orm.Todo(content=todo.content, completed="N", owner_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(
    db: Session,
    todo_id: int,
    todo_data: schema.TodoSchema,
    user: schema.User = None,
):
    todo = db.query(orm.Todo).filter(
        orm.Todo.id == todo_id, orm.Todo.deleted_at == None, orm.Todo.owner_id==user.id
    ).first()
    todo.completed = todo_data.completed
    db.commit()
    return todo


def remove_todo(
    db: Session,
    todo_id: int,
    user: schema.User = None,
):
    todo = db.query(orm.Todo).filter(
        orm.Todo.id == todo_id, orm.Todo.deleted_at == None, orm.Todo.owner_id==user.id
    ).first()
    todo.deleted_at = now()
    db.commit()
    return todo