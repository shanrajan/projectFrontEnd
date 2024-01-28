# key_generation.py
import random

from Crypto.Util.number import getPrime



from prime_time import microseconds_part


class KeyPair:
    def __init__(self, n, e, d):
        self.n = n
        self.e = e
        self.d = d

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_keys():
    p = getPrime(128)
    q = getPrime(128)
    r = microseconds_part

    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    e = random.randrange(2, phi)
    while gcd(phi, e) != 1:
        e = random.randrange(2, phi)
    d = pow(e, -1, phi)
    return KeyPair(n, e, d)

if __name__ == "__main__":
    kp = generate_keys()
    PublicKey= {kp.n}, {kp.e}
    PrivateKey= {kp.n}, {kp.d}