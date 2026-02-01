# Educational Keylogger with Encryption (Python)

> ⚠️ **DISCLAIMER**  
> This project is strictly for **educational purposes only**.  
> It is intended to demonstrate how keylogging, encryption, and system data collection work in a controlled environment.  
> **Do NOT use this project for illegal, unethical, or malicious activities.**


## 📌 Project Overview

This is a **terminal-based educational keylogger** written in Python.  
The program logs keyboard input **only while the script is running**, gathers basic system information and clipboard data, and then **encrypts all collected data** before exiting.

The keylogger:
- Runs only when executed manually
- Stops safely when the **ESC key** is pressed
- Does not run in the background
- Does not persist after execution

A separate decryption script is provided to view encrypted data for learning purposes.



## 🧠 Learning Objectives

This project helped in understanding:
- Keyboard event handling using `pynput`
- Clipboard access using `pywin32`
- System information gathering
- File handling in Python
- Symmetric encryption using `cryptography (Fernet)`
- Secure key generation and reuse
- Basic project structuring



## 📂 Project Structure

├── Cryptography/
│ ├── generateKey.py
│ └── encryption_key.txt
|
├── Project/
|
├── keylogger.py
├── decryptKey.py
├── requirements.txt
|
│ ├── Plain_Text/
│ │ ├── key_log.txt
│ │ ├── system_info.txt
│ │ └── clipboard.txt
│ ├── Encrypted/
│ │ ├── e_key_information.txt
│ │ ├── e_system_info.txt
│ │ └── e_clipboard.txt
│ └── Decrypted/

## 🔐 Encryption Details

- Uses **Fernet symmetric encryption (AES-based)**
- Encryption key is:
  - Generated once
  - Stored in `Cryptography/encryption_key.txt`
- The same key is used for encryption and decryption


## ▶️ How to Run

- open terminal
- navigate to the directory where the Program is installed (eg: C:\Downloads\Key_Logger_Python)
-pip install -r requirements.txt
- run the command
	python -m Project.keylogger
-if you have enabled the email feature enables first enter 
	1. Sender's Email
	2. App specific password
	3. Enter Recivers address
**Use the program for educational purposes only


🚫 Email Feature

An email-sending feature exists in the code but is commented out.
It was excluded from execution due to reliability issues and is not required for the learning goals of this project.

🛡️ Ethical Notice

This project:

Does not hide itself

Does not auto-start

Does not persist on the system

Requires manual execution

It is intended for cybersecurity education and defensive awareness only.





