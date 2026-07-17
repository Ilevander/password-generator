import argparse

from password_generator.generator import generate_password


def main():
    parser = argparse.ArgumentParser(
        description="Generate a secure password"
    )

    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="Password length"
    )

    args = parser.parse_args()

    password = generate_password(
        length=args.length
    )

    print("Generated password:")
    print(password)


if __name__ == "__main__":
    main()