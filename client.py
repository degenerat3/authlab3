import os
import requests
from cryptography.fernet import Fernet

ip = os.environ.get("auth_serv")
username = input("Username: ")
password = input("Password: ")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(password.encode())
r = requests.post('http://'+ip+':5000/auth', json={"username": username, "password": cipher_text, "key": key})
token = r.content

app = os.environ.get("app_serv")
nr = requests.post('http://'+app+':5000/gimme', json={"password": password, "token": token})
print(nr.status_code)
