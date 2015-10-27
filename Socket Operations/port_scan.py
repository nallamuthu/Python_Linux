"""" Python v3.4.2 Port Scanning"""

import socket
host="10.0.0.5"
print("[+] Port scanning initiated for "+str(host)+"...")
for i in range(1,9999):
	soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		soc.connect((host,i))
		print("Port %s : OPEN"%(str(i)))
	except Exception as e:
		"""print("Port %s : CLOSED"%(str(i)))	"""
		pass
	soc.close()
print("[+] Scanning Done [+]")
