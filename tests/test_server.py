import requests

from testhttpserver import Server
import testhttpserver.server as mod


class BaseHTTPServerTest(object):

    @classmethod
    def setup_class(cls, *args, **kwargs):
        cls.server = Server(*args, **kwargs)

    @classmethod
    def teardown_class(cls):
        cls.server.join()


class WhenGettingData(BaseHTTPServerTest):

    @classmethod
    def setup_class(cls, port=8010):
        BaseHTTPServerTest.setup_class(port, response_content='CONTENT')

        cls.response = requests.get('http://localhost:8010/')

    def should_return_content(self):
        assert self.response.content == 'CONTENT'

    def should_respond_with_status_200(self):
        assert self.response.status_code == 200


class WhenPostingData(BaseHTTPServerTest):

    @classmethod
    def setup_class(cls, port=8020):
        BaseHTTPServerTest.setup_class(port)

    def should_save_post_data(self):
        requests.post('http://localhost:8020', data='POST DATA')
        assert self.server.post_data == 'POST DATA'
