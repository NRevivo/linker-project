"""Domain-level error hierarchy for LinkForge.

These exceptions describe failure modes in business terms and are
intentionally free of HTTP or persistence specifics. The API layer
translates them into HTTP responses; the repository layer raises
RepositoryError for infrastructure problems.
"""


class DomainError(Exception):
    """Base class for all LinkForge domain errors."""


class ValidationError(DomainError):
    """Raised when input data fails domain validation rules."""


class NotFoundError(DomainError):
    """Raised when a requested short URL does not exist."""


class CollisionError(DomainError):
    """Raised when a freshly generated short code collides with an existing one."""


class RepositoryError(DomainError):
    """Raised when the persistence layer fails for infrastructure reasons."""
