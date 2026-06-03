from typing import Protocol


class CodeGenerator(Protocol):
    """Strategy for generating short codes.

    Implementations decide the algorithm (random, base62, hash-based, etc.).
    The service depends on this abstraction, never on a concrete generator.
    """

    def generate(self) -> str:
        """Return a newly generated short code."""
        ...