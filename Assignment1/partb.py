import hashlib
import sys
from subprocess import call

true = True

try:
	while(true):
		data = raw_input()
		m = hashlib.md5(data).hexdigest()
		cmd = ['openssl', 'aes256', '-d', '-a', '-in', '/A1/secret_file.aes256.txt', '-out', 'output.txt', '-k', m]
		decrypted = call(cmd)
		
		for line in open('output.txt'):
			if all(ord(char) > 128 for char in line):
				print("Bad Decryption")
			else:
				print("File Decrypted")
				print("Key is : " + m)
				print("Password is: "+data)
				sys.exit(0)
			
		
except EOFError as e:
	print("end of file reached")

