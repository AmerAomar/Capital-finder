from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class CustomRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        country = dictionary.get('country')
        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            response = requests.get(url)
            data = response.json()
            if isinstance(data, list):
                country_data = data[0]
                capital = country_data["capital"]
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(capital.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Country not found.")
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Missing 'country' parameter.")

        return
