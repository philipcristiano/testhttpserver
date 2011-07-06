from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class Server(object):

    def __init__(self, port, response_status=200, response_content='', response_headers=None):
        self.post_data = None
        if response_headers is None:
            response_headers = []

        class Handler(BaseHTTPRequestHandler):

            def respond(handler):
                handler.send_response(response_status)
                for header, value in response_headers:
                    print header, value
                    handler.send_header(header, value)
                handler.end_headers()
                handler.rfile.write(response_content)

            def request_handler(handler):
                self.request_headers = handler.headers
                length = int(handler.headers.get('Content-Length', 0))
                self.request_content = handler.rfile.read(length)

                handler.respond()

            def __getattr__(self, name):
                if not name.startswith('do_'):
                    raise AttributeError
                return self.request_handler

        self.server = HTTPServer(('localhost', port), Handler)
        self.server.timeout = 5
        self.thread = Thread(target=self.server.handle_request)
        self.thread.daemon = True
        self.thread.start()

    def join(self):
        self.thread.join()


