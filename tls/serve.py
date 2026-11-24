"""Serve a fixed reply on loopback. The server never serves repository files."""
import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

TLS_DIR = Path(__file__).resolve().parents[1] / ".dev-tls"


class Reply(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_error(404)
            return
        body = b"College TLS lab: HTTPS is working.\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.load_cert_chain(TLS_DIR / "localhost.crt", TLS_DIR / "localhost.key")
    with HTTPServer(("127.0.0.1", 4443), Reply) as server:
        server.socket = context.wrap_socket(server.socket, server_side=True)
        print("TLS lab listening on loopback, port 4443. Stop with Ctrl+C.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
