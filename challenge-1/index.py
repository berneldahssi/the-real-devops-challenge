import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def run_server(host, port):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f"Server started on {host}:{port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Web Server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to run the server on")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")

    args = parser.parse_args()

    run_server(args.host, args.port)


