#! /usr/bin/python3

import os
import sys
import socketserver
import http.server

PORT = 8000
html_dir = 'docs'

if len(sys.argv) > 1:
    html_dir = sys.argv[1]


html_dir = os.path.join(os.path.dirname(__file__), html_dir)
os.chdir(html_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print("html dir = " + html_dir)
print("serving at port", PORT)
httpd.serve_forever()
