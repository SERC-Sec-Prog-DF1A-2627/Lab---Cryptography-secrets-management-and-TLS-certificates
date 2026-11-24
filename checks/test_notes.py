import unittest

from cryptography.fernet import Fernet, InvalidToken

from note_crypto import decrypt_note, encrypt_note
from tools.tamper_sample import change_ciphertext


class NoteChecks(unittest.TestCase):
    def setUp(self):
        self.cipher = Fernet(Fernet.generate_key())

    def test_round_trip_preserves_unicode(self):
        text = "Café at 10 – room B"
        token = encrypt_note(text, self.cipher)
        self.assertIsInstance(token, bytes)
        self.assertNotEqual(token, text.encode("utf-8"))
        self.assertEqual(decrypt_note(token, self.cipher), text)

    def test_same_text_can_produce_different_tokens(self):
        first = encrypt_note("Practice", self.cipher)
        second = encrypt_note("Practice", self.cipher)
        self.assertNotEqual(first, second)

    def test_changed_token_is_rejected(self):
        token = encrypt_note("Practice", self.cipher)
        with self.assertRaises(InvalidToken):
            decrypt_note(change_ciphertext(token), self.cipher)

    def test_different_key_is_rejected(self):
        token = encrypt_note("Practice", self.cipher)
        other_cipher = Fernet(Fernet.generate_key())
        with self.assertRaises(InvalidToken):
            decrypt_note(token, other_cipher)
