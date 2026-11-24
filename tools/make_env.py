"""Create one private development key, preserving any existing .env."""
import os
from pathlib import Path

from cryptography.fernet import Fernet


def main() -> None:
    path = Path(__file__).resolve().parents[1] / ".env"
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        print("Keeping the existing .env. No new key was generated.")
        return
    with os.fdopen(fd, "w", encoding="ascii") as stream:
        key = Fernet.generate_key().decode("ascii")
        stream.write(f"NOTES_KEY={key}\n")
    print("Created .env with a new local NOTES_KEY.")


if __name__ == "__main__":
    main()
