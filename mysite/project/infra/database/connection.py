from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

def get_engine():
    db_engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

    if not database_exists(db_engine.url):
        create_database(db_engine.url)

    return db_engine

engine = get_engine()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db_session():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()