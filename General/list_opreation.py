#Convert File to List - each line will be treated as 1 elemtent in list
file_list = [line.rstrip('\n') for line in open("filename.txt")]
#Remove all the duplicate element from the list
file_list = list(set(file_list))
#Remove the empty elements/'' from the list
file_list = [x for x in file_list if x] 
#Total elements count in list
list_count=len(file_list)
#Search element exist in List
if "search_text" in file_list: 
	print("Element Found")

#Write list to File
input_list=['line1','line2','line3']
with open('out_file.txt','w') as fi:
	for element in input_list:
		fi.write(element+"\n")