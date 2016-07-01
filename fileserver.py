import socket
import thread

BUFF = 1024
PORT = 9999
s = socket.socket()
host = socket.gethostname()

def handler(clientsock, addr):
    while 1:
        data = clientsock.recv(BUFF)
        if not data:
            break
        print repr(addr) + ' recv:' + repr(data)
        clientsock.send(response(data))
        print repr(addr) + ' sent:' + repr(respons(data))
        if "close" == data.rstrip():
            break
    clientsock.close()
    print addr, "- closed connection" # logs on the console


if __name__=='__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))


print "Server listening...."

while True:
    conn, addr = s.accept()
    print "Got connection from", addr
    data = conn.recv(1024)
    print("server received", repr(data))

    filename = "mytext.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while(l):
        conn.send(l)
        print("sent ", repr(1))
        l = f.read(1024)
    f.close()

    print("Done sending")
    conn.send("Thank you for connecting")
    conn.close()
