import os
import requests
from cryptography.fernet import Fernet
import hashlib
import base64

def dec_tok(tok, password):
    hashed = hashlib.sha256(password.encode()).digest()
    print("LENGTH" + str(len(hashed)))
    key = base64.urlsafe_b64encode(hashed)
    cs = Fernet(key)
    et = cs.decrypt(tok)
    print("DEC TOK: " + et.decode())
    return et

ip = os.environ.get("auth_serv")
username = input("Username: ")
password = input("Password: ")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(password.encode())
r = requests.post('http://'+ip+':5000/auth', json={"username": username, "password": cipher_text, "key": key})
token = r.content
print(token)
if not token:
	print("Empty token lmao")
	exit()
pt_tok = dec_tok(token, password)

app = os.environ.get("app_serv")
nr = requests.post('http://'+app+':5000/gimme', json={"token": pt_tok})
print(nr.status_code)

