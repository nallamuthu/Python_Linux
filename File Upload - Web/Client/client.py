import requests

url = "http://localhost:7410/"
file_object = open('file_to_upload.txt', 'rb')
header = {'Authorization': 'any_password'}
files = {'file': file_object}
try:
    r = requests.post(url, headers=header,files=files)
    print(r.text)
finally:
	file_object.close()