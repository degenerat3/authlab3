import requests
from cryptography.fernet import Fernet

username = input("Username: ")
password = input("Password: ")
#password = password.rjust(16, '0')
key = Fernet.generate_key()
#print(type(key))
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(password.encode())
r = requests.post('http://10.150.101.40:5000/auth', json={"username": username, "password": cipher_text, "key": key})
