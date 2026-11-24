#!/usr/bin/env bash
# Generate a certificate and private key for a seven-day localhost experiment.
set -eu
cd "$(dirname "$0")/.."
umask 077
dir=.dev-tls

# Claim a new private directory. Preserve a pair from a previous run.
if ! mkdir -m 700 "$dir" 2>/dev/null; then
    if [[ -s "$dir/localhost.crt" && -s "$dir/localhost.key" ]]; then
        echo "Keeping the existing localhost certificate and key."
        exit 0
    fi
    echo "Cannot create .dev-tls. Check its permissions or see the TLS troubleshooting table." >&2
    exit 1
fi

# -x509 self-signs the new certificate. -noenc keeps this lab key usable
# without typing a passphrase. The directory and files are owner-only.
openssl req -x509 -newkey rsa:2048 -sha256 -noenc -days 7 \
    -keyout "$dir/localhost.key" -out "$dir/localhost.crt" \
    -subj "/CN=localhost" \
    -addext "subjectAltName=DNS:localhost" \
    -addext "basicConstraints=critical,CA:FALSE" \
    -addext "keyUsage=critical,digitalSignature,keyEncipherment" \
    -addext "extendedKeyUsage=serverAuth"
echo "Created .dev-tls/localhost.crt and .dev-tls/localhost.key."
