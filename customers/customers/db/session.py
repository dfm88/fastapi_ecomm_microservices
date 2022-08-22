from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from customers.core.config import settings

# XXX session and engine
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
