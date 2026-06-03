import logging
from datetime import datetime, timezone

from app.domain.models import ShortUrl
from app.domain.errors import CollisionError, NotFoundError
from app.repository.base import UrlRepository
from app.service.code_generator.base import CodeGenerator


logger = logging.getLogger(__name__)


class UrlService:
    """Business logic for creating and resolving short URLs.

    Coordinates code generation and persistence. Depends only on
    abstractions (UrlRepository, CodeGenerator), never on concrete
    implementations.
    """

    def __init__(
        self,
        repository: UrlRepository,
        code_generator: CodeGenerator,
        max_retries: int = 5,
    ) -> None:
        self._repository = repository
        self._code_generator = code_generator
        self._max_retries = max_retries

    def create_short_url(self, original_url: str) -> ShortUrl:
        """Create a new short URL for the given original URL.

        Generates a short code and attempts to save it. On collision,
        retries with a new code up to max_retries times.
        """
        for attempt in range(1, self._max_retries + 1):
            short_code = self._code_generator.generate()
            short_url = ShortUrl(
                short_code=short_code,
                original_url=original_url,
                created_at=datetime.now(timezone.utc),
            )

            try:
                saved = self._repository.save(short_url)
                logger.info(
                    "Created short URL: %s -> %s", short_code, original_url
                )
                return saved
            except CollisionError:
                logger.debug(
                    "Short code collision on attempt %d: %s", attempt, short_code
                )
                continue

        raise CollisionError(
            f"Failed to generate a unique short code after {self._max_retries} attempts"
        )

    def get_original_url(self, short_code: str) -> ShortUrl:
        """Retrieve a short URL by its code.

        Raises NotFoundError if no URL with the given code exists.
        """
        short_url = self._repository.get(short_code)
        if short_url is None:
            raise NotFoundError(f"Short code '{short_code}' not found")
        return short_url