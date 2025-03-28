import os

def simple_hash(data):
    hash_value = 0
    for char in data:
        hash_value = (hash_value * 31 + ord(char)) % 256  # Limit to byte range
    return hash_value

def generate_otp(secret, counter):
    combined = secret + str(counter)
    otp = simple_hash(combined)
    return otp

def otp_e(message, secret, counter=10):
    secret = secret.decode()
    message = message.decode()
    otp = generate_otp(secret, counter)
    ciphertext = ''.join(chr((ord(char) + otp) % 256) for char in message)
    return ciphertext.encode()

def otp_d(ciphertext, secret, counter=10):
    ciphertext = ciphertext.decode()
    secret = secret.decode()
    otp = generate_otp(secret, counter)
    plaintext = ''.join(chr((ord(char) - otp) % 256) for char in ciphertext)
    return plaintext.encode()
