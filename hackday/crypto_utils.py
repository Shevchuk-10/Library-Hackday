from cryptography.fernet import Fernet

def encrypt(data: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(data.encode())

def decrypt(token: bytes, key: bytes) -> str:
    return Fernet(key).decrypt(token).decode()

def generate_key() -> bytes:
    return Fernet.generate_key()
