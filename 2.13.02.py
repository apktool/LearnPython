# socket|client|udp

import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serversocket.sendto(b'hello world', ('127.0.0.1', 9999))

serversocket.close()
