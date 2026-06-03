
from dataclasses import dataclass
from datetime import datetime


@dataclass (frozen=True)
class ShortUrl:
    short_code: str
    original_url: str
    created_at: datetime
