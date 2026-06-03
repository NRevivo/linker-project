from functools import lru_cache
from typing import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.config import settings
from app.repository.base import UrlRepository
from app.repository.postgres import SessionLocal
from app.repository.postgres.repository import PostgresUrlRepository
from app.service.code_generator.base import CodeGenerator
from app.service.code_generator.random_generator import RandomCodeGenerator
from app.service.url_service import UrlService


def get_session() -> Generator[Session, None, None]:
    """Provide a database session for the duration of a request."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_repository(session: Session = Depends(get_session)) -> UrlRepository:
    """Provide a UrlRepository instance bound to the current session."""
    return PostgresUrlRepository(session=session)


@lru_cache
def get_code_generator() -> CodeGenerator:
    """Provide a singleton CodeGenerator instance."""
    return RandomCodeGenerator(length=settings.code_length)


def get_url_service(
    repository: UrlRepository = Depends(get_repository),
    code_generator: CodeGenerator = Depends(get_code_generator),
) -> UrlService:
    """Wire the UrlService with its dependencies."""
    return UrlService(
        repository=repository,
        code_generator=code_generator,
        max_retries=settings.max_retries,
    )