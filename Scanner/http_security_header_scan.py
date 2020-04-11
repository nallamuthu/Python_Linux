import requests
import urllib3 #to supress the warning


#Suppress all the request ssl error
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#Make the request and store the response with timeout 10s
def header_scan_initialize(hostname,port,service):
	result_dict={}
	search_list=['x-xss-protection','x-content-type-options','x-frame-options','strict-transport-security'] #add the headers in small case only
	for item in search_list:
		result_dict[item]="N/A"
	try:
		target_url=service+"://"+hostname+":"+str(port)
		response = requests.get(target_url, verify=False,timeout=10)
		res_headers=dict((k.lower(), v.lower()) for k,v in (response.headers).items()) #Store the response headers in res_headers dict and convert all them to small case
		for item in search_list:
			if item in res_headers.keys():
				result_dict[item]=res_headers[item]
	except Exception as e:
		#print(e)
		result_dict = dict.fromkeys( result_dict, "ERROR" ) #if any error occurs set all the value to ERROR
	return result_dict 	#Return the dict contains the headers and respective value

hostname="demo.testfire.net"
port=443
service="https"
result_dict=header_scan_initialize(hostname,port,service)
print(result_dict)

