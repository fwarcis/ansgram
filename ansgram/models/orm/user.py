from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .answer import Answer
from .base import Entry
from .description import Description
from .question import Question
from .subject import Subject


class User(Entry):
    __tablename__ = "users"

    entry_id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int]
    is_admin: Mapped[bool]
    grade: Mapped[str]

    subjects: Mapped[list[Subject] | None] = relationship(back_populates="user")
    description: Mapped[Optional[Description]] = relationship(back_populates="user")
    questions: Mapped[list[Question] | None] = relationship(back_populates="user")
    answers: Mapped[list[Answer] | None] = relationship(back_populates="user")
