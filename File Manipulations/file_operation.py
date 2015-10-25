"""" python v2.7.9 various file operations"""


fi=open("file1.txt",'rwb+')
inp=raw_input("Enter a string to write to file:")
fi.write(inp)
print("[+] File Attributes [+]")
print("File Name:"+fi.name)
print("File Mode:"+fi.mode)
print("File Closed:"+str(fi.closed))
print("[+] File Methods [+]")
print("File pointer:"+str(fi.tell()))
fi.seek(0)
print("File pointer:"+str(fi.tell()))
print("File read 5 bytes:"+fi.read(5))
print("File read remaining:"+fi.read())
inp=raw_input("enter a string to append to file:")
fi.write(inp)
fi.close()
print("[+] File closed[+]")


