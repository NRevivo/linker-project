"""Pydantic request/response schemas exposed by the HTTP API."""

from pydantic import BaseModel


class CreateUrlRequest(BaseModel):
    """Payload submitted to POST /shorten describing the URL to shorten."""

    target_url: str


class UrlResponse(BaseModel):
    """Response body returned after creating or resolving a short URL."""

    short_code: str
    short_url: str
    target_url: str
