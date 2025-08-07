import bcrypt

def bcryptHash(string):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(string.encode('utf-8'), salt).decode('utf-8')

def verifyBcryptHash(string, hash):
    return bcrypt.checkpw(string.encode('utf-8'), hash.encode('utf-8'))
