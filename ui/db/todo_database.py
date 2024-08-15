# from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, update, delete
# from sqlalchemy.orm import DeclarativeBase, Session
# from datetime import datetime

# # Updated declarative_base
# DATABASE_URL = "sqlite:///todo_database.db"


# engine = create_engine(DATABASE_URL, echo=True)

# class Base(DeclarativeBase):
#     pass

# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     description = Column(String)
#     status = Column(Boolean, default=False)
#     date_added = Column(DateTime, default=datetime.utcnow)


# def get_todo():
#     with Session(engine) as session:
#         todo = session.query(Todo).all()
#         return todo

# def add_todo(todo: Todo):
#     with Session(engine) as session:
#         try:
#             session.add(todo)
#             session.commit()
#         except Exception as e:
#             print(f"Error adding todo: {e}")
#             session.rollback()

# def update_todo(todo: Todo):
#     if not todo.id:
#         print(f"Error: todo.id is {todo.id}. Make sure the selected todo item has a valid ID.")
#         raise ValueError("Todo ID must be provided for updating.")

#     with Session(engine) as session:
#         session.execute(
#             update(Todo)
#             .where(Todo.id == todo.id)
#             .values(
#                 name=todo.name,
#                 description=todo.description,
#                 status=todo.status
#             )
#         )
#         session.commit()
            
# def delete_todo(id: int):
#     with Session(engine) as session:
#         session.execute(delete(Todo).where(Todo.id == id))
#         session.commit()


# # def slected_todo(self):
# #     with Session(engine) as session:



# # Set up the database

# Base.metadata.create_all(bind=engine)


# # engine = create_engine("sqlite:///ui/db/todo_database.db")
# # Base.metadata.create_all(engine)

# # # Set up sessionmaker
# # SessionLocal = sessionmaker(bind=engine)


# # # For create session
# # def get_session():
# #     return SessionLocal()





from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, update, delete
from sqlalchemy.orm import DeclarativeBase, Session
from datetime import datetime

# Database URL
DATABASE_URL = "sqlite:///ui/db/todo_database.db"

# Engine creation
engine = create_engine(DATABASE_URL, echo=True)

# Declarative Base
class Base(DeclarativeBase):
    pass

# Todo model
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(Boolean, default=False)
    date_added = Column(DateTime, default=datetime.utcnow)

# CRUD Operations

def get_todo():
    with Session(engine) as session:
        return session.query(Todo).all()

def add_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)


def update_todo(todo: Todo):
    with Session(engine) as session:
        session.execute(
            update(Todo)
            .where(Todo.id == todo.id)
            .values(
                {
                    "name": todo.name,
                    "description": todo.description,
                    "status": todo.status,
                }
            )
        )
        session.commit()

def delete_todo(id: int):
    with Session(engine) as session:
        session.execute(
            delete(Todo).where(Todo.id == id)
        )
        session.commit()

# Initialize the database
Base.metadata.create_all(bind=engine)
