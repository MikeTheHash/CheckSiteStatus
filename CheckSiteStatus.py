import requests
import time
import os
import random
from colorama import Fore, Back, Style
os.system("figlet CheckSiteStatus")
print("                                                         By MikeTheHash")
def check():
	user_input = input(Fore.MAGENTA + "Type the link (With http/https) > ")
	print(Style.RESET_ALL)
	try:
		r = requests.get(user_input)
	except:
		print(Fore.WHITE + Back.RED + "Error: Make sure you have entered an existing URL by also writing the http / https protocol") 
	try:
		print(f"The site responded with status: " + Fore.BLUE + f"{r.status_code}" + Style.RESET_ALL)
		other_user_input = input("Do you want the list of meanings of the status codes? [Y/N] > ")
		if other_user_input == "Y" or other_user_input == "Yes" or other_user_input == "YES" or other_user_input == "y":
			print("\n")
			print("Information message: \n    -100: Go on \n    -101: Protocol exchange in progress \nSuccessful: \n    -200: OK \n    -201: Created \n    -202: Accepted \n    -203: Non-authoritative information \n    -204: No content \n    -205: Reset Content \n    -206: Partial content \n    -207: Multi-Status \nRedirection: \n    -301: Moved permanently \n    -302: Found \n    -304: Not modified \n    -307: Temporary redirect \nClient Error: \n    -400: Invalid Requests \n    -401: Access Denied \n    -401.1: Login failed \n    -401.2: Login failed due to server configuration \n    -401.3: Access denied by ACL \n    -401.4: Authorization failed due to filter \n    -401.5: Authorization failed due to ISAPI / CGI application \n    -401.7: Access denied by URL authorization policy on the web server \n    -403: Operation not allowed \n    -403.1: Running access not allowed \n    -403.2: Read access is not allowed \n    -403.3: Write access not allowed \n    -403.4: SSL required \n    -403.5: SSL 128 required \n    -403.6: IP address rejected \n    -403.7: Client certificate required \n    -403.8: Access to the site denied \n    -403.9: Too many users \n    -403.10: Invalid configuration \n    -403.11: Change Password \n    -403.12: Access denied to the mapping program \n    -403.13: Client certificate revoked \n    -403.14: Cannot view directory contents \n    -403.15: Exceeded the number of client access licenses \n    -403.16: Untrusted or invalid client certificate \n    -403.17: Client certificate has expired or is not yet valid \n    -403.18: Unable to execute requested URL in current application pool \n    -403.19: Failed to perform CGI requests for the client in this application pool \n    -403.20: Passport login failed \n    -404: Not Found \n    -404.0: File or directory not found \n    -404.1: Website not accessible on the requested port \n    -404.2: Request not allowed by the Web Service Extension Blocking Policy \n    -404.3: Request not allowed by MIME mapping policy \n    -405: Method not allowed \n    -406: The MIME type of the requested page is not accepted by the client browser \n    -407: Proxy authentication required \n    -412: Precondition failed \n    -413: Requested entity too large \n    -414: URI requested too long \n    -415: Media type not supported \n    -416: Unable to comply with requested interval \n    -417: Unable to comply with requested interval \n    -423: File locked error \nServer Error: \n    -500: Internal Server Error \n    -500.12: The application is restarting on the web server \n    -500.13: Web server too busy \n    -500.15: Direct requests for Global.asa are not allowed \n    -500.16: Incorrect UNC authorization credentials \n    -500.18: Unable to open authorization store URL \n    -500.19: The data for the file is configured incorrectly in the metabase \n    -500.100: Internal ASP error \n    -501: The configuration specified by the header values ​​is not implemented \n    -502: The web server acting as a gateway or proxy received an invalid response \n    -502.1: CGI application timeout \n    -500-100.ASP: ASP error \n    -500.12: The application is restarting \n    -502.2: Error in the CGI application \n    -503: Service Unavailable \n    -504: Gateway timeout \n    -505: HTTP version not supported")
		else:
			pass
	except:
		exit()
print(Fore.MAGENTA + "----------------------------------------------------------------------------------")
check()
try:
	while True:
		input2 = input("Do you want to see the status of other sites? [Y/N] > ")
		if input2 == "Y" or input2 == "Yes" or input2 == "YES" or input2 == "y":
			input3 = input("Do you want to clear the terminal? [Y/N] > ")
			if input3 == "Y" or input3 == "y" or input3 == "yes" or input3 == "Yes" or input3 == "YES":
				os.system("clear")
				os.system("figlet CheckSiteStatus")
				print(Fore.MAGENTA + "----------------------------------------------------------------------------------")
				check()
			else:
				check()
		else:
			exit()
except:
	pass
