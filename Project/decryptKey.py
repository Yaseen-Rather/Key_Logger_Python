from cryptography.fernet import Fernet
import os

#Base dir

base_dir = os.path.join(os.getcwd(), "Project")

#Encrypted data

enc_dir = os.path.join(base_dir, "Encrypted")

#Decrypted data dir

dyc_dir = os.path.join(base_dir, "Decrypted")
os.makedirs(dyc_dir, exist_ok=True)

#key path

key_path = os.path.join(os.getcwd(), "Cryptography", "encryption_key.txt")

#key

with open(key_path, "rb") as f:
    key = f.read()

fernet = Fernet(key)

files_to_decrypt = [("e_key_information.txt", "key_info.txt"), ("e_system_info.txt", "system_info.txt"), ("e_clipboard.txt", "clipboard.txt")]

for enc_name, dyc_name in files_to_decrypt:
    enc_path = os.path.join(enc_dir, enc_name)
    dyc_path = os.path.join(dyc_dir, dyc_name)

    if not os.path.exists(enc_path):
        print("Missing File !: {enc_name}")
        continue

    with open(enc_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(dyc_path, "wb") as f:
        f.write(decrypted_data)

    print(f"[+] Decrypted: {dyc_name}")

print("Decryption Done!!!")

