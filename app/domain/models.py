"""Pure-Python domain models for LinkForge.

This module must remain free of any infrastructure dependencies
(no FastAPI, SQLAlchemy, Pydantic, etc.).
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class ShortUrl:
    """Domain entity representing a shortened URL.

    Encapsulates the identity (short code) and the original target URL,
    along with creation metadata. Pure Python — no framework coupling.
    """

    short_code: str
    target_url: str
    created_at: datetime
