#! /usr/bin/python3

import os
import socketserver
import http.server

PORT = 8000


html_dir = os.path.join(os.path.dirname(__file__), 'site')
os.chdir(html_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)

httpd.serve_forever()
