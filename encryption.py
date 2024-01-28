# encryption.py
from Crypto.Util.number import bytes_to_long

def encrypt(n, e, message):
    return pow(bytes_to_long(message.encode()), e, n)

if __name__ == "__main__":
    message = input("Enter the Text to Encrypt: ")
    key_n = int(input("Enter the public key 'n': "))
    key_e = int(input("Enter the public key 'e': "))

    encrypted = encrypt(key_n, key_e, message)
    print(f"Encrypted Message: {encrypted}")