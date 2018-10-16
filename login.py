from db_query import get_db, get_new_devID, add_user, get_server_secret
from authlib import get_combined_secret, hash256
import json
import mysql.connector
import email

def login (user_half_secret, user_hash, pin, email, devid, user_nonce):
    server_secret = get_server_secret(email, devid)
    combined_secret = get_combined_secret(user_half_secret, server_secret)
    combined_hash = hash256(combined_secret + pin)

    if user_hash == combined_hash:
        login_success = True
    else:
        login_success = False

    return login_success