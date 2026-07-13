# Create Database Connections

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL="sqlite:///./portfolio.db" 

# Connects the app to database
engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

SessionLocal=sessionmaker(
    autoflush=False,
    bind=engine
)

Base=declarative_base()