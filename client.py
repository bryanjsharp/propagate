#! /usr/bin/env python

import socket

BUFF = 1024

if __name__ == "__main__":
    s = socket.socket()
    host = "127.0.0.1"
    port = 9999
    s.connect((host, port))
    with open("recv.torrent", 'wb') as f:
        print 'file opened'
        print('receiving data...')
        while True:
            data = s.recv(BUFF)
            print('data=%s', (data))
            if not data:
                break
            #write to file
            f.write(data)
    f.close()
    print "Success!"
    s.close()
    print('connection closed')
