def encode (start):
    lenght = len(start)
    encrypted_text = [None] * lenght
    print ("Enter key: ")
    count_string = int(input())
    count_colum = int(((lenght - 1) / count_string) + 1)    
    for i in range(0, lenght):
        index = int(count_string * (i % count_colum) + (i / count_colum))
        encrypted_text[index] =start[i]
    encrypted_text = "".join(encrypted_text)
    return encrypted_text, count_string
def decode (encrypted_text, count_string):
    lenght = len(encrypted_text)
    count_colum = int(((lenght - 1) / count_string) + 1) 
    decrypted_text = [None] * lenght
    for i in range (0, lenght):
        index = int(count_colum * (i % count_string) + (i / count_string))
        decrypted_text[index] = encrypted_text[i]
    decrypted_text = "".join(decrypted_text)
    return decrypted_text
