from password_generator.cli import main
import sys


def test_cli_default_length(monkeypatch, capsys):
    """
    Test CLI with default password length.
    """

    monkeypatch.setattr(
        sys,
        "argv",
        ["cli"]
    )

    main()

    captured = capsys.readouterr()

    assert "Generated password:" in captured.out


def test_cli_custom_length(monkeypatch, capsys):
    """
    Test CLI with custom password length.
    """

    monkeypatch.setattr(
        sys,
        "argv",
        ["cli", "--length", "20"]
    )

    main()

    captured = capsys.readouterr()

    password = captured.out.splitlines()[1]

    assert len(password) == 20