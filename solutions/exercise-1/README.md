# Exercise 1 · Worked result

Compare your root `note_crypto.py` with the [completed functions](note_crypto.py). To use this checkpoint in a fresh starter, run these commands **from the repository root**:

```bash
cp solutions/exercise-1/note_crypto.py note_crypto.py
python -m unittest -v checks.test_notes
python app.py
```

The save path encodes a Python string as UTF-8, encrypts the resulting bytes and inserts the returned token as a SQLite BLOB. The read path obtains rows with `WHERE owner = ?`, verifies/decrypts each token and decodes verified bytes as UTF-8. `InvalidToken` reaches the route. Its handler substitutes a row-level message and the loop continues to the next record.

| Observation | Example evidence |
|---|---|
| Successful round trip | Alex saves “Café meeting in room B” and sees the same characters after a refresh. All four function checks pass. |
| Stored record | `owner=alex storage=blob` and a short token prefix. Someone reading the database can see row IDs, ownership and token lengths. Fernet also exposes a creation timestamp in the token. |
| Damaged copy | The checker reports `InvalidToken`. Alex sees “This note could not be verified.” for that row and can still read an intact note. We deliberately changed the copy while holding the key constant. |
| Different key | A correctly structured token encrypted under a different key also fails verification. The exception alone cannot identify the cause. |
| Other staff member | A fresh Sam account has an empty list. The SQL query takes its owner argument from the signed-in session. Possessing the application key would allow code to decrypt both accounts’ tokens. |

For a second independently runnable check of the routes, use `python -m unittest -v checks.test_app` after copying or completing the functions.
