#Remove Duplicates from list - Input (list)1 | Output (list)1
def remove_duplicate_list(input_list):
	output_list = list(set(input_list))
	return output_list

#Remove Empty elements from list  - Input (list)1 | Output (list)1
def remove_empty_element_list(input_list)
	output_list = [x for x in input_list if x] 
	return output_list

#Convert list to File - Input (input_list, output_file)2 | Output (output_file)1
def list_to_file(input_list,output_file):
	with open(output_file,'w') as fi:
		for element in input_list:
			fi.write(element+"\n")
        return output_file

#Convert file to list - Input (input_file)1 | Output (list)1
def file_to_list(input_file): 
	output_list=[]
	if os.path.isfile(input_file): #Check file exist
		with open(output_file) as f: #Open file
			output_list = f.read().splitlines() #Convert file to list
	return output_list

#Get the file details - Input (filename)1 | Output (file_abspath,dir_abspath,filename_withext,filename_only,file_ext_only) 5
def get_file_details(input_file):
	#Get absolute path of the file
	file_abspath=os.path.abspath(input_file)
	#Get the directory path - leaving the file name
	dir_abspath=os.path.dirname(file_abspath)
	#Get the File name with extension
	filename_withext=os.path.basename(file_abspath)
	#Get the filename removing the extension 
	filename_only=os.path.splitext(filename_withext)[0]  #Assuming there is only 1 dot
	#Get the extension
	file_ext_only=os.path.splitext(filename_withext)[1]  #Assuming there is only 1 dot
	return file_abspath,dir_abspath,filename_withext,filename_only,file_ext_only

#Open file and replace particular string and save the file in same name - Input (filename)1 | Output()
def file_string_replace(input_file):
	f1=open(input_file,"r+")
	input=f1.read()
	input=input.replace('<BR>','\n') #Replace all the '<BR>' with new line
	f2=open(input_file,"w+")
	f2.write(input)
	f1.close()
	f2.close()