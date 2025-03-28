import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from algo import aes_e, aes_d, des3_e, des3_d
from otp import otp_e, otp_d

app = Flask(__name__)

#This will help to manage headers in Flask applications
CORS(app)


# The following gives route for encrypt 
# takes data from post method by a given front end page
# encrypt using 3 algorithms AES, 3DES and OTP 

@app.route("/encrypt", methods=["POST"])
def encrypt_data():
	
	# takes data from the "POST" method
	# Extract its text, key
	# then change both of them to byte
	# to be an input for encryption algorithm methods
	data = request.get_json()
	text = data["text"].encode('utf-8')
	key_bytes = data["key"].encode('utf-8')

	# Takes data and try to encrypt using AES algo
	# Uses an encryption algorithm from algo.py
	if data["algorithm"] == "AES":
		try:
			encrypted_text = aes_e(text, key_bytes)
		except ValueError as e:
			return jsonify({"e": "ValueError", "error": str(e)})
		except Exception:
			return jsonify({"error": "Unexpected Error"})	

	# Takes data and try to encrypt using 3DES algo
	# Uses an encryption algorithm from algo.py
	elif data["algorithm"] == "3DES":
		try:
			encrypted_text = des3_e(text, key_bytes)
		except ValueError as e:
			return jsonify({"e": "ValueError", "error": str(e)})
		except Exception:
			return jsonify({"error": "Unexpected Error"})	


	# Takes data and try to encrypt using OTP algo
	# Uses an encryption algorithm from otp.py
	elif data["algorithm"] == "OTP":
		try:
			encrypted_text = otp_e(text, key_bytes)
		except Exception:
			return jsonify({"error": "Unexpected Error"})	
	
	# Takes a encrypted data in form of bytes 
	# Then chage it to text(string) format
	# Then send the encrypted data to the front end page for desplay			
	encrypted_text = encrypted_text.decode("latin1")

	return jsonify({"encrypted_text": encrypted_text})


# The following gives route for decrypt 
# takes data from post method by a given front end page
# decrypt using 3 algorithms AES, 3DES and OTP

@app.route("/decrypt", methods=["POST"])
def decrypt_data():

	# takes data from the "POST" method
	# Extract its text, key
	# then change both of them to byte
	# to be an input for decryption algorithm methods
	data = request.get_json()
	text = data["text"].encode('latin1')
	key_bytes = data["key"].encode('utf-8')

	# Takes data and try to decrypt using AES algo
	# Uses a decryption algorithm from algo.py

	if data["algorithm"] == "AES":
		try:
			decrypted_data = aes_d(text, key_bytes)
		except ValueError as e:
			return jsonify({"e": "ValueError", "error": str(e)})
		except Exception:
			return jsonify({"e": "Unexpected Error"})	
		
	# Takes data and try to decrypt using 3DES algo
	# Uses a decryption algorithm from algo.py
	elif data["algorithm"] == "3DES":
		try:
			decrypted_data = des3_d(text, key_bytes)
		except ValueError as e:
			return jsonify({"e": "ValueError", "error": str(e)})
		except Exception:
			return jsonify({"error": "Unexpected Error"})
		
	# Takes data and try to decrypt using OTP algo
	# Uses a decryption algorithm from otp.py
	elif data["algorithm"] == "OTP":
		try:
			decrypted_data = otp_d(text, key_bytes)
		except Exception:
			return jsonify({"error": "Unexpected Error"})
		
	# Takes a decrypted data in form of bytes 
	# Then chage it to text(string) format
	# Then send the decrypted data to the front end page for desplay		
	decrypted_data = decrypted_data.decode("latin1")

	return jsonify({"decrypted_data": decrypted_data})




if __name__ == '__main__':
	app.run()

