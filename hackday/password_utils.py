import hashlib

def hash_password(password: str, algo: str = 'sha256') -> str:
    h = hashlib.new(algo)
    h.update(password.encode())
    return h.hexdigest()
