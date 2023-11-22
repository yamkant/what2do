from sqlalchemy.orm import Session

from apps.database import orm

from apps.shared_kernel.repository import RDBRepository

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRDBRepository(RDBRepository):
    @staticmethod
    def get_todo_by_todo_id(session, todo_id: int) -> orm.Todo:
        todo = session.query(orm.Todo).filter(
            orm.Todo.id == todo_id, orm.Todo.deleted_at == None
        ).first()
        return todo

    @staticmethod
    def get_user_by_email(session: Session, email: str):
        user = session.query(orm.User).filter(
            orm.User.email == email
        ).first()
        return user


def get_user_by_email(db: Session, email: str):
    with db as session:
        user = session.query(orm.User).filter(orm.User.email == email).first()
    return user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(orm.User).offset(skip).limit(limit).all()
