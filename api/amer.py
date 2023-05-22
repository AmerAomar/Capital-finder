from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path  # path is an attribute of BaseHTTPRequestHandler
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)  # should return a list of tuples
        dictionary = dict(query_string_list)  # convert the list of tuples to a dictionary
        name = dictionary.get('name')
        age = dictionary.get('age')
        if name:
            message = "Hello, " + name + "!"
        else:
            message = "Hello, stranger!"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("hi".encode('utf-8'))
        return
