"""Exercise 2. Move the source of the Fernet key into the environment."""
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
    # Public Exercise 1 fixture. Anyone with this repository knows this value.
    # Exercise 2 replaces this whole function body. Use only fictional notes.
    training_key = "MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY="
    return validate_key(training_key)
