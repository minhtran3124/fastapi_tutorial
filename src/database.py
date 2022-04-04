from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

SQLALCHEMY_DATABASE_URL = settings.db_url

# Reading more about create engine at here
#https://docs.sqlalchemy.org/en/14/core/engines.html
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args={'check_same_thread': False}
)

# https://docs.sqlalchemy.org/en/14/orm/session.html
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# https://docs.sqlalchemy.org/en/14/orm/declarative_tables.html
Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
