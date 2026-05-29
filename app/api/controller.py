"""FastAPI routes for the LinkForge HTTP API."""

from fastapi import APIRouter

from app.api.schemas import CreateUrlRequest, UrlResponse

router = APIRouter()


@router.post("/shorten", response_model=UrlResponse)
def shorten_url(payload: CreateUrlRequest) -> UrlResponse:
    """Create a new short URL for the supplied target."""
    ...


@router.get("/{short_id}")
def resolve_url(short_id: str) -> UrlResponse:
    """Resolve ``short_id`` to its original target URL."""
    ...
