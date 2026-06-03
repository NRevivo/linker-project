from datetime import datetime

from pydantic import BaseModel, HttpUrl


class CreateUrlRequest(BaseModel):
    """Incoming payload for POST /shorten."""

    original_url: HttpUrl


class UrlResponse(BaseModel):
    """Outgoing payload representing a stored short URL."""

    short_code: str
    original_url: str
    short_url: str
    created_at: datetime