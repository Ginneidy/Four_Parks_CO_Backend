import hashlib

# Function for user password hashing
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()
