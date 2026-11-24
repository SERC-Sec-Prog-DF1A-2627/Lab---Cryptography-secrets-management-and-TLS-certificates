#!/usr/bin/env bash
# With tls/serve.py running, verify both expected results without changing trust stores.
set -eu
cd "$(dirname "$0")/../.."
args=(--ipv4 --noproxy '*' --silent --show-error --max-time 5)
url=https://localhost:4443/
status=0
curl "${args[@]}" "$url" || status=$?
if [[ "$status" -ne 60 ]]; then
    echo "Expected certificate verification exit 60. Observed $status." >&2
    exit 1
fi
echo "Default trust: rejected (60)."
body=$(curl "${args[@]}" --cacert .dev-tls/localhost.crt "$url")
if [[ "$body" != "College TLS lab: HTTPS is working." ]]; then
    echo "Unexpected HTTPS response." >&2
    exit 1
fi
echo "Explicit trust: accepted (0). $body"
