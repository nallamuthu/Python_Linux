import xmltodict

def parse_nmap_xml_file(input_file):
	open_ports_service={}
	with open(input_file) as fd:
	    col_ordered_dict = xmltodict.parse(fd.read())
	host_status=col_ordered_dict['nmaprun']['runstats']['hosts']['@up'] #Get the Host status Valye 1 or 0
	if host_status=="1": #if Host status is up then process further
		#Loop Through all the open ports and get the list
		for items in col_ordered_dict['nmaprun']['host']['ports']['port']:
			if items['state']['@state']=="open":
				open_ports_service[items['@portid']] = items['service']['@name']
	return host_status,open_ports_service
	

host_status,open_ports_service=parse_nmap_xml_file('output.xml')
print("Host Status: "+host_status)
print("Ports->Service: "+open_ports_service)