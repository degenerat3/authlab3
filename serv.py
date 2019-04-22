from flask import Flask, request
from cryptography.fernet import Fernet
import requests
import json
import hashlib
import base64

app = Flask(__name__)
OAUTH_SERV = "http://10.140.100.103:5000/auth"

def dec_pass(ct, key):
    cs = Fernet(key)
    pt = cs.decrypt(bytes(ct.encode()))
    return pt


@app.route('/auth', methods=['GET','POST'])
def authenticate():
    content = request.json
    username = content['username']
    password = content['password']
    key = content['key']
    pt_pass = dec_pass(password, key)
    print("PASSWORD: " + str(pt_pass.decode()))
    encrypted_oauth = oauth_work(username, pt_pass)
    return encrypted_oauth

def oauth_work(username, password):
    tok = get_OA_Tok(username, password)
    if tok == "fail":
        return ""
    print("PT TOK: " + tok)
    hashed = hashlib.sha256(bytes(password)).digest()
    print("LENGTH" + str(len(hashed)))
    key = base64.urlsafe_b64encode(hashed)
    cs = Fernet(key)
    et = cs.encrypt(tok.encode())
    print("ENC TOK: " + et.decode())
    return et


def get_OA_Tok(username, password):
    """
    my_data = {'grant_type': 'client_credentials'}
    r=requests.post(OAUTH_SERV, auth=(username,
        password.decode()), data=my_data)
    print("OAUTH RESPONSE: " + str(r.json()))
    print("REC_TOKEN: " + r.json()['access_token'])
    """
    my_data = {'username':username, 'password':password}
    r=requests.post(OAUTH_SERV, json=my_data)
    print("R CONTENT: " + r.text)
    return r.text#r.json()['access_token']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
