from cryptography.fernet import Fernet
import os

file_name = "encryption_key.txt"
file_path = os.getcwd()
extend = "\\Cryptography\\"
file_merge = file_path + extend + file_name

encryted_key = Fernet.generate_key()

file = open(file_merge, "wb")
file.write(key)
file.close()