#!/usr/bin/env python3
"""PassForge - A secure password generator with customizable options."""

import argparse
import secrets
import string
import sys


def generate_password(
    length: int = 16,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    exclude_chars: str = "",
    count: int = 1,
) -> list[str]:
    """Generate cryptographically secure passwords."""
    pool = ""
    required = []

    if uppercase:
        pool += string.ascii_uppercase
        required.append(secrets.choice(string.ascii_uppercase))
    if lowercase:
        pool += string.ascii_lowercase
        required.append(secrets.choice(string.ascii_lowercase))
    if digits:
        pool += string.digits
        required.append(secrets.choice(string.digits))
    if symbols:
        pool += "!@#$%^&*()-_=+[]{}|;:,.<>?"
        required.append(secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    if exclude_chars:
        pool = "".join(c for c in pool if c not in exclude_chars)

    if not pool:
        print("Error: No character types selected.", file=sys.stderr)
        sys.exit(1)

    if length < len(required):
        print(
            f"Error: Length too short. Minimum length is {len(required)}.",
            file=sys.stderr,
        )
        sys.exit(1)

    passwords = []
    for _ in range(count):
        remaining = length - len(required)
        password_chars = required + [secrets.choice(pool) for _ in range(remaining)]
        secrets.SystemRandom().shuffle(password_chars)
        passwords.append("".join(password_chars))

    return passwords


def main():
    parser = argparse.ArgumentParser(
        description="PassForge - Generate secure passwords",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  passforge                    # 16-char password with all char types
  passforge -l 32 -c 5         # Five 32-character passwords
  passforge --no-symbols -l 20 # 20-char, no symbols
  passforge --exclude "O0Il1"  # Exclude ambiguous characters""",
    )
    parser.add_argument(
        "-l", "--length", type=int, default=16, help="Password length (default: 16)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords (default: 1)"
    )
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument(
        "--exclude", type=str, default="", help="Exclude specific characters"
    )

    args = parser.parse_args()

    passwords = generate_password(
        length=args.length,
        uppercase=not args.no_upper,
        lowercase=not args.no_lower,
        digits=not args.no_digits,
        symbols=not args.no_symbols,
        exclude_chars=args.exclude,
        count=args.count,
    )

    for i, pwd in enumerate(passwords, 1):
        if args.count > 1:
            print(f"{i}. {pwd}")
        else:
            print(pwd)


if __name__ == "__main__":
    main()
