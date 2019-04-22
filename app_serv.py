from flask import Flask, request
from cryptography.fernet import Fernet
import hashlib
import base64

app = Flask(__name__)

def dec_tok(enc_tok):
    print("ENCTOK: " + enc_tok)
    """password = "letmein"
    hashed = hashlib.sha256(bytes(password.encode())).digest()
    key = base64.urlsafe_b64encode(hashed)
    print(len(hashed))"""
    key = b'pwAg6LW_GcnQAPVLkL3MN8AP-LQZwL53n07s7_IGHUE='
    cs = Fernet(key)
    pt = cs.decrypt(bytes(enc_tok.encode()))
    return pt

@app.route('/gimme', methods=['GET','POST'])
def get_tok():
    content = request.json
    enc_tok = content['token']
    hehe = dec_tok(enc_tok)
    print("the decoded: " +hehe.decode())
    return "gottem"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

