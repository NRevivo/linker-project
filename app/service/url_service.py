"""Application service that coordinates URL shortening use cases."""

from app.domain.models import ShortUrl
from app.repository.base import UrlRepository
from app.service.code_generator.base import CodeGenerator


class UrlService:
    """Orchestrates the shorten / resolve use cases.

    Holds no infrastructure knowledge of its own — it composes a
    UrlRepository and a CodeGenerator (both injected) to fulfill
    business operations such as creating a short URL or resolving
    one back to its target.
    """

    def __init__(self, repository: UrlRepository, code_generator: CodeGenerator) -> None:
        """Wire the service with its required collaborators."""
        ...

    def shorten(self, target_url: str) -> ShortUrl:
        """Generate a unique short code for ``target_url`` and persist the mapping."""
        ...

    def resolve(self, short_code: str) -> ShortUrl:
        """Return the ShortUrl identified by ``short_code`` or raise NotFoundError."""
        ...
