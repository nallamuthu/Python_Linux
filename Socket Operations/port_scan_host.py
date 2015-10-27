"""" Python v3.4.2 Port Scanning for the given host. Display all the open ports"""


import socket

global host

def port_scan():
	global host
	print("[+] Port scanning initiated for "+str(host)+"...")
	for i in range(20,35):
		soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			soc.connect((host,i))
			print("Port %s : OPEN"%(str(i)))
		except Exception as e:
			pass
		soc.close()
	print("[+] Scanning Done [+]")

valid=True
host=input("Enter the host IP:")
valid_host=host.split(".")
len_host=len(valid_host)
if (len_host<4) or (len_host>4):
	print("Invalid Host")
elif len_host==4:
	for i in valid_host:
		if (int(i)<0) or (int(i)>255):
			print("Invalid Host")
			valid=False
			break
	if valid:
		print("Scan Started")
		port_scan()




