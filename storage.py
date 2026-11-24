"""Provided SQLite scaffold. This layer accepts an encrypted token as bytes."""
import sqlite3
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_DB = ROOT / "instance" / "notes-1.sqlite3"


def initialise(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(path)) as db, db:
        db.execute("""CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY, owner TEXT NOT NULL, token BLOB NOT NULL
        )""")


def add_note(path: Path, owner: str, token: bytes) -> int:
    with closing(sqlite3.connect(path)) as db, db:
        row = db.execute("INSERT INTO notes (owner, token) VALUES (?, ?)", (owner, token))
        return row.lastrowid


def owned_notes(path: Path, owner: str) -> list[tuple[int, bytes]]:
    with closing(sqlite3.connect(path)) as db:
        return db.execute(
            "SELECT id, token FROM notes WHERE owner = ? ORDER BY id", (owner,)
        ).fetchall()
