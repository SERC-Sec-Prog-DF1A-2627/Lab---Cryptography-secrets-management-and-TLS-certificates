"""Add one intentionally damaged, fictional sample row for Alex."""
import argparse
import base64
from pathlib import Path

from cryptography.fernet import InvalidToken

import storage
from note_crypto import decrypt_note, encrypt_note
from settings import build_cipher


def change_ciphertext(token: bytes) -> bytes:
    # Decode the outer Base64 so that the modified copy still has valid encoding.
    raw = bytearray(base64.urlsafe_b64decode(token))
    # Fernet starts with 1 version byte, 8 timestamp bytes, then a 16-byte IV.
    raw[25] ^= 1  # Change one bit of encrypted content and leave its tag unchanged.
    return base64.urlsafe_b64encode(raw)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=storage.DEFAULT_DB)
    path = parser.parse_args().db
    cipher = build_cipher()
    original = encrypt_note("Disposable practice note", cipher)
    print("Original:", decrypt_note(original, cipher))
    damaged = change_ciphertext(original)
    try:
        decrypt_note(damaged, cipher)
    except InvalidToken:
        print("Changed copy: rejected (InvalidToken).")
    else:
        parser.exit(1, "The verification check should have rejected the changed copy.\n")
    storage.initialise(path)
    row = storage.add_note(path, "alex", damaged)
    print(f"Added damaged sample as Alex's note {row}. Refresh Alex's page.")


if __name__ == "__main__":
    main()
