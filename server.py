#! /usr/bin/env python

import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        #file stuff
        filename = "test.torrent"
        f = open(filename, "rb")
        file = f.read(1024)
        while (file):
            self.request.send(file)
            print ('Sent ', repr(file))
            file = f.read(1024)
        f.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()
