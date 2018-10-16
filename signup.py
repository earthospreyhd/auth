from authlib import get_combined_secret, get_new_secret, hash256, bytes_to_string, verify_code
from db_query import get_db, get_new_devID, add_user
import json
import mysql.connector
import email
from custom_errors import DataBaseError, CodeError

def signup (email, pin, devid, code, user_half_secret):

    if (verify_code(code, email, devid) == True):
        server_secret = get_new_secret()
        combined_secret = get_combined_secret(user_half_secret, server_secret)
        user_hash = hash256(combined_secret + pin)
        user_hash = bytes_to_string(user_hash)

        try:
            add_user(email, server_secret)
        except Exception:
            raise DataBaseError("an internal error occurred")
    
    else:
        raise CodeError("incorrect code")

    return user_hash