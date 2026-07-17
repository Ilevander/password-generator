from password_generator.validator import validate_password


def test_valid_password():
    password = "Password123"

    assert validate_password(password) is True


def test_password_without_digit():
    password = "Password"

    assert validate_password(password) is False


def test_password_without_uppercase():
    password = "password123"

    assert validate_password(password) is False


def test_short_password():
    password = "Pa123"

    assert validate_password(password) is False