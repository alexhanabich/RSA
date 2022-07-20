from helper import mod_exp, generate_prime, mult_inv, gcd

def calc_private_key(e, p, q):
    phi = (p-1)*(q-1)
    d = mult_inv(e, phi)
    return d


def encrypt(msg, e, n):
    return mod_exp(msg, e, n)


def decript(msg, d, n):
    return mod_exp(msg, d, n)

class RSA():
    def __init__(self, key_bit=None):
        if key_bit == None:
            self.key_bit = 2048
        else:
            self.key_bit = key_bit
        self.prime_bit = self.key_bit//2
        self.e = 65537


    def generate_keys(self):
        # generate public key n
        p = generate_prime(self.prime_bit)
        q = generate_prime(self.prime_bit)
        # generate primes while gcd(e, phi) != 1
        phi = (p-1)*(q-1)
        while gcd(phi, self.e) != 1:
            p = generate_prime(self.prime_bit)
            q = generate_prime(self.prime_bit)
            phi = (p-1)*(q-1)
        n = p*q
        # calculate private key: d
        phi = (p-1)*(q-1)
        d = mult_inv(self.e, phi)
        return n, d, self.e


    def encrypt(self, msg, e, n):
        return mod_exp(msg, e, n)


    def decript(self, msg, d, n):
        return mod_exp(msg, d, n)


msg = 1234567890
rsa = RSA()
n, d, e = rsa.generate_keys()
cipher = rsa.encrypt(msg, e, n)
print(cipher)
print(decript(cipher, d, n))