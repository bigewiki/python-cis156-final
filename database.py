from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database location
SQLALCHEMY_DATABASE_URL = "sqlite:///./wishlist.db"

# Set up SQLAlchemy engine
engine = create_engine(
    # more than one thread can interact with the database during the same request
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# We will later inherit the Base class to create the ORM models
Base = declarative_base()