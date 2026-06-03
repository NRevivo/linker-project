import logging

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from app.api.dependencies import get_url_service
from app.api.schemas import CreateUrlRequest, UrlResponse
from app.domain.errors import CollisionError, NotFoundError
from app.service.url_service import UrlService
from app.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/shorten",
    response_model=UrlResponse,
    status_code=status.HTTP_201_CREATED,
)
def shorten(
    request: CreateUrlRequest,
    service: UrlService = Depends(get_url_service),
) -> UrlResponse:
    """Create a new short URL."""
    try:
        short_url = service.create_short_url(str(request.original_url))
    except CollisionError as e:
        logger.error("Failed to create short URL: %s", e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Could not generate a unique short code. Please try again.",
        )

    return UrlResponse(
        short_code=short_url.short_code,
        original_url=short_url.original_url,
        short_url=f"{settings.base_url}/{short_url.short_code}",
        created_at=short_url.created_at,
    )


@router.get("/{short_code}")
def redirect(
    short_code: str,
    service: UrlService = Depends(get_url_service),
) -> RedirectResponse:
    """Resolve a short code and redirect to the original URL."""
    try:
        short_url = service.get_original_url(short_code)
    except NotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Short code '{short_code}' not found",
        )

    return RedirectResponse(
        url=short_url.original_url,
        status_code=status.HTTP_302_FOUND,
    )