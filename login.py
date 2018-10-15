from db_query import get_db, get_new_devID, add_user, get_server_secret
from authlib import get_combined_secret, hash256
import json
import mysql.connector
import email

def login (user_secret, user_hash, pin, email, devid, user_nonce):
    login_success = False
    server_secret = get_server_secret(email, devid)
    combined_secret = get_combined_secret(user_secret, server_secret)
    combined_hash = hash256(combined_secret + pin)

    if user_hash == combined_hash:
        login_success = True

    return login_success