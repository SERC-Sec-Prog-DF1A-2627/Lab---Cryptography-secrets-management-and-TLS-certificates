"""Read only the stored type, length and a short token prefix."""
import argparse
import sqlite3
from contextlib import closing
from pathlib import Path

from storage import DEFAULT_DB


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    path = parser.parse_args().db
    if not path.is_file():
        parser.exit(1, "Start the app with this database and save a practice note first.\n")
    uri = path.resolve().as_uri() + "?mode=ro"
    with closing(sqlite3.connect(uri, uri=True)) as db:
        rows = db.execute("""SELECT id, owner, typeof(token), length(token), substr(token,1,12)
                             FROM notes ORDER BY id""").fetchall()
    if not rows:
        print("No notes yet.")
    for note_id, owner, kind, size, first in rows:
        prefix = first.decode("ascii", errors="replace") if isinstance(first, bytes) else first
        print(f"id={note_id} owner={owner} storage={kind} bytes={size} prefix={prefix}...")


if __name__ == "__main__":
    main()
