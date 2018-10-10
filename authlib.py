import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from prime_modulus import PRIME_MODULUS

class cookie ():

    def __init__(self):
        self.user_hash = None
        self.user_secret = None

    def set_user_hash (self, user_hash):
        self.user_hash = user_hash

    def get_user_hash (self): 
        return self.user_hash

    def set_user_hash (self, user_hash):
        self.user_hash = user_hash

    def get_user_hash (self): 
        return self.user_hash


def gen_combined_secret ():
    combined_secret = pow(2, user_secret * server_secret, PRIME_MODULUS)

    return combined_secret

def get_new_secret ():
    new_secret = os.urandom(16)

    return new_secret

def authenticate(user_cookie, pin, email, devID, inc):
    key = hash256(str(SECRET) + str(pin) + str(devID) + str(inc))
    body = string_to_bytes(user_cookie.get_body())
    iv = string_to_bytes(user_cookie.get_iv())
    try:
        cookie_email = aes_decrypt(body, iv, key)
    except:
        return False

    if email == cookie_email:
        return True
    else:
        return False

def aes_encrypt (content, key, iv):
    content = content.encode("utf-8")
    content = pad_data(content, 128)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(content) + encryptor.finalize()
    ciphertext = bytes_to_string(ciphertext)

    return ciphertext

def aes_decrypt(body, iv, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
    decryptor = cipher.decryptor()
    user_email = decryptor.update(body) + decryptor.finalize()
    user_email = unpad_data(user_email, 128)
    user_email = user_email.decode("utf-8")

    return user_email

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

def verify_code(content, user_email, devID):
    code = hash256(str(SECRET) + user_email + str(devID))
    code = bytes_to_string(code)

    if content == code:
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

def pad_data (data, byte_size):
    padder = padding.PKCS7(byte_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    return padded_data

def unpad_data (padded_data, byte_size):
    unpadder = padding.PKCS7(byte_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data