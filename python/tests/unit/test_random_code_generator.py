import string

from python.app.service.code_generator.random_generator import RandomCodeGenerator


def test_generate_returns_code_of_requested_length():
    generator = RandomCodeGenerator(length=7)

    code = generator.generate()

    assert len(code) == 7


def test_generate_uses_only_alphanumeric_characters():
    generator = RandomCodeGenerator(length=10)
    allowed = set(string.ascii_letters + string.digits)

    code = generator.generate()

    assert set(code).issubset(allowed)


def test_generate_produces_different_codes_on_successive_calls():
    generator = RandomCodeGenerator(length=8)

    codes = {generator.generate() for _ in range(100)}

    assert len(codes) > 90