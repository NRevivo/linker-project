"""Structural interface for short-code generators."""

from typing import Protocol


class CodeGenerator(Protocol):
    """Port describing any strategy that can produce a short URL code.

    Implementations may be random, hash-based, sequential, etc. The
    service depends only on this protocol so generation strategies
    remain interchangeable.
    """

    def generate(self, length: int) -> str:
        """Return a freshly produced short code of the requested length."""
        ...
