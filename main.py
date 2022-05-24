from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver
import webbrowser

port = 80
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as http:
    print("Serving at port ", port)
    http.serve_forever()

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        text  =open("htnl.html", "rb")
        text_to_send=text.read()

        text_decode = text_to_send.decode("utf-8")

        self.wfile.write(text_decode.encode())


def main():
    PORT = 8080
    server = HTTPServer(('10.1.1.24', PORT), helloHandler)
    print(f"server running on port {PORT}")
    server.serve_forever()


if __name__ == '__main__':
    main()