import requests
from cryptography.fernet import Fernet

ip = input("IP Address of Authentication Server: ")
username = input("Username: ")
password = input("Password: ")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(password.encode())
r = requests.post('http://'+ip+':5000/auth', json={"username": username, "password": cipher_text, "key": key})
