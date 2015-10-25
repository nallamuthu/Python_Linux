""" python v2.7.9 file write operation """


portlist=[21,22,25,80,8080,9999,8888,143,3306]
servicelist=['FTP','SMTP','MYSQL','HTTP']

fi=open('ports.txt','w')
for ports in portlist:
	fi.write(str(ports)+"\n")
fi.close()


with open('services.txt','w') as fi:
	for services in servicelist:
		fi.write(services+"\n")
