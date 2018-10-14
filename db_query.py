import mysql.connector

def get_db():
    db = mysql.connector.connect(
        host = "localhost",
        user = "zach",
        passwd = "zach",
        database = "auth_db",
    )

    return db

# def add_user(email, inc, dblink, devID):
#     query = "INSERT INTO user_secrets VALUES(%s, %s, %s)"
#     values = email, devID, inc
#     dblink.execute(query, values)

def add_user(email, server_secret):
    db = get_db()
    dblink = db.cursor()

    devID = get_new_devID(email, dblink)
    query = "INSERT INTO user_secrets VALUES(%s, %s, %s)"
    values = email, devID, server_secret
    dblink.execute(query, values)

def get_new_devID (email, dblink):
    query = "SELECT ID FROM user_secrets WHERE Email=%s"
    values = email,
    dblink.execute(query, values)
    devID = dblink.fetchall()
    if devID == []:
        devID = 0
    else:
        devID = max(devID)
        devID = devID[0] + 1

    return devID

def set_devID (email, dblink, devID):
    query = "UPDATE user_secrets SET devID = %s WHERE Email=%s"
    values = devID, email
    dblink.execute(query, values)

def get_server_secret(email, devID):
    db = get_db()
    dblink = db.cursor()
    query = "SELECT Secret FROM user_secrets WHERE Email=%s AND ID=%s"
    values = email, devID
    dblink.execute(query, values)
    inc = dblink.fetchall()
    inc = int(inc[0][0])

    return inc
def set_server_secret(email, devID, secret):
    db = get_db()
    dblink = db.cursor()
    query = "UPDATE user_secrets SET Secret= %s WHERE Email=%s AND ID=%s"
    values = secret, email, devID
    dblink.execute(query, values)

# def set_server_secret(email, dblink, devID, inc):
#     query = "UPDATE user_secrets SET Secret= %s WHERE Email=%s AND ID=%s"
#     values = inc, email, devID
#     dblink.execute(query, values)

# def increment (email, dblink, devID):
#     inc = get_inc(email, dblink,devID)
#     inc += 1
#     set_inc(email, dblink, devID, inc)

def user_exists(email, dblink, devID):
    query = "SELECT * FROM user_secrets WHERE Email=%s AND ID=%s"
    values = email, devID
    dblink.execute(query, values)
    result = dblink.fetchall()
    if result == []:
        return False
    else:
        return True