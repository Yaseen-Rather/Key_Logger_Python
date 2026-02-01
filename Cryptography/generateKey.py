from cryptography.fernet import Fernet
import os

key_dir = os.path.join(os.getcwd(), "Cryptography")
key_path = os.path.join(key_dir, "encryption_key.txt")

def get_or_create_key():
    os.makedirs(key_dir, exist_ok = True)

    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as f:
            f.write(key)
        return key
    else:
        with open(key_path, "rb") as f:
            return f.read()
