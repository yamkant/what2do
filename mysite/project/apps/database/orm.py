from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, MetaData, Table, DateTime
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

from apps.todo.exception import TodoContentException

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    completed = Column(String)
    deleted_at = Column(DateTime(timezone=True), default=None, nullable=True)

    started_at = Column(DateTime(timezone=True), default=None, nullable=True)
    ended_at = Column(DateTime(timezone=True), default=None, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")

    @validates("content")
    def validate_content(self, key, content) -> str:
        if not content:
            raise TodoContentException()
        return content

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    body = Column(String)
    url = Column(String)

    published_at = Column(String)