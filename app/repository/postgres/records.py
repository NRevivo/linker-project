from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models."""


class UrlRecord(Base):
    """ORM model representing a row in the urls table.

    This is an infrastructure concern. The service layer must never
    see this class — it lives behind the PostgresUrlRepository.
    """

    __tablename__ = "urls"

    short_code: Mapped[str] = mapped_column(String(32), primary_key=True)
    original_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)