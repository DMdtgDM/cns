from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os


####

				# AES


# Takes plaintext and a key
# Encrypt it using AES algorithm of The crypthography(the library used)
def aes_e(plaintext, key):
    
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    padded_plaintext = pad(plaintext, AES.block_size)
  
    ciphertext = cipher.encrypt(padded_plaintext)
   
    return iv + ciphertext  

# Takes ciphertext(text which is encrypted) and a key
# decrypt it using AES algorithm of The crypthography(the library used)
def aes_d(ciphertext, key):

	iv = ciphertext[:16]
	actual_ciphertext = ciphertext[16:]
	cipher = AES.new(key, AES.MODE_CBC, iv)

	padded_plaintext = cipher.decrypt(actual_ciphertext)

	# Unpad the decrypted plaintext
	plaintext = unpad(padded_plaintext, AES.block_size)

	return unpad(padded_plaintext, AES.block_size) 

	# AES

###



###

				# 3AES


# Takes plaintext and a key
# Encrypt it using 3DES algorithm of The crypthography(the library used)
def des3_e(plaintext, key):
   
    if isinstance(plaintext, str):
        plaintext = plaintext.encode()
    
    padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    iv = os.urandom(8)  # Generate a random IV
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    return iv + encryptor.update(padded_plaintext) + encryptor.finalize()

# Takes ciphertext(text which is encrypted) and a key
# decrypt it using 3DES algorithm of The crypthography(the library used)
def des3_d(ciphertext, key):

	print(ciphertext) 
	iv = ciphertext[:8]
	cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=default_backend())
	decryptor = cipher.decryptor()

	padded_data = decryptor.update(ciphertext[8:]) + decryptor.finalize()

	unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
	plaintext = unpadder.update(padded_data) + unpadder.finalize()
	return plaintext

	# 3DES

###