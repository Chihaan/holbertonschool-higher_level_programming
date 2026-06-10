#!/usr/bin/python3
"""Simple HTTP server built with the http.server module."""

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json


class MonHandler(BaseHTTPRequestHandler):
    """Request handler that routes GET requests for the simple API."""

    def do_GET(self):
        """Route the GET request and send the matching response."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())
        elif self.path == "/info":
            version = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            info = json.dumps(version)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(info.encode())
        elif self.path == "/data":
            personnes = {"name": "John", "age": 30, "city": "New York"}
            corps = json.dumps(personnes)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(corps.encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":
    serveur = HTTPServer(("localhost", 8000), MonHandler)
    serveur.serve_forever()
