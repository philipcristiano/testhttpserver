Test HTTP Server
================

This is a simple HTTP server that will respond to a single HTTP request and
record some of the data. It is still an early version and doesn't do
everything you probably want.

[![Build Status](https://secure.travis-ci.org/philipcristiano/testhttpserver.png?branch=master)](http://travis-ci.org/philipcristiano/testhttpserver)

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
server it will have ``request_headers``, ``request_content``, and
``request_path``  available.

When you are done remember to ``join()``!

    server.join()

See ``tests/test_server.py`` for an example!


Server Parameters
================
port - The port the server will listen on

response_status - int of the status to return

response_content - string of content to return

response_headers - a list of tuples to return as headers

timeout - number of seconds before the server timesout and returns
