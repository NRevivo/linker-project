import secrets
import string


class RandomCodeGenerator:
    """Generates short codes using cryptographically secure random characters.

    Codes are drawn from URL-safe alphanumeric characters.
    Collision handling is the service's responsibility, not the generator's.
    """

    _ALPHABET = string.ascii_letters + string.digits

    def __init__(self, length: int) -> None:
        self._length = length

    def generate(self) -> str:
        return "".join(secrets.choice(self._ALPHABET) for _ in range(self._length))