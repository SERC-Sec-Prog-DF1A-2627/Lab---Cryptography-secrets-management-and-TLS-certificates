# Activity 1 · Exemplar reasoning

Other answers can earn credit when their assumptions match the scenario. Look for the asset, the party holding a key or trusted value, and a limit on the assurance.

| Case | Suitable choice and reason | Trust assumption and remaining risk |
|---|---|---|
| 1. Returning user | A salted, costed password hash such as Argon2id allows verification of a guess. Store the encoded verifier and parameters. | A unique salt per password prevents efficient reuse of work across accounts. A weak password can still be guessed after a verifier leak. |
| 2. Confidential note | Authenticated encryption such as Fernet lets authorised application code recover the text and detect token modification. | Guard the symmetric key separately from the backup. A running process with the key can read or create valid tokens. The application must enforce ownership. |
| 3. Public PDF | Sign the document with the college’s private signing key. Recipients can use the authentic public key to verify integrity and origin. | Recipients must trust the association between public key and college. Keep the signing key private. The signature does not hide the document. |
| 4. Browser submission | HTTPS with successful server certificate validation protects traffic in transit and authenticates the intended server name. | Trustworthy client roots, the right hostname, valid dates and possession of the server key matter. The application sees plaintext at an endpoint. Stored records need a separate control. |
| 5. Transfer file | Compute and verify an HMAC over the same file bytes with the shared integrity key. | The third party lacks the key. Either authorised service can create a tag, so the tag alone cannot distinguish the two authors. A plain digest beside a replaceable file can also be replaced. |

**Example defence.** A hash would let the college compare a candidate note, but Alex needs to recover the original text. Authenticated encryption meets that requirement while the application keeps the key available and enforces ownership.
