import os
from Crypto.Hash import MD5
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import Crypto.Util.Padding

backend = default_backend()
key = MD5.new(b'Password').digest()
iv = bytes.fromhex('ffffffffffffffffffffffffffffffff')

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

file = open('secret.jpg', 'rb')
msg = file.read()
file.close()
data = Crypto.Util.Padding.pad(msg, 16)
encryptor = cipher.encryptor()
ct = encryptor.update(data) + encryptor.finalize()


decryptor = cipher.decryptor()
decryptor.update(ct) + decryptor.finalize()

file = open('decrypted.jpg', 'wb')
file.write(ct)
file.close()