from flask import Flask, request
from cryptography.fernet import Fernet
import requests
import json
import hashlib

app = Flask(__name__)
OAUTH_SERV = "http://127.0.0.1/endpoint"

def dec_pass(ct, key):
    cs = Fernet(bytes(key))
    pt = cs.decrypt(bytes(ct))
    return pt


@app.route('/auth', methods=['GET','POST'])
def authenticate():
    content = request.json
    user = content['username']
    password = content['password']
    key = content['key']
    pt_pass = dec_pass(password, key)
    print(pt_pass)
    encrypted_oath = oauth_work(username, password)
    return encrypted_oauth

def oauth_work(username, password):
    tok = get_OA_Tok(username, password)
    hashed = hashlib.sha256(bytes(password)).digest()
    cs = Fernet(bytes(hashed))
    et = cs.encrypt(bytes(tok))
    return et


def get_OA_Tok(username, password):
    cont = json.dumps({'username': username, 'password': password})
    r=requests.post(OAUTH_SERV, data=cont, headers={'Content-Type': 'application/json'})
    print(r.content)
    return "success or failure data"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
