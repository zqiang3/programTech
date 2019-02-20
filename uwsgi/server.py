#! /usr/bin/env python
# coding: utf-8

import socket
import sys
import StringIO
from app import application
from datetime import datetime

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class WSGIServer(object):

    def __init__(self, server_address):
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_sock.bind(server_address)
        self.listen_sock.listen(5)
        (host, port) = self.listen_sock.getsockname()
        self.server_port = port
        self.server_name = socket.getfqdn(host)

    def set_application(self, application):
        self.application = application

    def get_environ(self):
        self.env = {
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'http',
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.run_once': False,
            'REQUEST_METHOD': self.request_method,
            'PATH_INFO': self.request_path,
            'SERVER_NAME': self.server_name,
            'SERVER_PORT': str(self.server_port),
            'wsgi.input': StringIO.StringIO(self.request_data),
        }
        return self.env

    def start_response(self, http_status, http_headers):
        self.http_status = http_status
        self.http_headers = dict(http_headers)
        headers = {
                'Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),
                'Server': 'WSGIServer 1.0'
        }
        self.http_headers.update(headers)

    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_info = request_line.split(' ')
        (self.request_method,
        self.request_path,
        self.request_version) = request_info

    def get_http_response(self, response_data):
        res = 'HTTP/1.1 {status} \r\n'.format(status=self.http_status)
        for header in self.http_headers.items():
            res += '{0}: {1} \r\n'.format(*header)

        res += '\r\n'
        res_body = ''
        for val in response_data:
            res_body += val

        res += res_body
        return res

    def handle_request(self):
        conn, addr = self.listen_sock.accept()

        self.request_data = conn.recv(1024)
        self.parse_request(self.request_data)

        env = self.get_environ()
        start_response = self.start_response

        response_data = self.application(env, start_response)

        res = self.get_http_response(response_data)
        conn.sendall(res)

        conn.close()


def make_server(server_address, application):
    wsgi_server = WSGIServer(server_address)
    wsgi_server.set_application(application)

    return wsgi_server

SERVER_ADDR = (HOST, PORT) = '', 8000
wsgi_server = make_server(SERVER_ADDR, application)
wsgi_server.handle_request()



