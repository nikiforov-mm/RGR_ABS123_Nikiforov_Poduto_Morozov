from copy import deepcopy
import random
from misc import to_matr

shift = 250

def table_shuffling_en(start):
    if "\\" in start:
        return "Cannot be encrypted, avoid using \\ in encryption string", chr(1)
    encoded = ""
    t_string = list(start)
    t_len = len(t_string)
    root_len = int(t_len ** 0.5)
    if root_len ** 2 != t_len:
        root_len += 1
        new_len = root_len ** 2
        shuffle_base = [n for n in range(0, root_len)]
        while len(t_string) < new_len:
            t_string.append("\\")
        t_len = len(t_string)
        shuffle_string = [n for n in range(0, t_len)]
    else:
        shuffle_base = [n for n in range(0, root_len)]
        shuffle_string = [n for n in range(0, t_len)]
    seed_row = random.randint(0, 10 ** 4)
    seed_col = random.randint(0, 10 ** 4)
    seed_str = random.randint(0, 10 ** 4)
    random.Random(seed_str).shuffle(t_string)
    random.Random(seed_str).shuffle(shuffle_string)
    shuffle_row = deepcopy(shuffle_base)
    shuffle_col = deepcopy(shuffle_base)
    random.Random(seed_row).shuffle(shuffle_row)
    random.Random(seed_col).shuffle(shuffle_col)
    matr = to_matr(t_string)
    for ind, row in enumerate(matr):
        t_list = deepcopy(row)
        random.Random(seed_col).shuffle(t_list)
        matr[ind] = t_list
    random.Random(seed_row).shuffle(matr)
    private_key = ""
    for row in matr:
        for elem in row:
            encoded = "{}{}".format(encoded, elem)
    for listed in [shuffle_string, shuffle_col, shuffle_row]:
        for elem in listed:
            private_key = "{}{}".format(private_key, chr(elem + shift))
    return encoded, private_key


def table_shuffling_de(encoded, private_key):
    string = ""
    enc_len = len(encoded)
    col_len = int(enc_len ** 0.5)
    shuffled_string = ""
    unshuffle_list = []
    string_list = []

    shuffle_str = []
    for char in private_key[0:enc_len]:
        shuffle_str.append(ord(char)-shift)

    shuffle_col = []
    for char in private_key[enc_len: enc_len + col_len]:
        shuffle_col.append(ord(char)-shift)

    shuffle_row = []
    for char in private_key[enc_len+col_len:]:
        shuffle_row.append(ord(char)-shift)

    matr = []
    ind_1 = 0
    ind_2 = col_len
    while len(matr) < col_len:
        matr_a = list(encoded[ind_1: ind_2])
        matr.append(matr_a)
        ind_1 += col_len
        ind_2 += col_len

    for row in matr:
        inner_list = []
        for num in range(0, len(shuffle_col)):
            ind = shuffle_col.index(num)
            inner_list.append(row[ind])
        string_list.append(inner_list)
    for num in range(0, len(shuffle_row)):
        ind = shuffle_row.index(num)
        unshuffle_list.append(string_list[ind])
    for row in unshuffle_list:
        for elem in row:
            shuffled_string = "{}{}".format(shuffled_string, elem)
    for num in range(0, len(shuffle_str)):
        ind = shuffle_str.index(num)
        string = "{}{}".format(string, shuffled_string[ind])
    string = string.replace("\\", "")
    return string

