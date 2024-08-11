from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Updated declarative_base
Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(Boolean, default=False)
    date_added = Column(DateTime, default=datetime.utcnow)


# Set up the database
engine = create_engine("sqlite:///ui/db/todo_database.db")
Base.metadata.create_all(engine)

# Set up sessionmaker
SessionLocal = sessionmaker(bind=engine)


# For create session
def get_session():
    return SessionLocal()
