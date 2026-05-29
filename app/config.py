"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Runtime configuration for LinkForge.

    Values are populated from environment variables (and an optional
    ``.env`` file) by pydantic-settings.
    """

    database_url: str
    base_url: str
    code_length: int
    max_retries: int
    log_level: str


def get_settings() -> Settings:
    """Return the application Settings singleton."""
    ...
