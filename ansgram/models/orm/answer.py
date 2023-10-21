from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Entry


class Answer(Entry):
    __tablename__ = "answers"

    entry_id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(2048))
    explanation: Mapped[str] = mapped_column(String(1024))

    user_entry_id: Mapped[int] = mapped_column(ForeignKey("users.entry_id"))
    user: Mapped["User"] = relationship(back_populates="answers")  # type: ignore[name-defined] # noqa: F821

    question_entry_id: Mapped[int] = mapped_column(ForeignKey("questions.entry_id"))
    question: Mapped["Question"] = relationship(back_populates="answers")  # type: ignore[name-defined] # noqa: F821
