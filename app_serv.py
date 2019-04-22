from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

def dec_tok(enc_tok, password)
    cs = Fernet(bytes(password)
    pt = cs.decrypt(bytes(enc_tok))
    return pt

@app.route('/gimme', methods=['GET',['POST'])
def get_tok():
    content = request.json
    enc_tok = content['token']
    password = content['password']
    dec_tok(enc_tok, password)
    print(dec_tok)_
    return "gottem"
