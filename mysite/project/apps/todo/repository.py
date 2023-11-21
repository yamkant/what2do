from sqlalchemy.orm import Session
from datetime import datetime, time

from apps.database import orm
from apps.user import schema as user_schema
from apps.todo import schema as todo_schema
from apps.shared_kernel.utils import now

def get_todo_list(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    user: user_schema.User = None,
):
    _todo_list = db.query(orm.Todo).filter(
        orm.Todo.deleted_at == None, orm.Todo.user_id==user.id
    ).offset(skip).limit(limit)
    return _todo_list

def get_todo(
    db: Session,
    todo_id: int,
    user_id: int,
):
    todo = db.query(orm.Todo).filter(
        orm.Todo.id == todo_id, orm.Todo.deleted_at == None, orm.Todo.user_id==user_id
    ).first()
    return todo

def create_todo(
    db: Session,
    todo: user_schema.TodoSchema,
    user: user_schema.User = None,
):
    new_todo = orm.Todo(content=todo.content, completed="N", user_id=user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(
    db: Session,
    todo_id: int,
    request: todo_schema.UpdateTodoRequest,
    user: user_schema.User = None,
):
    todo = get_todo(db=db, todo_id=todo_id, user_id=user.id)

    update_data = request.dict(exclude_unset=True)
    for key, value in update_data.items():
        if isinstance(value, time):
            value = datetime.combine(datetime.today().date(), value)
        setattr(todo, key, value)
    
    db.commit()
    db.refresh(todo)
    return todo


def remove_todo(
    db: Session,
    todo_id: int,
    user: user_schema.User = None,
):
    todo = get_todo(db=db, todo_id=todo_id, user_id=user.id)
    todo.deleted_at = now()
    db.commit()
    return todo