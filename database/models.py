from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import ForeignKey, String
from datetime import date
import uuid

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "Users"
    user_id: Mapped[str] = mapped_column(primary_key=True, default =lambda: str(uuid.uuid4()))
    email: Mapped[str]
    username: Mapped[str]
    password: Mapped[str]
    
    tasks: Mapped[list["Tasks"]] = relationship(back_populates="user")

  
    
class Tasks(Base):
    __tablename__ = "Tasks"
    id: Mapped[str] = mapped_column(primary_key=True, default = lambda: str(uuid.uuid4()))
    title: Mapped[str] = mapped_column(String(30))
    limited: Mapped[date]
    created: Mapped[date]
    done: Mapped[bool]
    user_id = mapped_column(ForeignKey("Users.user_id"))

    user: Mapped["Users"] = relationship(back_populates="tasks")

