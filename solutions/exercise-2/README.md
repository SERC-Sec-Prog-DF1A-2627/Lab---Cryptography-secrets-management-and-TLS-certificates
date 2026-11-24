# Exercise 2 · Worked result and individual check

The [finished configuration](settings.py) uses `load_dotenv(env_file, override=False)` and returns `validate_key(os.environ.get("NOTES_KEY"))`. The first operation supplies missing settings. The second accepts a valid key or stops startup. A real key belongs outside the repository.

To run a completed version in a fresh starter, activate the environment, then run from the repository root:

```bash
cp solutions/exercise-1/note_crypto.py note_crypto.py
cp solutions/exercise-2/settings.py settings.py
python -m tools.make_env
python -m unittest -v checks.test_notes checks.test_config checks.test_app
python app.py --db instance/notes-2.sqlite3
```

| Case | Expected evidence | Explanation |
|---|---|---|
| Local key, well formed | `Configuration OK.`, exit 0 | The helper constructed a Fernet object. |
| Empty environment and empty configuration file | `Configuration error: NOTES_KEY is missing.`, exit 2 | Startup stops before serving requests. |
| Temporary `NOTES_KEY=short` plus valid file | `Configuration error: NOTES_KEY has an invalid format.`, exit 2 | An existing environment variable takes priority. Fernet rejects that value. |
| Restart with persistent key | A new sign-in code is issued. Alex can still read “Room C”. | The same key and database were used across both processes. |
| Git | `git check-ignore -v .env` names the `.gitignore` rule. | An ignored local file still needs appropriate file and account permissions. |

## Five-minute individual check

1. A reader of the backup sees note IDs, owners, sizes and tokens. The Fernet timestamp is visible. To read a body, the reader would need the matching symmetric key or access to a process that can use it.
2. A damaged token and a token made with another key both fail verification. Show a generic message for that row, withhold its contents and allow intact, authorised rows to display.
3. Generating a replacement on startup leaves earlier ciphertext tied to the old key. Stop on missing configuration, preserve the existing data and restore the correct key through a controlled process. A planned key rotation maintains access to old data until migration succeeds.
