from Crypto.Util import number
from fast_mod_exp.fastmodexp import mod_exp


# based on the theorm that gcd(a,b) = gcd(b,a%b)
def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a


# if xa + yb = 1
# then xa = 1 mod b (mod b removes all multiples of b)
# then x = a^(-1) mod b
# using an adaptation of egcd
def mult_inv(a, n):
    t, newt = 0 ,1
    r, newr = n, a
    while newr != 0:
        q = r//newr
        t, newt = newt, t-q*newt
        r, newr = newr, r-q*newr
    if r > 1:
        raise Exception('not invertible')
    return t%n

def generate():
    len_bit = 512
    e = 65537
    while True:
        p = number.getPrime(len_bit)
        q = number.getPrime(len_bit)
        phi = (p-1)*(q-1)
        if p >> (len_bit-1) == 1 and q >> (len_bit-1) == 1:
            if gcd(phi, e) == 1:
                break
    n = p*q
    phi = (p-1)*(q-1)
    d = mult_inv(e, phi)
    return p, q, n, phi, d



p, q, n, phi, d = generate()
e = 65537
def encrypt(message):
    return mod_exp(message, e, n)


def decript(message, d):
    return mod_exp(message, d, n)



message = 1234567890
cipher = encrypt(message)
print(cipher)
print(decript(cipher, d))
