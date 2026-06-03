from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables.

    Values can be overridden via environment variables or a .env file
    in the project root. Variable names are case-insensitive.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Database
    database_url: str = "postgresql+psycopg://linkforge:linkforge@localhost:5432/linkforge"

    # Application
    base_url: str = "http://localhost:8000"

    # Short code generation
    code_length: int = 7
    max_retries: int = 5

    # Logging
    log_level: str = "INFO"

    # CORS
    cors_allow_origins: list[str] = ["http://localhost:5173", "http://localhost:5174"]


settings = Settings()