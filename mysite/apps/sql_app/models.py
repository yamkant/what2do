from sqlalchemy import (
    MetaData,
    Table,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from apps.sql_app.database import Base

# metadata_obj = MetaData()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# user_table = Table(
#     "users",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, index=True, autoincrement=True),
#     Column("email", String, unique=True, index=True),
#     Column("hashed_password", String),
#     Column("is_active", Boolean, default=True),
# )

# item_table = Table(
#     "items",
#     metadata_obj,
#     Column("id", Integer, primary_key=True, index=True, autoincrement=True),
#     Column("title", String, index=True),
#     Column("description", String, index=True),
#     Column("owner_id", Integer, ForeignKey("users.id")),
# )