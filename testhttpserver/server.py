from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

class Server(object):

    def __init__(self, port, response_status=200, response_content=''):
        self.post_data = None

        class Handler(BaseHTTPRequestHandler):

            def do_POST(handler):
                self.post_headers = handler.headers
                length = int(handler.headers['Content-Length'])
                self.post_data = handler.rfile.read(length)

                handler.respond()

            def do_GET(handler):
                handler.respond()

            def respond(handler):
                handler.send_response(response_status)
                handler.end_headers()
                handler.rfile.write(response_content)

        self.server = HTTPServer(('localhost', port), Handler)
        self.server.timeout = 5
        self.thread = Thread(target=self.server.handle_request)
        self.thread.daemon = True
        self.thread.start()

    def join(self):
        self.thread.join()


