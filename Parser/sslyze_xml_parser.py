#Read ME - SSLYZE Output file processed as XML
#Input - SSLYZE Output XML File
#Output - Dictonary (Contains the hostname, ip, port, SSL versions and respective weak ciphers if any)
import xml.etree.ElementTree as ET
import os

#Check for SSL Supported Versions
def is_ssl_version_supported(root,search_element):
	status="Error" #Return Error in case of the element / parameter not found
	for element in root.iter(search_element):
		if element: #Check if the element is present or not
			if element.attrib['isProtocolSupported']: #Check if the element has the parameter isProtocolSupported
				status= element.attrib['isProtocolSupported'] #Return True or False
	return status

#Check weak ciphers is enabled on the enabled SSL versions
def is_weak_cipher_enabled(root,search_element):
	weak_cipher_list=[]
	for element in root.iter(search_element): #Root Element - SSLv3 or TLS1_1 or TLS1_2
		if element: #check if there is further elements like <acceptedCipherSuites , <preferredCipherSuite, <rejectedCipherSuites
			for childs in element.getiterator('acceptedCipherSuites'): #Loop through only acceptedCipherSuites. if changes required make it empty element.getiterator()
				if childs: #if the childs has the elements <cipherSuite
					for cipher in childs:
						if cipher.attrib: #If the cipher element has attributes like connectionstatus and name
							conn_status=cipher.attrib['connectionStatus']
							conn_cipher=cipher.attrib['name']
							if (("200" in conn_status) and ("MD5" in conn_cipher or "RC4" in conn_cipher or "SHA1" in conn_cipher or "CBC" in conn_cipher)):
								weak_cipher_list.append(conn_cipher)
	return weak_cipher_list

#Get all the SSL Version and respective cipher
def get_ssl_ciphers(root):
	ssl_ciphers={}
	ssl_versions=['sslv2','sslv3','tlsv1','tlsv1_1','tlsv1_2','tlsv1_3']
	for version in ssl_versions:
		status=is_ssl_version_supported(root,version) #Check the ssl version is supported or not
		if status=="True":
			result=is_weak_cipher_enabled(root,version) #If the version is supported then look for weak ciphers
			if result : #Check any weak cipher list came or empty
				ssl_ciphers[version]=result #If weak ciphers present, set the version to weak ciphers as list
			else:
				ssl_ciphers[version]="TRUE" #If no weak ciphers present, set version to true
		else:
			ssl_ciphers[version]="FALSE" #if the ssl version is not enabled set version to flase
	return ssl_ciphers

#Get scan details(host, ip, port)
def get_scan_details(root):
	scan_details={}
	required_details=['host','ip','port']
	for element in root.iter('target'):
		if element.attrib: #If the arget <target element has attributes (host, ip,port)
			for items in required_details:
				scan_details[items]=element.attrib[items]
	return scan_details

#Take the SSLYZE input file and parse the output
def parse_sslyze_xml_file(input_file):
	result_dict={}
	if os.path.isfile(input_file):
		tree=ET.parse(input_file)
		root=tree.getroot()
		result_dict=get_ssl_ciphers(root) #get the ssl version enabled and weak ciphers
		scan_details=get_scan_details(root) #get the host,ip,port
		result_dict.update(scan_details) #merge 2 dictonary
	else:
		print("File not Found")
	return result_dict

input_file='output.xml'
result_dict=parse_sslyze_xml_file(input_file) #Function call with file name
print(result_dict)