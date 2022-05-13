#Шифр Вернама является разновидностью криптосистемы одноразовых блокнотов. Основной принцип в создании случайного ключа такой же длины, как шифруемое сообщение. 
import random
def encryption(start): #функция шифрования 
	key =""
	lenght = len(start);
	encoded_text =""
	for i in range(lenght):
		key += chr(random.randrange(1, 65536)) #cоздание случайного ключа
	for i in range(lenght):
		encoded_text += chr (ord(start[i]) ^ ord(key[i]))
	return encoded_text, key
def decryption(encoded_text, key): #функция расшифрования
	decoded_text =""
	lenght = len(encoded_text);
	while 1: 
		if len(key) == lenght:
			for i in range(lenght):
				decoded_text += chr(ord(encoded_text[i]) ^ ord(key[i]))
			return decoded_text

