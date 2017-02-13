# socket|server|udp

import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind(('127.0.0.1',9999))
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

(data,addr)=serversocket.recvfrom(1024)
print('Received %s'%(data))

serversocket.close()
