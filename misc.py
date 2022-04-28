import random
from copy import deepcopy

forbidden_symbols = " ᬐ΁⯾ꣀ꛰ⱀ⴫⯥" \
                    "­" \
                    "\n " + chr(0)

feistel_symbols = "абвгдеёжзийклмнопрстуфцхчшщьъыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФЦХЧШЩЪЬЫЭЮЯ\\/"

def to_matr(symbols):
    len_root = int(len(symbols) ** 0.5)
    if len_root ** 2 != len(symbols):
        raise ValueError("Unable to form a matrix with {} len string".format(len(symbols)))
    matr = []
    inner = []
    for num, elem in enumerate(symbols):
        if (num % len_root != 0):
            inner.append(elem)
        elif num == 0:
            inner.append(elem)
        else:
            matr.append(inner)
            inner = [elem]
    matr.append(inner)
    return matr

def shuffle_to_matr(symbols, seed=None):
    len_root = int(len(symbols) ** 0.5)
    if len_root ** 2 != len(symbols):
        raise ValueError("Unable to form a matrix with {} len string".format(len(symbols)))

    t_symbols = list(symbols)
    if seed is None:
        seed = random.randint(250, 5000)
        while chr(seed) in forbidden_symbols:
            seed = random.randint(250, 5000)
    random.Random(seed).shuffle(t_symbols)

    matr = []
    inner = []
    for num, elem in enumerate(t_symbols):
        if (num % len_root != 0):
            inner.append(elem)
        elif num == 0:
            inner.append(elem)
        else:
            matr.append(inner)
            inner = [elem]
    matr.append(inner)
    return seed, matr


def find_char_matr(matr, char):
    for ind_r, row in enumerate(matr):
        for ind_c, elem in enumerate(row):
            if elem == char:
                return [ind_r, ind_c]
    raise ValueError("{} char not found".format(char))


def char_pair_matr(matr, char1, char2):
    first = find_char_matr(matr, char1)
    second = find_char_matr(matr, char2)
    return first, second