from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from threading import Thread


class Server(object):

    def __init__(self,
        port,
        response_status=200,
        response_content='',
        response_headers=None,
        timeout=5
    ):
        """Create a new test server

        :param response_status: int of the status to return

        :param response_content: string of content to return

        :param response_headers: a list of tuples to return as headers

        :param timeout: number of seconds before the server timesout and returns

        """
        self.post_data = None
        if response_headers is None:
            response_headers = []

        class Handler(BaseHTTPRequestHandler):

            def respond(handler):
                handler.send_response(response_status)
                for header, value in response_headers:
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
        self.server.timeout = timeout
        self.thread = Thread(target=self.server.handle_request)
        self.thread.daemon = True
        self.thread.start()

    def join(self):
        self.thread.join()


