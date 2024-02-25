from __future__ import annotations
from typing import List, Optional
from sqlalchemy import ForeignKey, Column, String, Date, Time
from sqlalchemy.orm import Mapped, mapped_column,relationship
from base import Base
from user import User


class Event(Base):
    tablename = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    date = Column("Date", Date)
    time = Column("Time", Time, nullable=True)
    header: Mapped[str] = mapped_column(String(80))
    describe: Mapped[str] = mapped_column(String(200), nullable=True)
    user: Mapped[User] = relationship(back_populates="events")# Встановлення зв'язку з користувачем

    def __str__(self):
        return self.header.capitalize()

    # Метод для представлення об'єкта у вигляді рядка з ім'ям класу
    def __repr__(self):
        return f"Event: {self.header}"

