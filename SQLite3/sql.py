#Assuming There is database file call sql.db with the below structure




#Import Module
import sqlite3
#Create Connection
sqliteConnection = sqlite3.connect('sql.db')
#Commit Changes
sqliteConnection.commit()
#close connection
sqliteConnection.close()


###Select one column from any table
def select_one_column(sqliteConnection,column_name,table_name):
	select_one_column_query="select {column} from {tn}".format(column=column_name,tn=table_name)
	select_one_column_result = sqliteConnection.cursor()
	select_one_column_result.execute(select_one_column_query)
	return select_one_column_result
#Call the function
select_output=select_one_column(sqliteConnection,"address","table1")
#Process the output
for address in select_output:
	print(address)

###Select one column with condition from any table 
def select_one_column_where(sqliteConnection,column_name,table_name,where_field,where_value):
	select_one_column_where_query="select {column} from {tn} where {wf}=?".format(column=column_name,tn=table_name,wf=where_field)
	data=(where_value,)
	select_one_column_where_result = sqliteConnection.cursor()
	select_one_column_where_result.execute(select_one_column_where_query,data)
	return select_one_column_where_result
#Call the function
select_output=select_one_column_where(sqliteConnection,"address","table1","name","nalla")
#Process the output
for address in select_output:
	print(address)

###Select two column from any table
def select_two_column(sqliteConnection,column_name1,column_name2,table_name):
	select_two_column_query="select {column1},{column2} from {tn}".format(column1=column_name1,column2=column_name2,tn=table_name)
	select_two_column_result = sqliteConnection.cursor()
	select_two_column_result.execute(select_two_column_query)
	return select_two_column_result
#Call the function
select_output=select_two_column(sqliteConnection,"address","count","table1")
#Process the output
for address,count in select_output:
	print(address+" "+count)

###Update One Field in any Table
def update_one_field(sqliteConnection,table_name,set_field1,set_value1,where_field,where_value):
	update_one_field_query="UPDATE {tn} SET {sf1}=? WHERE {wf}=?".format(tn=table_name,sf1=set_field1, wf=where_field)
	data = (set_value1, where_value) #SQLITE does not support address data type. Covert to string before store it to DB
	sqliteConnection.execute(update_one_field_query, data)
	sqliteConnection.commit()
#Call the function
update_one_field(sqliteConnection,'table1','count','6','name','Anything')

###Update Two Field in any Table
def update_two_field(sqliteConnection,table_name,set_field1,set_value1,set_field2,set_value2,where_field,where_value):
	update_two_field_query="UPDATE {tn} SET {sf1}=?,{sf2}=? WHERE {wf}=?".format(tn=table_name,sf1=set_field1,sf2=set_field2, wf=where_field)
	data = (set_value1,str(set_value2), where_value) #SQLITE does not support address data type. Covert to string before store it to DB
	sqliteConnection.execute(update_two_field_query, data)
	sqliteConnection.commit()
#Call the function
update_two_field(sqliteConnection,'table1','count','6','address','hello','name','Something')

###Update Three Field in any Table
def update_three_field(sqliteConnection,table_name,set_field1,set_value1,set_field2,set_value2,set_field3,set_value3,where_field,where_value):
	update_three_field_query="UPDATE {tn} SET {sf1}=?,{sf2}=?,{sf3}=? WHERE {wf}=?".format(tn=table_name,sf1=set_field1,sf2=set_field2,sf3=set_field3,wf=where_field)
	data = (set_value1,str(set_value2).strip('[]'),str(set_value3),where_value) #if required remove [] from the data
	sqliteConnection.execute(update_three_field_query, data)
	sqliteConnection.commit()
#Call the function
update_three_field(sqliteConnection,'table1','count','6','address','hello','path','/root/text.txt','name','123')


###Insert any 4 columns values into any table
def insert_four_field(sqliteConnection,table_name,update_field1,update_value1,update_field2,update_value2,update_field3,update_value3,update_field4,update_value4):
	insert_four_field_query="INSERT INTO {tn} ({uf1},{uf2},{uf3},{uf4}) VALUES (?,?,?,?)".format(tn=table_name,uf1=update_field1,uf2=update_field2,uf3=update_field3,uf4=update_field4)
	data = (update_value1,update_value2,update_value3,update_value4)
	sqliteConnection.execute(insert_four_field_query, data)
	sqliteConnection.commit()
#Call the function
insert_four_field(sqliteConnection,'table1','name','just','count','45','address','abu dhabi','path','/bin/1.txt')



