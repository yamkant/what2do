from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, MetaData, Table, DateTime
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

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
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")
