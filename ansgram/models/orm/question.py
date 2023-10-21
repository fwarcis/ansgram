from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Subjects
from .answer import Answer
from .base import Entry


class Question(Entry):
    __tablename__ = "questions"

    entry_id: Mapped[int] = mapped_column(primary_key=True)
    header: Mapped[str] = mapped_column(String(102))
    text: Mapped[str] = mapped_column(String(1024))
    subject: Mapped[Subjects]
    answers: Mapped[list[Answer] | None] = relationship(back_populates="question")

    user_entry_id: Mapped[int] = mapped_column(ForeignKey("users.entry_id"))
    user: Mapped["User"] = relationship(back_populates="questions")  # type: ignore[name-defined] # noqa: F821
