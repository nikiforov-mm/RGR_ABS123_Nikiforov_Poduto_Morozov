import random
from misc import is_prime


def pull_prime(lower, upper):
    current_num = random.randint(lower, upper)
    while (not is_prime(current_num)):
        current_num = current_num + current_num % 6
        if (is_prime(current_num + 1)):
            return current_num + 1
        elif (is_prime(current_num - 1)):
            return current_num - 1
        current_num = random.randint(lower, upper)
    return current_num


def have_common_div(a, b):
    ranged = max([a,b])
    for div in range(2, int(ranged ** 0.5)):
        if a % div == 0 and b % div == 0:
            return 1
    return 0


def el_gamal_loop(text):
    p = pull_prime(100, 3000)
    g = random.randint(2, p-1)
    X = random.randint(2, p-1)
    Y = pow(g, X, p)
    k = random.randint(2, p-1)
    while have_common_div(k, p-1):
        k = random.randint(2, p-1)
    encrypted = ""
    for char in text:
        e = chr((ord(char) * pow(Y, k)) % p)
        encrypted += e
    transform = [p, g, k, X]
    key = ""
    for elem in transform:
        key += chr(elem)
    return encrypted, key


def el_gamal_de(enc_text, key):
    p = ord(key[0])
    g = ord(key[1])
    k = ord(key[2])
    X = ord(key[3])
    r = pow(g, k, p)
    decrypted = ""
    for char in enc_text:
        d = chr((ord(char) * pow(r, p - 1 - X)) % p)
        decrypted += d
    return decrypted

# sanity
def el_gamal_en(text):
    encrypted, key = el_gamal_loop(text)
    count = 500
    while (el_gamal_de(encrypted, key) != text and count >= 0):
        encrypted, key = el_gamal_loop(text)
        count -= 1
    if count < 0:
        return "Couldn't encrypt. Check for special symbols, '№' for example", chr(1)
    return encrypted, key
