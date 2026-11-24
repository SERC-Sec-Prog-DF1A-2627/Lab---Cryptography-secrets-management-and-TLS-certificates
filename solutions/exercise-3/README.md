# Exercise 3 · Exemplar results and reflections

The complete [certificate generator](../../tls/generate.sh) and [HTTPS server](../../tls/serve.py) are supplied to all students. From the repository root, run `bash tls/generate.sh`, inspect the public file with the command in [the walkthrough](../../exercises/03-tls.md), then run `python tls/serve.py`. In terminal B, `bash solutions/exercise-3/check_local.sh` repeats both verification cases and checks their outcomes.

| Evidence | An acceptable answer |
|---|---|
| Public website certificate | Record the actual hostname or matching SAN, issuer, start/end dates and browser chain on the observation date. A current issuing intermediate can change. A domain match, valid time and accepted path to a client trust anchor explain acceptance. |
| Local public certificate | Subject and issuer both identify `localhost`. The SAN contains `DNS:localhost`. The two dates span about seven days. Submit your public copy at `worksheets/localhost.crt` and give its actual SHA-256 fingerprint. |
| Default trust settings | curl returns exit 60. In the controlled setup, it reports an untrusted self-signed certificate and withholds the HTTP response. |
| Explicit trust for this request | curl returns exit 0 and the body `College TLS lab: HTTPS is working.`. It can verify the same server against the specific certificate supplied. |

## Reflection exemplars

1. **What changed?** The client’s source of trust changed. I used the same URL, server, server key and certificate. My second request explicitly trusted the certificate I generated in this Codespace. The first client did not accept any HTTP data. The second connection met its identity checks and delivered encrypted HTTP traffic.
2. **What does the certificate do?** The certificate associates a name with a public key. The client checks the SAN, dates and issuer chain against its trust settings. In a typical TLS 1.3 handshake the server proves possession of its private key. Negotiated symmetric traffic keys protect the HTTP data. The certificate itself can be public.
3. **Which would I deploy?** For a portal used by arbitrary students’ browsers, a public CA such as Let’s Encrypt can validate domain control and issue a chain that typical clients already trust. I would automate renewal, verify the renewed certificate is loaded and restrict access to the private key. If that key is exposed, replace it and seek revocation of the affected certificate. For a private local test, I can generate a short-lived self-signed certificate and supply that known public certificate to my test client. A client that has no trustworthy copy has no basis to authenticate the self-signed identity.

**Codespaces comparison.** The public forwarded address authenticates the GitHub-managed endpoint. The exercise inspects the Python server’s certificate by using loopback from within the same Codespace.
