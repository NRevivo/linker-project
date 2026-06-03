from typing import Optional

from app.domain.models import ShortUrl
from app.domain.errors import CollisionError


class InMemoryUrlRepository:
    """In-memory implementation of UrlRepository.

    Stores short URLs in a dictionary keyed by short_code.
    Used for stage 1 development and as a test double.
    Data is lost when the process terminates.
    """

    def __init__(self) -> None:
        self._store: dict[str, ShortUrl] = {}

    def save(self, short_url: ShortUrl) -> ShortUrl:
        if short_url.short_code in self._store:
            raise CollisionError(
                f"Short code '{short_url.short_code}' already exists"
            )
        self._store[short_url.short_code] = short_url
        return short_url

    def get(self, short_code: str) -> Optional[ShortUrl]:
        return self._store.get(short_code)

    def exists(self, short_code: str) -> bool:
        return short_code in self._store