""" Python v2.7.9 Linux client request linux server (Same machine)"""

import socket

s_host="10.0.2.15"
s_port=6666

try:
	socket.setdefaulttimeout(5)
	c_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	c_sock.connect((s_host,s_port))
	c_sock.send("Client hello")
	result=c_sock.recv(5000)
	print(result)
	c_sock.close()
except Exception,e:
	print(e)
	
