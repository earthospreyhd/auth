from auth.authlib import new_cookie
from auth.db_query import get_db, get_new_devID, add_user
import json
import mysql.connector
import email

def signup (email, pin):
    user_secret = get_new_secret()
    server_secret = get_new_secret()
    combined_secret = gen_combined_secret(user_secret, server_secret)
    user_hash = hash256(combined_secret + pin)
    user_hash = bytes_to_int(user_hash)
    # breaks abstraction?
    db = get_db
    dblink = db.cursor()
    add_user(email, server_secret, devID, dblink)

    # email.send_email(,email)
    return user_hash