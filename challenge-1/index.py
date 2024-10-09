import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import datetime

# A list of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the coffee file a police report? It got mugged!"
]

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        random_joke = random.choice(jokes)

        # HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Random Joke Server</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    background-color: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 1.2em;
                }}
                footer {{
                    margin-top: 20px;
                    font-size: 0.8em;
                    color: #777;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Random Joke Generator</h1>
                <p>{random_joke}</p>
                <p><strong>Current Time:</strong> {current_time}</p>
            </div>
            <footer>
                <p>Refresh the page for a new joke! ;)</p>
            </footer>
        </body>
        </html>
        """
        
        self.wfile.write(html_content.encode('utf-8'))

def run_server(host, port):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print(f"Server started on {host}:{port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Web Server with Jokes")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to run the server on")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on")

    args = parser.parse_args()

    run_server(args.host, args.port)

