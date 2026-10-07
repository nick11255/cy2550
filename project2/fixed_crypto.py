import os, sys, getpass
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Hash import SHA256

SALT = 16
NONCE = 12
TAG = 16

def derive(pw, salt):
    return PBKDF2(pw, salt, dkLen=32, count=600000, hmac_hash_module=SHA256)

def encrypt_file(infile, outfile, pw):
    data = open(infile, 'rb').read()
    salt = os.urandom(SALT)
    nonce = os.urandom(NONCE)
    c = AES.new(derive(pw, salt), AES.MODE_GCM, nonce=nonce)
    ct, tag = c.encrypt_and_digest(data)
    open(outfile, 'wb').write(salt + nonce + tag + ct)

def decrypt_file(infile, outfile, pw):
    b = open(infile, 'rb').read()
    salt = b[:SALT]
    nonce = b[SALT:SALT+NONCE]
    tag = b[SALT+NONCE:SALT+NONCE+TAG]
    ct = b[SALT+NONCE+TAG:]
    c = AES.new(derive(pw, salt), AES.MODE_GCM, nonce=nonce)
    open(outfile, 'wb').write(c.decrypt_and_verify(ct, tag))

if __name__ == '__main__':
    mode, infile, outfile = sys.argv[1], sys.argv[2], sys.argv[3]
    pw = getpass.getpass("Passphrase: ")
    if mode == 'encrypt':
        encrypt_file(infile, outfile, pw)
        print("encrypted")
    else:
        try:
            decrypt_file(infile, outfile, pw)
            print("decrypted")
        except ValueError:
            print("FAILED: tampered or wrong passphrase")
