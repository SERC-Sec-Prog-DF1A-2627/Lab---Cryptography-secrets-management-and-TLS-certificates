"""Run from the repository root with python app.py."""
import argparse
import secrets
import sys
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from flask import Flask, redirect, render_template, request, session, url_for

import storage
from access import new_codes, register_access
from note_crypto import decrypt_note, encrypt_note
from settings import DEFAULT_ENV, ConfigurationError, build_cipher

UNREADABLE = "This note could not be verified."


def create_app(db_path: Path, cipher: Fernet, codes: dict[str, str]) -> Flask:
    app = Flask(__name__)
    # A separate, per-run session signing key. Restarting requires signing in again.
    app.config.update(SECRET_KEY=secrets.token_bytes(32), SESSION_COOKIE_SAMESITE="Lax",
                      MAX_CONTENT_LENGTH=16_384)
    register_access(app, codes)
    storage.initialise(db_path)

    @app.route("/", methods=["GET", "POST"])
    def notes():
        owner = session.get("staff")
        if owner is None:
            return redirect(url_for("login"))

        if request.method == "POST":
            body = request.form.get("body", "").strip()
            if not 1 <= len(body) <= 500:
                return "Enter between 1 and 500 characters.", 400
            token = encrypt_note(body, cipher)
            storage.add_note(db_path, owner, token)
            return redirect(url_for("notes"))

        visible_notes = []
        # Restrict the query to this staff member BEFORE decrypting any row.
        for note_id, token in storage.owned_notes(db_path, owner):
            try:
                text = decrypt_note(token, cipher)
            except InvalidToken:
                text = UNREADABLE
            visible_notes.append((note_id, text))
        return render_template("notes.html", owner=owner, notes=visible_notes)

    @app.errorhandler(NotImplementedError)
    def unfinished_exercise(error):
        return "Exercise 1: finish the two functions in note_crypto.py, then restart.", 503

    return app


def main() -> int:
    parser = argparse.ArgumentParser(description="College Secure Notes classroom server")
    parser.add_argument("--db", type=Path, default=storage.DEFAULT_DB)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV)
    parser.add_argument("--check-config", action="store_true")
    args = parser.parse_args()
    try:
        cipher = build_cipher(args.env_file)
    except ConfigurationError as error:
        print(f"Configuration error: {error}", file=sys.stderr)
        return 2
    if args.check_config:
        print("Configuration OK.")
        return 0
    codes = new_codes()
    app = create_app(args.db, cipher, codes)
    print("Temporary staff sign-in codes for this private lab terminal:", flush=True)
    for staff, code in codes.items():
        print(f"  {staff}: {code}", flush=True)
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
