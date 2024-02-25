from __future__ import annotations
from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date, Time
from sqlalchemy.orm import Mapped, mapped_column
from base import Base
from flask_login import UserMixin


class User(Base, UserMixin):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(primary_key=True)
    nickname: Mapped[Optional[str]] = mapped_column()
    email: Mapped[Optional[str]] = mapped_column()
    password: Mapped[Optional[str]] = mapped_column()

    def __str__(self):
        return self.nickname.capitalize()

    def __repr__(self):
        return f"User: {self.nickname}"
