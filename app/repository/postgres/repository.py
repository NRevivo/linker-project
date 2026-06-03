from typing import Optional

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.domain.errors import CollisionError, RepositoryError
from app.domain.models import ShortUrl
from app.repository.postgres.records import UrlRecord


class PostgresUrlRepository:
    """Postgres-backed implementation of UrlRepository.

    Translates between the domain model (ShortUrl) and the ORM model
    (UrlRecord), and converts database errors into domain errors.
    """

    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, short_url: ShortUrl) -> ShortUrl:
        record = UrlRecord(
            short_code=short_url.short_code,
            original_url=short_url.original_url,
            created_at=short_url.created_at,
        )

        try:
            self._session.add(record)
            self._session.commit()
        except IntegrityError as e:
            self._session.rollback()
            raise CollisionError(
                f"Short code '{short_url.short_code}' already exists"
            ) from e
        except Exception as e:
            self._session.rollback()
            raise RepositoryError("Failed to save short URL") from e

        return short_url

    def get(self, short_code: str) -> Optional[ShortUrl]:
        try:
            stmt = select(UrlRecord).where(UrlRecord.short_code == short_code)
            record = self._session.execute(stmt).scalar_one_or_none()
        except Exception as e:
            raise RepositoryError("Failed to fetch short URL") from e

        if record is None:
            return None

        return self._to_domain(record)

    def exists(self, short_code: str) -> bool:
        try:
            stmt = select(UrlRecord.short_code).where(UrlRecord.short_code == short_code)
            result = self._session.execute(stmt).scalar_one_or_none()
        except Exception as e:
            raise RepositoryError("Failed to check existence") from e

        return result is not None

    @staticmethod
    def _to_domain(record: UrlRecord) -> ShortUrl:
        """Translate ORM model to domain model."""
        return ShortUrl(
            short_code=record.short_code,
            original_url=record.original_url,
            created_at=record.created_at,
        )