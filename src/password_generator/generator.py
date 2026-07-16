import secrets
import string


def generate_password(
    length: int = 12,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generate a secure random password.

    Args:
        length: Password length.
        use_digits: Include numbers.
        use_symbols: Include special characters.

    Returns:
        A generated password.
    """

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password