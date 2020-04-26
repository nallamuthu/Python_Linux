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

#Get absolute path of the file
file_abspath=os.path.abspath("dir/myfile.txt")

#Get the directory path - leaving the file name
dir_abspath=os.path.dirname(file_abspath)

#Get the File name with extension
filename_withext=os.path.basename(file_abspath)

#Get the filename removing the extension 
filename=os.path.splitext(filename_withext)[0]  #Assuming there is only 1 dot