from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import Crypto.Util.Padding

# --------- Key -------------------------------------------
key = MD5.new(b'Password').digest()

# --------- IV  -------------------------------------------
# iv = Random.new().read(AES.block_size)
iv = bytes.fromhex('ffffffffffffffffffffffffffffffff')

# --------- Encode ----------------------------------------
# msg = b"Hello world!1111"
# msg = bytes.fromhex('6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411e5fbc1191a0a52eff69f2445df4f9b17ad2b417be66c3710')
#
# # data = Crypto.Util.Padding.pad(msg, AES.block_size)
# cipher = AES.new(key, AES.MODE_CBC, iv)
# ciphered = cipher.encrypt(msg)
#
# a = ciphered.hex()
# print()
# print(a[:32])
# print(a[32:64])
# print(a[64:96])
# print(a[96:128])

file = open('secret.jpg', 'rb')
msg = file.read()
data = Crypto.Util.Padding.pad(msg, AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered = cipher.encrypt(data)

file.close()
file = open('encrypted_py.jpg', 'wb')
file.write(ciphered)
file.close()

# --------- Decode ----------------------------------------
file  = open('encrypted.jpg', 'rb')
ciphered = file.read();
file.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphered)
# msg = Crypto.Util.Padding.unpad(decrypted, AES.block_size)

file = open('decrypted.jpg', 'wb')
file.write(decrypted)
file.close()