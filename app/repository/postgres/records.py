"""SQLAlchemy ORM mappings for the postgres repository."""


class UrlRecord:
    """ORM row representing a stored short URL mapping.

    Mirrors the ShortUrl domain entity at the persistence boundary;
    the repository is responsible for translating between this row
    type and the domain model.
    """

    ...
