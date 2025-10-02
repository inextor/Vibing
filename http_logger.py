
import http.server
import socketserver
import sys

class RequestLogger(http.server.BaseHTTPRequestHandler):
    def handle_request(self):
        # Print request line
        sys.stdout.write(f'{self.requestline}\n')
        
        # Print headers
        for header, value in self.headers.items():
            sys.stdout.write(f'{header}: {value}\n')
        
        sys.stdout.write('\n')
        
        # Print body if present
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length)
            sys.stdout.write(body.decode('utf-8'))
            sys.stdout.write('\n')

        # Send a simple response
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self_message = b"Request has been logged to standard output."
        self.wfile.write(self_message)
        sys.stdout.write('----------------------------------------\n')
        sys.stdout.flush()

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def do_PUT(self):
        self.handle_request()

    def do_DELETE(self):
        self.handle_request()

    def do_PATCH(self):
        self.handle_request()

    def do_HEAD(self):
        self.handle_request()

    def do_OPTIONS(self):
        self.handle_request()

def run(server_class=http.server.HTTPServer, handler_class=RequestLogger, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    sys.stdout.write(f'Starting httpd server on port {port}...')
    sys.stdout.write('Incoming requests will be redirected to standard output.\n')
    sys.stdout.flush()
    httpd.serve_forever()

if __name__ == '__main__':
    run()
