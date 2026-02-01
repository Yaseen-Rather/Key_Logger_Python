from cryptography.fernet import Fernet
import os

file_name = "encryption_key.txt"
file_merge = os.path.join(os.getcwd(), "Project")

key = Fernet.generate_key()

file = open(file_merge, "wb")
file.write(key)
file.close()