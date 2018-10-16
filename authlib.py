import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from prime_modulus import PRIME_MODULUS, GENERATOR

SECRET = 23487230598734098570934875

def get_half_secret(secret):
    half_secret = pow(GENERATOR, secret, PRIME_MODULUS)

    return half_secret

def new_combined_secret (user_secret, server_secret):
    combined_secret = pow(GENERATOR, user_secret * server_secret, PRIME_MODULUS)

    return combined_secret

def get_combined_secret(user_half, server_secret):
    combined_secret = pow(user_half, server_secret, PRIME_MODULUS)

    return combined_secret

def get_new_secret ():
    new_secret = os.urandom(16)
    new_secret = int.from_bytes(new_secret, byteorder="big")

    return new_secret

def hash256(text):
    text = text.encode("utf-8")
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(text)
    key = digest.finalize()

    return key

def gen_code (user_email, devID):
    code = hash256(str(SECRET) + user_email + str(devID))
    code = bytes_to_string(code)

    return code

def verify_code(user_code, user_email, devID):
    code = hash256(str(SECRET) + user_email + str(devID))
    code = bytes_to_string(code)

    if user_code == code:
        return True

    else:
        return False

def bytes_to_string(bytes_data):
    string = int.from_bytes(bytes_data, byteorder="big")
    string = str(string)

    return string

def string_to_bytes(string):
    bytes_data = int(string)
    bytes_data = bytes_data.to_bytes((bytes_data.bit_length() + 7) // 8, byteorder="big")

    return bytes_data