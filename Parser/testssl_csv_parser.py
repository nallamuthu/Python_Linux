#Read Me - Receive the testssl csv output file and parse it
#Input   - testssl out csv file
#Output  - Dictonary contains ssl vulnerability details
import csv

#Function call to parser the CSV File
def parse_testssl_csv_file(input_file):
	result_dict={}
	search_list=['heartbleed','ccs','ticketbleed','robot','crime_tls','breach','poodle_ssl','freak','beast','lucky13','sweet32','logjam','drown','secure_renego','secure_client_renego','fallback_scsv']	
	heartbleed=ccs=ticketbleed=robot=crime=breach=poodle=freak=beast=lucky13=sweet32=logjam=drown=sr_server=sr_client=fallback_scsv="N/A"
	with open(input_file, 'r') as file:
		reader = csv.reader(file)
		for csv_row in reader:
			for item in search_list:
				if item == csv_row[0].lower(): #csv_row[0] contains the vulnerability name
					result_dict[item]=csv_row[3] #csv_row[3] contains the result vulnerable or not
				heartbleed=csv_row[3]
	return result_dict #Result dict
	
#Call to function by passing the testssl out file
result_dict=parse_testssl_csv_file('out.csv')
print(result_dict)
