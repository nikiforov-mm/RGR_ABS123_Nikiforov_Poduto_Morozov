import numpy as np
import binascii


def gen_binary_key(length, seed=None):
    length = length * 8
    if seed is None:
        seed = np.random.randint(200, 45000)
    state = np.random.RandomState(seed)
    key = state.randint(0, 2, size=length)
    return chr(seed), key.tolist()


def bin_dec(binary):
    return int(binary, 2)

def bin_str_dec(string, base=7):
    r_str = ""
    for ind in range(0, len(string), 7):
        sliced = string[ind:ind+7]
        dec = bin_dec(sliced)
        r_str += chr(dec)
    return r_str

def gen_s_box(seed=None):
    key = [x for x in range(16)]
    if seed is None:
        seed = np.random.randint(200, 45000)
    state = np.random.RandomState(seed)
    state.shuffle(key)
    return chr(seed), key


def xor_str(left, right):
    b_str = ""
    left_len = len(left)
    for ind in range(left_len):
        if left[ind] == right[ind]:
            b_str += "0"
        else:
            b_str += "1"
    return b_str


def string_to_bin(string):
    a_ord = [ord(char) for char in string]
    binary = "".join([format(int, '08b') for int in a_ord])
    return binary


def gost_en(start):
    rounds = 32
    c_r = 0


def gost_de(encrypted, private_key):
    rounds = 32
    c_r = 0


def feistel_en(start):
    rounds = 32
    if len(start) % 2 != 0:
        start += "("
    c_r = 0
    mid = len(start) // 2
    private_key = ""
    l = string_to_bin(start[0:mid])
    r = string_to_bin(start[mid::])
    while c_r < rounds:
        seed, l_key = gen_binary_key(mid)
        str_l_key = "".join(str(integ) for integ in l_key)
        private_key = "{}{}".format(private_key, seed)
        p_r = r
        f = xor_str(r, str_l_key)
        r = xor_str(f, l)
        l = p_r
        c_r += 1
    encrypted = bin_str_dec(l + r)
    return encrypted, private_key


def feistel_de(encrypted, private_key):
    private_key = list(private_key)
    mid = len(encrypted) // 2
    encrypted = string_to_bin(encrypted)
    l = encrypted[0:mid]
    r = encrypted[mid::]
    for char in private_key[::-1]:
        junk, l_key = gen_binary_key(mid, ord(char))
        str_l_key = "".join(str(integ) for integ in l_key)
        p_l = l
        f = xor_str(l, str_l_key)
        l = xor_str(r, f)
        r = p_l
    decrypted = int(l + r, 2)
    decrypted = str(binascii.unhexlify("%x" % decrypted))
    decrypted = decrypted[2:len(decrypted) - 1]
    if decrypted[-1] == "(":
        decrypted = decrypted[0:len(decrypted)-1]
    return decrypted

