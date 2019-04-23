# Pre-req
# PHP OAUTH server listening on localhost:80
# Guide: https://bshaffer.github.io/oauth2-server-php-docs/cookbook/
#
from flask import Flask, request
from cryptography.fernet import Fernet
import requests
import hashlib
import base64

app = Flask(__name__)
OAUTH_SERV = "http://localhost/token.php"

@app.route("/auth", methods=['POST'])
def authenticate():
	content = request.json
	username = content['username']
	password = content['password']
	r = requests.post(OAUTH_SERV, auth=(username, password), data={'grant_type': 'client_credentials'})
	if 'access_token' not in r.json():
		print('[!] OAuth failed to generate token')
		return 'fail'
	tok = r.json()['access_token']
	print('PT TOKEN: ' + str(tok))
	
	# encrypt
	#pass2 = 'letmein'
	#hashed = hashlib.sha256(bytes(pass2.encode())).digest()
	#print(type(hashed))
	#key = base64.urlsafe_b64encode(hashed)
	key = b'pwAg6LW_GcnQAPVLkL3MN8AP-LQZwL53n07s7_IGHUE='
	cs = Fernet(key)
	et = cs.encrypt(tok.encode())
	print('SECRET ENC TOK: ' + et.decode())

	return et

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

