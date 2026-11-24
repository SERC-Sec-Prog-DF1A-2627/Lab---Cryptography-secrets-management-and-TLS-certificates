import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from cryptography.fernet import Fernet

from settings import ConfigurationError, build_cipher


class ConfigChecks(unittest.TestCase):
    def setUp(self):
        self.enterContext(patch.dict(os.environ, {}, clear=True))
        folder = self.enterContext(tempfile.TemporaryDirectory())
        self.env_file = Path(folder) / ".env"

    def test_missing_key_stops_startup(self):
        with self.assertRaisesRegex(ConfigurationError, "missing"):
            build_cipher(self.env_file)

    def test_malformed_key_stops_startup(self):
        os.environ["NOTES_KEY"] = "short"
        with self.assertRaisesRegex(ConfigurationError, "invalid format"):
            build_cipher(self.env_file)

    def test_dotenv_supplies_the_key(self):
        key = Fernet.generate_key()
        self.env_file.write_text("NOTES_KEY=" + key.decode("ascii"), encoding="ascii")
        cipher = build_cipher(self.env_file)
        self.assertEqual(cipher.decrypt(Fernet(key).encrypt(b"test")), b"test")

    def test_process_environment_has_priority(self):
        key = Fernet.generate_key()
        os.environ["NOTES_KEY"] = key.decode("ascii")
        self.env_file.write_text("NOTES_KEY=short", encoding="ascii")
        cipher = build_cipher(self.env_file)
        self.assertEqual(cipher.decrypt(Fernet(key).encrypt(b"test")), b"test")
