"""Python v2.7.9 Server in Linux and listen for linux client (Same machine)
   works for single connection"""

import socket

host1="10.0.2.15"
port1=5555

try:
	s_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s_sock.bind((host1,port1))
	s_sock.listen(2)
	c_sock,c_addr=s_sock.accept()
	print("Connection Received from "+c_addr[0]+":"+str(c_addr[1]))
	result=c_sock.recv(2000)
	c_sock.send("Server hello")
	print("Received Data:"+result)
	s_sock.close()
except Exception,e:
	print(e)
