# socket|server

import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1',9999))
serversocket.listen(5)

conn,addr=serversocket.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print('server received data:%s', data)
    conn.send(data)

serversocket.close()
