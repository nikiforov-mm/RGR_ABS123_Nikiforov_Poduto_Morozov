import random
from misc import is_prime


def scytale_en(start):
    length = len(start)
    count = random.randint(2, round(length**0.5))
    while (is_prime(length)):
        length += 1
        start += " "
    while length % count != 0:
        count = random.randint(2, round(length**0.5))
    encrypted = [None for x in range(0, length)]
    cols = int(((length - 1) / count) + 1)
    for i in range(0, length):
        index = int(count * (i % cols) + (i / cols))
        encrypted[index] = start[i]
    encrypted = "".join(encrypted)
    return encrypted, chr(count)


def scytale_de(encrypted_text, count):
    count = ord(count)
    length = len(encrypted_text)
    cols = int(((length - 1) / count) + 1)
    decrypted = [None for x in range(0, length)]
    for i in range (0, length):
        index = int(cols * (i % count) + (i / count))
        decrypted[index] = encrypted_text[i]
    decrypted = "".join(decrypted)
    return decrypted
