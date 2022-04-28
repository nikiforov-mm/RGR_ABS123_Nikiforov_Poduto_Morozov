def encode (text, lenght, count_string, count_colum):
    cipher_text = [None] * lenght
    for i in range(0, lenght):
        index = int(count_string * (i % count_colum) + (i / count_colum))
        cipher_text[index] = text[i]
    cipher_text = "".join(cipher_text)
    print ("Encode: ", cipher_text)

print ("Enter text: ")
text = input ()
lenght = len(text)
print ("Enter key: ")
count_string = int(input())
count_colum = int(((lenght - 1) / count_string) + 1)
encode (text, lenght, count_string, count_colum)
