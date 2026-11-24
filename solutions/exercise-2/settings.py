"""Completed Exercise 2 configuration. A bad key stops startup."""
import os
from pathlib import Path

from cryptography.fernet import Fernet
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
DEFAULT_ENV = ROOT / ".env"


class ConfigurationError(ValueError):
    """A safe message that the launcher can show without revealing a secret."""


def validate_key(value: str | None) -> Fernet:
    if not value:
        raise ConfigurationError("NOTES_KEY is missing.")
    try:
        return Fernet(value.encode("ascii"))
    except ValueError:
        raise ConfigurationError("NOTES_KEY has an invalid format.") from None


def build_cipher(env_file: Path = DEFAULT_ENV) -> Fernet:
    load_dotenv(env_file, override=False)
    return validate_key(os.environ.get("NOTES_KEY"))
