#Perform top port scan

from execute_command import * #Import the python file in the same github path. Contains 2 function execute_command,is_folder_exit
import sys
import os


#Perform the NMAP Scan
def nmap_scan_perform(out_dir,ip_addr):
	output_file=out_dir+ip_addr+"_NMAP.xml"
	cmd="nmap "+ip_addr+" --top-ports 100 -oX "+output_file
	return_value=execute_command(cmd,"NMAP")        #Function scan to execute os commands using subprocess
	if return_value=="SUCCESS" and os.path.isfile(output_file):
		pass
	else:
		output_file="N/A"
	return output_file #Return the path of the xml file contains the nmap output
    
    
#Main entry for program   
out_dir='OUTPUT/NMAP_OUTPUT/'
ip_addr='1.1.1.1'
if is_folder_exit(out_dir)=="SUCCESS":  
    output_file=nmap_scan_perform(out_dir,ip_addr)  #Check if the folder exist if not create it
    print(output_file)