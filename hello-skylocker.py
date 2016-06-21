#!/usr/bin/env python

import os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
 
class HelloSkylocker(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<h2>Hello, Skylocker!</h2>")
  
    def do_POST(self):
        self.do_GET()
 
def main():
    try:
        server = HTTPServer(("", int(os.environ.get('PORT', 8080))), HelloSkylocker)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()
 
if __name__ == '__main__':
    main()
