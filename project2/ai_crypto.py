from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    with open(output_file, 'wb') as f:
        f.write(ciphertext)

key = b'1234567890123456'
encrypt_file('input.txt', 'encrypted.bin', key)
