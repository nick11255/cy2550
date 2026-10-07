# Project 2: Cryptography

## Part 1

### 1.1
-pbkdf2 turns a passphrase into a 256-bit AES key by combining the passphrase with a random salt and applying HMAC-SHA256 many times.
-A passphrase requires this  because AES needs a fixed-size high-entropy key and a passphrase is neither, so the iterations make brute force cost a lot of time.
### 1.2
-'salt' generates a new random salt each run, so that the same passphrase derives a different key and the files share no data. If the files were identical, then an attacker could potentially recognize a pattern because it would be deterministic.

### 1.3
1. ECB produced 3 distinct blocks out of 37, and the most common repeated 24 times.
CBC produced 37 distinct blocks.

2. ECB leaked the structure within the plaintext. This was the important lesson in week 3, that a cipher fails when structure in the plaintext survives into the ciphertext. Because ECB encrypts each 16-byte block independently and deterministically,
an attacker without the key can still read off repeating patterns.

3. I would ask which mode? Because for example, ECB is a lot less secure than CBC. I would also ask whether each record gets a unique IV and whether there is a MAC.
## Part 2

### 2.2
1. SHA-256 is unkeyed, so it gives integrity against an accident instead of an attacker. So mallory could control the channel and modify the file, while the colleague still receives the same hash.
2. HMAC mixes a shared secret into the hash which turns integrity into authenticated integrity. So mallory can still change the message but she cannot produce a tag that verifies, so the colleague's check fails and the tampering is detected.
3. With SHA-256 mallory can read and modify a file. With HMAC, she can still read and modify, but she can't forge a matching tag, so the tampering is detected.
## Part 3
1. This check proves someone with access to the inbox clicked it, so whoever uploaded the key also has access to the inbox.
It proves that the key is associated with the address, but does not prove that the key belongs to a certain person. This is because the inbox could be compromised.
2. The safest way would be having the person write it down in person. If mallory controls the network, she can intercept the key in transit and modify it. In person she cannot. This works because the fingerprint is a collision-resistant hash of the key, so matching fingerprints mean matching keys, and Mallory can't construct a different key with the same fingerprint.

## Part 4


### 4.2
1. The 'pubkey enc packet' holds a randomly generated one-time symmetric session key, encrypted with my RSA-4096 public key. The 'encrypted data packet' holds the actual message, encrypted with the one session key.
2. GPG does it this way for two reasons. RSA can only encrypt something smaller than its modulus. And RSA is much slower than AES.
3. This construction is called hybrid encryption
### 4.3
1. Signing: sender's private key
2. Verifying: sender's public key
3. Encryption: recipient's public key
4. Decryption: recipient's private key
5. Signing provides authenticity while encryption does not. In week 4, we learned public key encryption gives confidentiality and integrity but no authentication, because anyone can use a public key.
## Part 5
The much smaller key is not necessarily the weaker key because Ed25519's problem is harder. Ed25519 rests on a discrete logarithm problem as opposed to RSA-4096's factoring problem, so a smaller key can have the same strength as a large key in RSA-4096.
## Part 7
### 7.1
AI assistant used: Claude
Prompt: "write me a python function that encrypts a file with AES"
### 7.2
1. The code uses AES.MODE_ECB, which encrypts every 16-byte block independently and deterministically. so identical plaintext produces identical ciphertext blocks. An attacker who never gets the key can still find a pattern because of this. So this violates the week 3 rule that a cipher fails when structure in the plaintext survives into the ciphertext.
2. Hardcoded key. key = b'1234567890123456' is written into the source, so anyone who reads the file can decrypt everything. Violates key management.
3. No integrity protection. There is no authenticated mode, so an attacker can modify the file and the decryption will still succeed. The lecture says to use an authenticated mode like AES-GCM, and that if you use raw CBC you should ask where the MAC is (which it doesn't).
### 7.3
Changed the mode from ECB to GCM, which removes the structural leak in ECB. GCM is what we learned is recommended for new code. This fixes the first defect.
The key now comes from getpass at runtime instead of being written into the source, which fixes defect 2.
decrypt_and_verify raises an error instead of returning plaintext when the tag does not verify, so tampering raises an error, fixing defect 3.
I also added PBKDF2-SHA256 key derivation with a random salt, and a random nonce per encryption, since GCM requires a nonce.
Demonstrated: encrypted and decrypted secret.txt with an identical result. After corrupting one byte of the ciphertext, decryption reported failure instead of returning garbage.
Note: imports use cryptodome rather than crypto, which is the namespace Ubuntu's python3-pycryptodome package installs. ai_crypto.py is unmodified.
