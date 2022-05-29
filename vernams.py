import random


def vernam_en(string):
    key = ""
    length = len(string)
    encoded_text = ""
    for i in range(length):
        key += chr(random.randrange(1, 65536))
    for num, char in enumerate(string):
        encoded_text += chr(ord(char) ^ ord(key[num]))
    return encoded_text, key


def vernam_de(encrypted, key):
    decoded_text = ""
    for num, char in encrypted:
        decoded_text += chr(ord(char) ^ ord(key[num]))
    return decoded_text