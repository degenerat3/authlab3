from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)


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
	return "nice meme"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
