from dataclasses import dataclass

from sqlalchemy.orm import DeclarativeBase


@dataclass
class Entry(DeclarativeBase):
    pass
