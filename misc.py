import random
from copy import deepcopy

forbidden_symbols = " ᬐ΁⯾ꣀ꛰ⱀ⴫⯥" \
                    "­№" \
                    "\n " + chr(0)

feistel_symbols = "абвгдеёжзийклмнопрстуфцхчшщьъыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФЦХЧШЩЪЬЫЭЮЯ\\/"

infos = [# Gronsfield
         "Gronsfield is a variation of Caesar's cypher.\n" + \
         "Restriction: Using characters with ord() value at 64600+ might cause an error when encrypting.",
         # Playfair
         "Playfair's cypher uses table of a certain alphabet.\n" + \
         "This program uses:\n" + \
         "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRSTVUWXYZ1234567890+-/=_@<>~`,.?!:;'\"\\[{}" + \
         "()-+абвгдеёжзийклмнопрстуфцхчшщъьыэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФЦХЧШЩЪЬЫЭЮЯ\\n\\t\\v$№êéèçæåäãâ \"\n" + \
         "All other characters are prohibited.",
         # Table shuffle
         "Table shuffle uses indices.\n" + \
         "Programm makes sure to have a square matrix therefore it adds '\\' symbols to input string until the requirement is met.\n" + \
         "Cypher doesn't have any restrictions.",
         # El Gamal
         "Uses big numbers and remainders of its divisions.\nAvoid using № and other special characters for encryption",
         # Scytale
         "Scytale cypher shuffles input string in a special manner.\n" + \
         "Cypher doesn't have any restrictions.",
         # Vernam
         "Vernam's cypher uses bitwise \"xor\" for encryption of input string." + \
         "Cypher doesn't have any restrictions."]

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


def is_prime(num):
    for div in range(2, round(num ** 0.5)):
        if num % div == 0:
            return 0
    return 1