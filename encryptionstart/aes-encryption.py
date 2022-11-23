
import requests
import base64, hashlib
from Crypto.Cipher import AES
from Crypto import Random
import hashlib

#Making GET request and extracting data
url = "https://dummyjson.com/users"
response = requests.get(url)
data = response.json()
users_info = []
for user in data['users']:
	print(user)
	users_info.append({'username': user['firstName'] + " " + user['lastName'], 'password': user['password']})

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

key = "401725002"
def encrypt_func(password):
	iv = Random.new().read(AES.block_size)
	private_key = hashlib.sha256(key.encode("UTF-8")).digest()
	password = pad(password)
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	return base64.b64encode(iv + cipher.encrypt(password))

for user in users_info:
	print(encrypt_func(user['password']))
