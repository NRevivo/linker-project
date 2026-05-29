"""SQLAlchemy-backed implementation of UrlRepository."""

from app.domain.models import ShortUrl


class PostgresRepository:
    """Persists ShortUrl entities in PostgreSQL via SQLAlchemy.

    Translates between the domain ShortUrl model and the UrlRecord
    ORM row. Satisfies the UrlRepository protocol structurally.
    """

    def __init__(self, session: object) -> None:
        """Wire the repository with a SQLAlchemy session/sessionmaker."""
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
