import pytest

from app.domain.errors import CollisionError, NotFoundError
from app.repository.in_memory import InMemoryUrlRepository
from app.service.code_generator.base import CodeGenerator
from app.service.url_service import UrlService


class FixedCodeGenerator:
    """Test double that returns a predetermined sequence of codes."""

    def __init__(self, codes: list[str]) -> None:
        self._codes = list(codes)
        self._index = 0

    def generate(self) -> str:
        code = self._codes[self._index]
        self._index += 1
        return code


def make_service(codes: list[str], max_retries: int = 5) -> UrlService:
    return UrlService(
        repository=InMemoryUrlRepository(),
        code_generator=FixedCodeGenerator(codes),
        max_retries=max_retries,
    )


def test_create_short_url_persists_and_returns_entity():
    service = make_service(codes=["abc123"])

    result = service.create_short_url("https://example.com")

    assert result.short_code == "abc123"
    assert result.original_url == "https://example.com"
    assert result.created_at is not None


def test_create_short_url_retries_on_collision():
    service = make_service(codes=["taken", "fresh"])
    service.create_short_url("https://first.com")  # occupies "taken"

    result = service.create_short_url("https://second.com")

    assert result.short_code == "fresh"


def test_create_short_url_raises_after_exhausting_retries():
    service = make_service(codes=["dup", "dup", "dup", "dup"], max_retries=3)
    service.create_short_url("https://first.com")  # occupies "dup"

    with pytest.raises(CollisionError):
        service.create_short_url("https://second.com")


def test_get_original_url_returns_saved_entity():
    service = make_service(codes=["abc"])
    service.create_short_url("https://example.com")

    result = service.get_original_url("abc")

    assert result.original_url == "https://example.com"


def test_get_original_url_raises_when_not_found():
    service = make_service(codes=["abc"])

    with pytest.raises(NotFoundError):
        service.get_original_url("nonexistent")