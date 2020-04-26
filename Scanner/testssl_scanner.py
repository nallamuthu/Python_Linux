from EXECUTE_COMMAND import *

#wget -O testssl.sh  https://testssl.sh
#chmod a+x testssl.sh
#or
#sudo apt-get install testssl.sh


#testssl -h --jsonfile out.json -U wrong.host.badssl.com:443
#testssl -h --csvfile out.csv -U wrong.host.badssl.com:443

#Initiate TestSSL Scan for the target
def ssl_vuln_scan_initialize(hostname,port):
	dest_server=hostname+":"+str(port)
	output_file=dest_server+"_.csv"
	cmd="testssl --openssl-timeout 120 --csvfile "+output_file+" -U "+dest_server
	return_code=execute_command(cmd,'testssl')
	status = "Failed"
	if os.path.isfile(output_file):
		status = "Success"
	else:
		status = "Failed"
	return status


hostname="wrong.host.badssl.com"
port = 443
status=ssl_vuln_scan_initialize(hostname,port)
print(status)