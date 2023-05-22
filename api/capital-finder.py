import json
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("country")
        capital = dic.get("capital")

        if country:
            url = "https://restcountries.com/v3.1/name/"
            res = requests.get(url + country)
            data = res.json()
            
            capital = data[0]['capital'][0]  # Access the capital from the response data
            text = "The capital of " + country + " is " + capital
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(text.encode('utf-8'))  # Send the capital as the response to the user

        elif capital:
            url = "https://restcountries.com/v3.1/capital/"
            res = requests.get(url + capital)
            data = res.json()

            country = data[0]['name']['common']
            #The capital of X is Y
            text = capital + " is the capital of " + country
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(text.encode('utf-8'))

        return
