# College Secure Notes

**Week 10 · Block 1 · 120 minutes · Level 6 secure programming**

A member of college staff wants to save a fictional meeting note, read it later and keep it private from other staff. You will follow that note from the browser into a SQLite database, then examine how a browser decides whether to trust an HTTPS server. Use made-up notes such as **Café meeting in room B**.

## Your route through the block

| Minutes | Work | Evidence |
|---|---|---|
| 0–10 | Tutor introduction. For catch-up, read [the short introduction](exercises/00-introduction.md). | Name where a note is readable. |
| 10–25 | [Activity 1 · Choose a technique](worksheets/activity-1.md) | Five choices, each with a reason and an assumption. |
| 25–70 | [Exercise 1 · Encrypt and retrieve a note](exercises/01-encrypted-notes.md) | A round trip, a database observation, a changed token and an ownership check. |
| 70–95 | [Exercise 2 · Move the key out of source](exercises/02-environment.md) | Valid, missing and invalid key results and evidence that Git ignores the secret. |
| 95–100 | [Five-minute individual check](worksheets/evidence.md#five-minute-individual-check) | Three short explanations in your own words. |
| 100–120 | [Exercise 3 · TLS certificates and HTTPS](exercises/03-tls.md) | Certificate fields, two curl results and a deployment decision. |

Write individual observations in [your evidence sheet](worksheets/evidence.md). Each activity has a solo route. Exercise 2 includes an entry point if you missed Exercise 1. Exercise 3 only needs Python, OpenSSL and curl. The [solutions](solutions/README.md) give worked code, reasons and expected observations.

## Open your development environment

1. Accept your lecturer’s assignment link. Open your own repository, then use **Code → Codespaces → Create codespace** or the assignment’s Codespaces button. Wait for the development container to finish installing the requirements.
2. In the terminal at the repository root, run the commands below. Activate the virtual environment in **each new terminal** used for Flask. `pwd` should identify the folder containing `app.py`.
3. Keep port 5000 private. Open its **Ports** entry in a new browser tab when the instructions ask you to view Flask. For port 4443, use the terminal commands in Exercise 3.

```bash
source .venv/bin/activate
python --version
python -m pip show Flask cryptography python-dotenv
openssl version
curl --version
```

Expect Python 3.14.x, three package names and versions, OpenSSL 3.x and a curl version. If the environment setup is still running, open the creation log and wait for the install to finish. For a local Linux machine with Python 3.14, or to repair an incomplete install inside Codespaces, run:

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Where to work

| File or folder | Why you open it |
|---|---|
| `note_crypto.py` | Exercise 1. Write the two functions that turn text into an encrypted token and back. |
| `settings.py` | Exercise 2. Choose where Flask obtains the Fernet key at startup. |
| `app.py` | Read the provided route. GET displays notes. POST accepts form text, encrypts it and saves a row. |
| `storage.py` | See the parameterised SQL and the owner filter. SQLite stores the token as a BLOB (bytes). |
| `access.py` | Provided sign-in and form protection. The server assigns each signed-in session a staff name. |
| `templates/` | Jinja fills the form and note list with values supplied by the route. |
| `tools/` and `checks/` | Observe the database, create a local key and run built-in progress checks. |
| `tls/` | Standalone certificate generator and fixed-response HTTPS server. |
| `instance/`, `.env` and `.dev-tls/` | Local files created as you work. Git ignores them. |

Codespaces restarts end the temporary sign-ins. Practice databases and the local encryption key persist in the same workspace. A new Codespace needs its own key and fresh fictional data. Use the copyable commands in each guide.

## Hand in your evidence

Save your edited functions, the two worksheets and the public certificate copy created in Exercise 3 at `worksheets/localhost.crt`. Record its public details and fingerprint so the tutor can match it to your results. Keep terminal sign-in codes, `.env`, actual note databases and the TLS private key out of your submission. Check `git status --short` before committing. Use the submission method your lecturer supplies.
