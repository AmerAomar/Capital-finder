from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Welcome to capital finder server\n\n''If you want to get the capital of specific country you can put the country name for example "jordan" /capital-finder?country=jordan\n\n''if you want to get the country by entering the capital you can put the capital name for example "amman" /capital-finder?capital=amman '.encode('utf-8'))
        return