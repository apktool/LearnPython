# socket|server|tcp

import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
serversocket.bind(('127.0.0.1',9999))
serversocket.listen(5)

(conn,addr)=serversocket.accept()

data = conn.recv(1024)
print('server received data:%s'%(data))
conn.send(data)

serversocket.close()
