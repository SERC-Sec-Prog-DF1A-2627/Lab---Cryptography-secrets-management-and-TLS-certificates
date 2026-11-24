"""Completed Exercise 1 functions. SQLite stores the returned bytes directly."""
from cryptography.fernet import Fernet


def encrypt_note(text: str, cipher: Fernet) -> bytes:
    plaintext = text.encode("utf-8")
    return cipher.encrypt(plaintext)


def decrypt_note(token: bytes, cipher: Fernet) -> str:
    plaintext = cipher.decrypt(token)
    return plaintext.decode("utf-8")
