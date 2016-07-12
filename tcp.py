import socket
import commands
HOST='0.0.0.0'
PORT=50000
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
while 1:
	conn,addr=s.accept()
	print'Connected by',addr
	while 1:
		data=conn.recv(1600)
		print data
		conn.sendall(data.upper())

conn.close()
