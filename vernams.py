import random


def vernam_loop(string):
    key = ""
    length = len(string)
    encrypted = ""
    for i in range(length):
        key += chr(random.randrange(1, 6000))
    for num, char in enumerate(string):
        encrypted += chr(ord(char) ^ ord(key[num]))
    return encrypted, key


def vernam_de(encrypted, key):
    decrypted = ""
    for num, char in enumerate(encrypted):
        decrypted += chr(ord(char) ^ ord(key[num]))
    return decrypted

# sanity
def vernam_en(string):
    flag = 0
    while 1:
        try:
            encrypted, key = vernam_loop(string)
            decrypted = vernam_de(encrypted, key)
            if decrypted == string:
                flag = 1
        except:
            pass
        if flag:
            return encrypted, key