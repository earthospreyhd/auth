from db_query import get_server_nonce
def increment(user_nonce, email, devid):
    server_nonce = get_server_nonce(email, devid)
    mutual_increment = get_combined_secret(user_nonce, server_nonce)
    half_increment = get_half_secret(server_nonce)

    return half_increment