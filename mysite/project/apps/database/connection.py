from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apps.shared_kernel.config import config

if config.READER_DB_URL.startswith("sqlite"):
    engine = create_engine(
        config.READER_DB_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(config.READER_DB_URL)

SessionFactory = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

@contextmanager
def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()