import random
from misc import shuffle_to_matr, to_matr, char_pair_matr
from copy import deepcopy

symbols = "abcdefghijklmnopqrstvuwxyzABCDEFGHIJKLMNOPQRSTVUWXYZ1234567890+-/=_@<>~`,.?!:;'\"\\[{}()-+абвгдеёжзийклмнопрстуфцхчшщъьыэюя" + \
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФЦХЧШЩЪЬЫЭЮЯ\n\t\v$№êéèçæåäãâ "
row_len= int(len(symbols) ** 0.5)

def playfair_conditions(fli, sli):
    same_col = fli[1] == sli[1]
    same_row = fli[0] == sli[0]
    lir1 = fli[0] == (row_len - 1)
    lir2 = sli[0] == (row_len - 1)
    lic1 = fli[1] == (row_len - 1)
    lic2 = sli[1] == (row_len - 1)
    fir1 = fli[0] == 0
    fir2 = sli[0] == 0
    fic1 = fli[1] == 0
    fic2 = sli[1] == 0
    return same_col, same_row, lir1, lir2, lic1, lic2, fir1, fir2, fic1, fic2


def consec_dupes(string):
    t_string = deepcopy(string)
    for symb in symbols:
        if symb + symb in string:
            t_string = t_string.replace(symb+symb, symb + "X")
    return t_string


def form_bigramm_no_loss(matr, fli, sli):
    sc, sr, lir1, lir2, lic1, lic2, fir1, fir2, fic1, fic2 = playfair_conditions(fli, sli)
    if sr and sc:
        pair = "{}]".format(matr[fli[0]][fli[1]])
    elif sr and not sc:
        if lic1:
            pair = "{}{}".format(matr[fli[0]][0], matr[sli[0]][sli[1]+1])
        elif lic2:
            pair = "{}{}".format(matr[fli[0]][fli[1]+1], matr[sli[0]][0])
        else:
            pair = "{}{}".format(matr[fli[0]][fli[1]+1], matr[sli[0]][sli[1]+1])
    elif not sr and sc:
        if lir1:
            pair = "{}{}".format(matr[0][fli[1]], matr[sli[0]+1][sli[1]])
        elif lir2:
            pair = "{}{}".format(matr[fli[0]+1][fli[1]], matr[0][sli[1]])
        else:
            pair = "{}{}".format(matr[fli[0]+1][fli[1]], matr[sli[0]+1][sli[1]])
    else:
        flag = 0
        if sli[1] < fli[1]:
            flag = 1
        col_diff = abs(sli[1] - fli[1])
        if not flag:
            pair = "{}{}".format(matr[fli[0]][fli[1] + col_diff], matr[sli[0]][sli[1] - col_diff])
        else:
            pair = "{}{}".format(matr[fli[0]][fli[1] - col_diff], matr[sli[0]][sli[1] + col_diff])
    return pair


def unform_bigramm_no_loss(matr, fli, sli):
    try:
        sc, sr, lir1, lir2, lic1, lic2, fir1, fir2, fic1, fic2 = playfair_conditions(fli, sli)
        if sr and not sc:
            if fic1:
                pair = "{}{}".format(matr[fli[0]][-1], matr[sli[0]][sli[1]-1])
            elif fic2:
                pair = "{}{}".format(matr[fli[0]][fli[1]-1], matr[sli[0]][-1])
            else:
                pair = "{}{}".format(matr[fli[0]][fli[1]-1], matr[sli[0]][sli[1]-1])
        elif not sr and sc:
            if fir1:
                pair = "{}{}".format(matr[-1][fli[1]], matr[sli[0]-1][sli[1]])
            elif fir2:
                pair = "{}{}".format(matr[fli[0]-1][fli[1]], matr[-1][sli[1]])
            else:
                pair = "{}{}".format(matr[fli[0]-1][fli[1]], matr[sli[0]-1][sli[1]])
        else:
            flag = 0
            if sli[1] < fli[1]:
                flag = 1
            col_diff = abs(sli[1] - fli[1])
            if not flag:
                pair = "{}{}".format(matr[fli[0]][fli[1] + col_diff], matr[sli[0]][sli[1] - col_diff])
            else:
                pair = "{}{}".format(matr[fli[0]][fli[1] - col_diff], matr[sli[0]][sli[1] + col_diff])
        return pair
    except:
        pair = "{}{}".format(matr[fli[0]][fli[1]], matr[fli[0]][fli[1]])
        return pair

def playfair_no_loss_en(string, key=None):
    t_string = deepcopy(string)
    private_key = ""
    encrypted = ""
    t_len = len(t_string)
    if t_len % 2 != 0:
        ind_app = int(random.uniform(0, 144))
        t_string = "{}{}".format(t_string, symbols[ind_app])
        t_len += 1
    for ind in range(0, int(t_len/2)):
        if key is not None:
            seed = ord(key[ind])
            junk, matr = shuffle_to_matr(symbols, seed)
        else:
            seed, matr = shuffle_to_matr(symbols)
        private_key = "{}{}".format(private_key, chr(seed))
        fli, sli = char_pair_matr(matr, t_string[ind * 2], t_string[ind * 2 + 1])
        bigramm = form_bigramm_no_loss(matr, fli, sli)
        encrypted = "{}{}".format(encrypted, bigramm)
    ## pepehands . Костыль
    if playfair_no_loss_de(encrypted, private_key) != string:
        encrypted, private_key = playfair_no_loss_en(string)
    return encrypted, private_key


def playfair_no_loss_de(encrypted, private_key):
    decrypted = ""
    t_string = deepcopy(encrypted)
    t_len = len(t_string)
    for ind in range(0, int(t_len/2)):
        seed = ord(private_key[ind])
        seed, matr = shuffle_to_matr(symbols, seed)
        fli, sli = char_pair_matr(matr, t_string[ind * 2], t_string[ind * 2 + 1])
        unformed = unform_bigramm_no_loss(matr, fli, sli)
        decrypted = "{}{}".format(decrypted, unformed)
    return decrypted

