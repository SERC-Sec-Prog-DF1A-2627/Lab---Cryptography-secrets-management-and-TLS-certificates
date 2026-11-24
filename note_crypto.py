"""Exercise 1. The Flask routes call these two functions."""
from cryptography.fernet import Fernet


def encrypt_note(text: str, cipher: Fernet) -> bytes:
    """Turn the form's text into an authenticated token for SQLite."""
    raise NotImplementedError("Complete encrypt_note in Exercise 1.")


def decrypt_note(token: bytes, cipher: Fernet) -> str:
    """Return verified text for display. Let InvalidToken reach the caller."""
    raise NotImplementedError("Complete decrypt_note in Exercise 1.")
