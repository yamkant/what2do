from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    MetaData,
    Table,
)
from sqlalchemy.orm import (
    relationship,
    registry,
)

metadata = MetaData()
mapper_registry = registry()

user_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String),
    Column("is_active", Boolean, default=True),
)

item_table = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("title", String, index=True),
    Column("description", String, index=True),
    Column("owner_id", Integer, ForeignKey("users.id")),
)

def init_orm_mappers():
    from apps.account.domain.entity.user import User as UserEntity

    mapper_registry.map_imperatively(
        UserEntity,
        user_table,
    )
