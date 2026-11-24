"""Exercise 1 end-to-end checks with Flask's test client and a temporary database."""
import tempfile
import unittest
from pathlib import Path

from cryptography.fernet import Fernet

import storage
from app import UNREADABLE, create_app
from tools.tamper_sample import change_ciphertext


class AppChecks(unittest.TestCase):
    def setUp(self):
        directory = self.enterContext(tempfile.TemporaryDirectory())
        self.db_path = Path(directory) / "practice.sqlite3"
        self.cipher = Fernet(Fernet.generate_key())
        self.codes = {"alex": "fictional-alex-code", "sam": "fictional-sam-code"}
        app = create_app(self.db_path, self.cipher, self.codes)
        app.config["TESTING"] = True
        self.client = app.test_client()

    def form(self, url, **fields):
        with self.client.session_transaction() as session:
            csrf = session["csrf"]
        return self.client.post(url, data={**fields, "csrf": csrf}, follow_redirects=True)

    def sign_in(self, staff):
        self.client.get("/login")
        return self.form("/login", staff=staff, code=self.codes[staff])

    def test_login_required(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith("/login"))

    def test_storage_and_staff_visibility(self):
        self.sign_in("alex")
        text = "Café meeting in room B"
        page = self.form("/", body=text)
        self.assertIn(text, page.get_data(as_text=True))
        _, token = storage.owned_notes(self.db_path, "alex")[0]
        self.assertIsInstance(token, bytes)
        self.assertEqual(self.cipher.decrypt(token).decode("utf-8"), text)
        self.form("/logout")
        sams_page = self.sign_in("sam").get_data(as_text=True)
        self.assertNotIn(text, sams_page)
        self.assertIn("You have no notes yet.", sams_page)

    def test_damaged_row_does_not_hide_a_valid_row(self):
        self.sign_in("alex")
        token = self.cipher.encrypt(b"Disposable record")
        storage.add_note(self.db_path, "alex", change_ciphertext(token))
        page = self.form("/", body="Intact record").get_data(as_text=True)
        self.assertIn(UNREADABLE, page)
        self.assertIn("Intact record", page)
        self.assertNotIn("Disposable record", page)
