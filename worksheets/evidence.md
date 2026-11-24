# Individual evidence · College Secure Notes

Use short observations and reasons. Use fictional examples. Record public certificate fields, abbreviated token previews and exit codes. Keep private keys, local sign-in codes, whole tokens and the contents of `.env` out of this sheet.

## Exercise 1

| Observation | Your evidence |
|---|---|
| UTF-8 input and text shown after saving | |
| One database row: owner, SQLite type, token length or short prefix | |
| What Alex sees after the sample changes, and what happens to an intact note | |
| What Sam sees and the exact SQL condition that explains it | |
| What someone with only a database copy could still learn | |
| What the same decrypt error can and cannot establish | |

## Exercise 2

| Test | Predicted result | Observed message and exit code |
|---|---|---|
| Valid local key | | |
| Missing key in an isolated process | | |
| Invalid process value with a valid local file present | | |
| Restart with the same key and same database | | |

Git’s rule that matches `.env`:  
What the restart proves:  
What would happen to existing records after silently substituting a new valid key?

## Five-minute individual check

1. A backup contains a note ID, owner and Fernet token. What remains visible to the backup holder? What additional item would let them read the note body?
2. An owner sees “This note could not be verified.” Give two possible causes and one safe display behaviour.
3. A colleague proposes generating a new key every time configuration is missing. Predict the result on the next restart and justify your preferred behaviour.

## Exercise 3

Public HTTPS site and date observed:  
Covered DNS name (SAN):  
Issuer:  
Valid from / until (include time zone):  
Root or trust anchor shown by the browser, and why the browser accepted this name:

Local public certificate subject, issuer, SAN, dates and SHA-256 fingerprint:  
Generated public certificate for submission: `worksheets/localhost.crt`. Its fingerprint matches the local server certificate:  

| Request made inside the Codespace | Prediction | Actual result and what it shows |
|---|---|---|
| System trust settings, `https://localhost:4443/` | | |
| Same URL with `--cacert .dev-tls/localhost.crt` | | |

1. What changed between the two requests? What stayed the same?
2. How does a certificate help the client authenticate the server? What protects HTTP data once the handshake succeeds?
3. Choose a certificate for a public college portal and one for this private test. Explain who trusts each one, what is validated and how you would handle renewal and the private key.
