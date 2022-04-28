import random
from misc import forbidden_symbols

def perfect_gronsfield_en(start):
    private_key = ""
    encrypted = ""
    max_seed = len(start)
    for s_char in start:
        seed = int(random.randint(200, 900))
        while chr(seed) in forbidden_symbols:
            seed = int(random.randint(200, 900))
        key_iter = chr(seed)
        crypt_char = chr(ord(s_char)+ord(key_iter))
        private_key = "{}{}".format(private_key, key_iter)
        encrypted = "{}{}".format(encrypted, crypt_char)
    return encrypted, private_key


def perfect_gronsfield_de(encrypted, private_key):
    original = ""
    for ind, crypt_char in enumerate(encrypted):
        traceback = ord(private_key[ind])
        original = "{}{}".format(original, chr(ord(crypt_char)-traceback))
    return original


def a_basic_en(private_key):
    public_key = ""
    count = 0
    for elem in private_key:
        public_key = "{}{}".format(public_key, chr(ord(elem) + count))
        count += 1
    return public_key


def a_basic_de(public_key):
    private_key = ""
    count = 0
    for elem in public_key:
        private_key = "{}{}".format(private_key, chr(ord(elem) - count))
        count += 1
    return public_key

def d_asym_perfect_gronsfield(encrypted, public_key):
    private_key = a_basic_de(public_key)
    res = perfect_ceasar_de(encrypted, private_key)
    return res
