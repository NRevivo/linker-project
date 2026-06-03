from typing import Optional, Protocol

from app.domain.models import ShortUrl


class UrlRepository(Protocol):
    """Persistence contract for short URLs.

    Implementations may use Postgres, MongoDB, in-memory storage, etc.
    The service depends only on this abstraction.
    """

    def save(self, short_url: ShortUrl) -> ShortUrl:
        """Persist a short URL and return the saved entity."""
        ...

    def get(self, short_code: str) -> Optional[ShortUrl]:
        """Retrieve a short URL by its code, or None if not found."""
        ...

    def exists(self, short_code: str) -> bool:
        """Return True if a short URL with this code already exists."""
        ...