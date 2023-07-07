import http.server
import socketserver
import datetime

PORT = 8000 

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        today = datetime.datetime.now().strftime("%d %B %Y")
        message = f"<h1>Today is {today}</h1>"
        self.wfile.write(message.encode())

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()

