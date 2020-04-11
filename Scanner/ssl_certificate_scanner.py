#Read Me - Make connection to remote host and port and get the certificate
#Input   - Hostname and Port
#Output  - Dictonary contains Certificate (Expired or not, Expiry Date, Expiry Days Count, Digital Signature Algorithm)
 
import OpenSSL
import ssl, socket
from datetime import timedelta, date

#Get Certificate Details
def get_cert_details(hostname,port):
	result_dict={'expiry_status':'N/A','expiry_date':'N/A','expiry_in':'N/A','sign_alg':'N/A'}
	try:
		public_cert_obj=ssl.get_server_certificate((hostname, port))
		x509_object = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, public_cert_obj)
		exp_date =x509_object.get_notAfter()
		exp_day = int(exp_date[6:8].decode('utf-8'))
		exp_month = int(exp_date[4:6].decode('utf-8'))
		exp_year = int(exp_date[:4].decode('utf-8'))
		exp_date = str(exp_year) + "-" + str(exp_month) + "-" + str(exp_day)
		result_dict['expiry_status']=x509_object.has_expired() #Certificate Expired or not
		result_dict['expiry_date']=exp_date #The Date in which the certificate Expires
		result_dict['expiry_in']=(date(exp_year,exp_month,exp_day)-date.today()).days #Get the No.of.Days Left for Expiry
		result_dict['sign_alg']=(x509_object.get_signature_algorithm()).decode('utf-8') #Get the signature algorithm
	except Exception as e:
		#print(e)
		result_dict = dict.fromkeys( result_dict, "ERROR" ) #if any error occurs set all the value to ERROR
	return result_dict 	#Return the dict contains the result


#Main entry for program
hostname="expired.badssl.com"
port = 443
#Function call to get the details
result_dict=get_cert_details(hostname,port)
print(result_dict)