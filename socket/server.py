import socket

HOST = '127.0.0.1'
PORT = 19000

BUFSIZE = 5

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'set address reuse'
s.bind((HOST, PORT))


s.listen(5)
print 'start listening...'
conn, addr = s.accept()
while True:
    r = conn.recv(BUFSIZE)
    if r == 'quit':
        break
    print r
print 'finished'
