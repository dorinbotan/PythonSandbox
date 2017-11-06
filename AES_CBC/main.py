from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import Crypto.Util.Padding

# --------- Key -------------------------------------------
password = b'Password'
key = MD5.new(password).digest()
print("Key: ", MD5.new(password).hexdigest())

# --------- IV  -------------------------------------------
iv = Random.new().read(AES.block_size)

# --------- Encode ----------------------------------------
f = open('original.png', 'rb')
image = f.read()
f.close()

data = Crypto.Util.Padding.pad(image, AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphered = cipher.encrypt(data)

f = open('encrypted.png', 'wb')
f.write(ciphered)
f.close()

# --------- Decode ----------------------------------------
f = open('encrypted.png', 'rb')
image = f.read()
f.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(image)
# image = decrypted
image = Crypto.Util.Padding.unpad(decrypted, AES.block_size)

f = open('decrypted.png', 'wb')
f.write(image)
f.close()