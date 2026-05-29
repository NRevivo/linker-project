"""Structural interface for short URL repositories."""

from typing import Protocol

from app.domain.models import ShortUrl


class UrlRepository(Protocol):
    """Port describing persistence operations for ShortUrl entities.

    Implementations may be in-memory, SQL-backed, or remote; the
    service depends only on this protocol.
    """

    def save(self, short_url: ShortUrl) -> None:
        """Persist a ShortUrl, raising CollisionError on duplicate code."""
        ...

    def get(self, short_code: str) -> ShortUrl:
        """Return the ShortUrl for ``short_code`` or raise NotFoundError."""
        ...

    def exists(self, short_code: str) -> bool:
        """Return True if a ShortUrl with ``short_code`` is stored."""
        ...
