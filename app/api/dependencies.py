"""FastAPI dependency-injection wiring for the API layer."""

from app.repository.base import UrlRepository
from app.service.code_generator.base import CodeGenerator
from app.service.url_service import UrlService


def get_repository() -> UrlRepository:
    """Provide a configured UrlRepository instance for request handlers."""
    ...


def get_code_generator() -> CodeGenerator:
    """Provide a configured CodeGenerator instance for request handlers."""
    ...


def get_url_service() -> UrlService:
    """Build a UrlService with the configured repository and generator."""
    ...
