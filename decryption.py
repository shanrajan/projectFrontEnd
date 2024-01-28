# decryption.py
from Crypto.Util.number import long_to_bytes

def decrypt(n, d, encrypted):
    return long_to_bytes(pow(encrypted, d, n)).decode()

if __name__ == "__main__":
    encrypted = int(input("Enter the Encrypted Message: "))
    key_n = int(input("Enter the private/public key 'n': "))
    key_d = int(input("Enter the private key 'd': "))

    decrypted = decrypt(key_n, key_d, encrypted)
    print(f"Decrypted Message: {decrypted}")