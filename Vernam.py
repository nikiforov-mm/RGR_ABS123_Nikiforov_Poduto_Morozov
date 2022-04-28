import random
def encryption(text, lenght):
	key =""
	encode =""
	for i in range(lenght):
		key += chr(random.randrange(97, 97+26))
	for i in range(lenght):
		encode += chr (ord(text[i]) ^ ord(key[i]))
	print ("Key: ", key)
	print ("Encrypted text:", encode)
def decryption(text, lenght):
	print ("Enter key:")
	key = input()
	decode =""
	ntry = 1
	while ntry < 10: 
		key = input ()
		if len(key) == lenght:
			for i in range(lenght):
				decode += chr(ord(text[i]) ^ ord(key[i]))
			print ("Decrypted text:", decode)
			break
		else:
			print ("Invalid key, try again")
			ntry = ntry + 1
print("Enter text:")
text = ""
text = input ()
lenght = len(text);
print ("To encrypt - press 1, to decrypt - press 0")
button = int(input ())
if button == int("1"):
	encryption(text, lenght)
if button == int("0"):
	decryption(text, lenght)
	