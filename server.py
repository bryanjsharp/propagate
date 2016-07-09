#! /usr/bin/env python

import SocketServer
import SimpleHTTPServer


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9999
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving at port", PORT
    httpd.serve_forever()
