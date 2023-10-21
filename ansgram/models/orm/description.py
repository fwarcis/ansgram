from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Entry


class Description(Entry):
    __tablename__ = "descriptions"

    entry_id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(256))
    proofs: Mapped[str]

    user_entry_id: Mapped[int] = mapped_column(ForeignKey("users.entry_id"))
    user: Mapped["User"] = relationship(back_populates="description")  # type: ignore[name-defined] # noqa: F821
