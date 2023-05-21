from http.server import BaseHTTPRequestHandler
from urllib import parse
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        s = self.path # path is attribute of BaseHTTPRequestHandler
        url_components = parse.urlsplit(s) 
        query_string_list=parse.parse_qsl(url_components.query) #should return a list of tuples
        dictionary=dict(query_string_list) #convert list of tuples to dictionary
        name=dictionary['name']
        age=dictionary['age']
        if name:
            message = "Hello, " + name + "!"

        else:
            message = "Hello, stranger!"


        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return