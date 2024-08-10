from sqlalchemy import String, Boolean, create_engine, DateTime, select

from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from datetime import datetime

from pathlib import Path

ROOT_DIR = Path(__file__).parent

# -----> Data Base Setting
# DB_PATH = ROOT_DIR / "db" / "database.db"
DEBUG = True


# Define the path to your database
ROOT_DIR = Path(__file__).parent
# DB_DIR = ROOT_DIR / "db"
DB_PATH = ROOT_DIR / "db" / "database.db"


engine = create_engine(f"sqlite:///{DB_PATH}", echo=DEBUG)


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "TodoList"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[bool] = mapped_column(Boolean)
    name: Mapped[str] = mapped_column(String(40))
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    def __reper__(self):
        return f"Todo(id={self.id}, name={self.name}, date={self.date}, status={self.status}, description={self.description})"


def get_all_users() -> list[Todo]:
    with Session(engine) as session:
        data = session.query(Todo).all()
        return data
    

def add_todo(name: str, description: str = None, status: bool = False):
    with Session(engine) as session:
        new_todo = Todo(name=name, description=description, status=status)
        session.add(new_todo)
        session.commit()


def update_todo(
    todo_id: int, name: str = None, description: str = None, status: bool = None
):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return None

        # Update fields only if new values are provided
        if name is not None:
            todo.name = name
        if description is not None:
            todo.description = description
        if status is not None:
            todo.status = status

        # Commit the changes to the database
        session.commit()
        return todo


def delete_todo(todo_id: int):
    with Session(engine) as session:
        
        todo = session.get(Todo, todo_id)

        session.delete(todo)
        session.commit()


def select_todo(name: str = "", description: str = "", status: bool = None, id: int = -1):
    with Session(engine) as session:
        if id > -1:
            # Select a specific todo by ID
            return session.execute(select(Todo).where(Todo.id == id)).scalars().first()
        else:
            # Build a list of filtering conditions
            args = []
            if name:
                args.append(Todo.name.like(f"%{name}%"))
            if description:
                args.append(Todo.description.like(f"%{description}%"))
            if status is not None:
                args.append(Todo.status == status)
            
            # Execute the query with all provided conditions
            return session.execute(select(Todo).where(*args)).scalars().all()
        
Base.metadata.create_all(bind=engine)
