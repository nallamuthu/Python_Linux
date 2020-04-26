#Covert the SQLITE DB file to CSV Files
#Input - DB File
#Output - CSV Files. For each table CSV file will be created in the name of table name
import sqlite3
import csv


#Export all the tables to csv file
def export_db_csv(db_name,output_folder):
	conn = sqlite3.connect(db_name)
	conn.text_factory = str ## my current (failed) attempt to resolve this
	cur = conn.cursor()
	tables_list=cur.execute('SELECT name from sqlite_master where type= "table"')
	for table in tables_list:
		cur = conn.cursor()
		query ='select * from {0}'.format(table[0])
		data = cur.execute(query)
		output_file = output_folder+"/"+db_name+table[0]+'.csv'
		with open(output_file, "w") as csv_file:
			csv_writer = csv.writer(csv_file, delimiter="\t")
			csv_writer.writerow([i[0] for i in data.description])
			csv_writer.writerows(data)

#Call function with DB file name
export_db_csv('ip_sheet1.db','Existing_folder')
