#Read Me - Make connection to remote host and port and get the certificate
#Input   - Hostname and Port
#Output  - Dictonary contains Certificate (Expired or not, Expiry Date, Expiry Days Count, Digital Signature Algorithm)
 
import OpenSSL
import ssl, socket
from datetime import timedelta, date

#Get Certificate Details
def get_cert_details(hostname,port):
	result_dict={}
	public_certificate=ssl.get_server_certificate((hostname, port))
	x509_object = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, public_certificate)
	exp_date =x509_object.get_notAfter()
	exp_day = int(exp_date[6:8].decode('utf-8'))
	exp_month = int(exp_date[4:6].decode('utf-8'))
	exp_year = int(exp_date[:4].decode('utf-8'))
	exp_date = str(exp_year) + "-" + str(exp_month) + "-" + str(exp_day)
	result_dict['expiry_status']=x509_object.has_expired() #Certificate Expired or not
	result_dict['expiry_date']=exp_date #The Date in which the certificate Expires
	result_dict['expiry_in']=(date(exp_year,exp_month,exp_day)-date.today()).days #Get the No.of.Days Left for Expiry
	result_dict['sign_alg']=(x509_object.get_signature_algorithm()).decode('utf-8') #Get the signature algorithm
	return result_dict


#hostname="expired.badssl.com"
#hostname="wrong.host.badssl.com"
hostname="wrong.host.badssl.com"

result_dict=get_cert_details(hostname,443)
print(result_dict)