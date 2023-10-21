from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import Subjects
from .base import Entry


class Subject(Entry):
    __tablename__ = "subjects"

    entry_id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[Subjects]
    can_help: Mapped[bool] = mapped_column(default=False)
    has_question: Mapped[bool] = mapped_column(default=False)

    user_entry_id: Mapped[int] = mapped_column(ForeignKey("users.entry_id"))
    user: Mapped["User"] = relationship(back_populates="subjects")  # type: ignore[name-defined] # noqa: F821
