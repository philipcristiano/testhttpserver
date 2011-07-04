Test HTTP Server
================

This is a simple HTTP server that will respond to a single HTTP request and
record some of the data. It is still an early version and doesn't do
everything you probably want.

Installing
==========

    pip install testhttpserver

Using in your tests
===================

To create a test server import the server

    from testhttpserver import Server

And then create a new instance including the port, response status and
content.

    server = Server(8000, response_status=200, response_content='Content')

After you make your request to http://localhost:8000/ . If you POST to the
server it will have ``post_headers`` and ``post_content`` available.

When you are done remember to ``join()``!

    server.join()

See ``tests/test_server.py`` for an example!
