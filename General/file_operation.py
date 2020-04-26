import os


#Open file and replace particular string and save the file in same name
def file_string_replace(input_file):
	f1=open(input_file,"r+")
	input=f1.read()
	input=input.replace('<BR>','\n') #Replace all the '<BR>' with new line
	f2=open(input_file,"w+")
	f2.write(input)
	f1.close()
	f2.close()
    

input_file='inp_file.txt'
#Check if file exist
if os.path.isfile(output_file):
    file_string_replace(output_file)