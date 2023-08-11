from http.server import HTTPServer, SimpleHTTPRequestHandler

# Serve the files using Python's built-in HTTP server
server_address = ("", 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()
