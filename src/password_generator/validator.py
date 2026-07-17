def validate_password(password: str) -> bool:
    """
    Validate password strength.

    Rules:
    - Minimum 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    """

    if len(password) < 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    return has_digit and has_upper and has_lower