from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (SQLite in this example)
DATABASE_URL = "sqlite:///./test.db"

# Create database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Metadata and Base class
metadata = MetaData()
Base = declarative_base()