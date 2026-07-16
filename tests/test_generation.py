from password_generator.generator import generate_password


def test_password_length():
    password = generate_password(16)
    assert len(password) == 16


def test_password_is_string():
    password = generate_password()
    assert isinstance(password, str)




    