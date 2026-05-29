"""In-memory UrlRepository for stage 1 and unit tests."""

from app.domain.models import ShortUrl


class InMemoryUrlRepository:
    """Stores ShortUrl entities in a process-local dictionary.

    Suitable for early stages and tests; not durable across restarts.
    Satisfies the UrlRepository protocol structurally.
    """

    def __init__(self) -> None:
        """Initialize the backing store."""
        ...

    def save(self, short_url: ShortUrl) -> None:
        """Persist a ShortUrl, raising CollisionError on duplicate code."""
        ...

    def get(self, short_code: str) -> ShortUrl:
        """Return the ShortUrl for ``short_code`` or raise NotFoundError."""
        ...

    def exists(self, short_code: str) -> bool:
        """Return True if a ShortUrl with ``short_code`` is stored."""
        ...
