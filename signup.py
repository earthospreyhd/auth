from authlib import get_combined_secret, get_new_secret, hash256, bytes_to_string
from db_query import get_db, get_new_devID, add_user
import json
import mysql.connector
import email

def signup (email, pin, success):
    user_secret = get_new_secret()
    server_secret = get_new_secret()
    combined_secret = get_combined_secret(user_secret, server_secret)
    user_hash = hash256(combined_secret + pin)
    user_hash = bytes_to_string(user_hash)
    add_user(email, server_secret)

    return user_hash