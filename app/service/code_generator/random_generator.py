"""Random short-code generator implementation."""


class RandomCodeGenerator:
    """Produces short codes by sampling a URL-safe alphabet at random.

    Satisfies the CodeGenerator protocol structurally; no explicit
    inheritance is required.
    """

    def generate(self, length: int) -> str:
        """Return a random short code of the given ``length``."""
        ...
