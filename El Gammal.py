import random
def is_prime(n):
  if n%2 == 0: return False
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True 

def have_common_div(a, b):
    ranged = max([a,b])
    for div in range(2, int(ranged ** 0.5)):
        if a % div == 0 and b % div == 0:
            return 1
    return 0
def encode(text):
    primes = []
    for i in range(100, 10000):
        if (is_prime(i) == True):
            primes.append(i)
    primes.sort()
    g = random.randint(0, 100)
    p = primes[random.randint(0, 722)]
    X = random.randint(1, p-1)
    Y = pow(g, X, p)
    k = 0
    while have_common_div(k, p-1):
        k = random.randint(1, p-1)
    enc_text = []
    for char in text:
        e_modless = ord(char) * pow(Y, k)
        e = e_modless % p
        enc_text.append(e)
    return enc_text, p, g, k, X
def decode(enc_text, p, g, k, X):
    r = pow(g, k, p)
    dec_text = ""
    for element in enc_text:
        modless = element * pow(r,p-1-X)
        m_s = modless % p
        dec_text = "{}{}".format(dec_text, chr(m_s))
    return dec_text
