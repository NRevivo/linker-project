from functools import lru_cache

from fastapi import Depends

from app.repository.base import UrlRepository
from app.repository.in_memory import InMemoryUrlRepository
from app.service.code_generator.base import CodeGenerator
from app.service.code_generator.random_generator import RandomCodeGenerator
from app.service.url_service import UrlService


@lru_cache
def get_repository() -> UrlRepository:
    """Provide a singleton UrlRepository instance.

    Currently returns an in-memory implementation. Swap this line
    to switch persistence backends.
    """
    return InMemoryUrlRepository()


@lru_cache
def get_code_generator() -> CodeGenerator:
    """Provide a singleton CodeGenerator instance."""
    return RandomCodeGenerator(length=7)


def get_url_service(
    repository: UrlRepository = Depends(get_repository),
    code_generator: CodeGenerator = Depends(get_code_generator),
) -> UrlService:
    """Wire the UrlService with its dependencies."""
    return UrlService(repository=repository, code_generator=code_generator)