import socket

HOST = '127.0.0.1'
PORT = 19000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT+1))
s.connect((HOST, PORT))
print 'connect success'
while True:
    cmd = raw_input("please input command: ")
    s.send(cmd)
    if cmd == "quit":
        break

print 'finish'
