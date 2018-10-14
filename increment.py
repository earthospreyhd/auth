from db_query import get_server_nonce, get_server_secret, set_server_secret
from authlib import get_new_secret, get_half_secret, get_combined_secret

def increment(user_nonce, email, devid):
    server_nonce = get_new_secret()
    mutual_increment = get_combined_secret(user_nonce, server_nonce)
    server_secret = get_server_secret()
    new_server_secret = hash256(mutual_increment + server_secret)
    set_server_secret(new_server_secret)

    user_half_increment = get_half_secret(server_nonce)

    return user_half_increment