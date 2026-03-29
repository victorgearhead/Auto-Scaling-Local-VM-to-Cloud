from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
server.serve_forever()
