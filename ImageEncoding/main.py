from Crypto.Cipher import AES
from Crypto.Hash import MD5

# --------- Key -------------------------------------------
password = b'Password'
key = MD5.new(password).digest()

print(MD5.new(password).hexdigest())

# --------- Encode ----------------------------------------
f = open('original.png', 'rb')
data = f.read()
f.close()

cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
print(nonce)
cipheredImage, tag = cipher.encrypt_and_digest(data)

f = open('ciphered.png', 'wb')
f.write(cipheredImage)
f.close()

# --------- Decode ----------------------------------------
f = open('ciphered.png', 'rb')
data = f.read()
f.close()

cipher = AES.new(key, AES.MODE_EAX, nonce)
decryptedImage = cipher.decrypt(data)

f = open('deciphered.png', 'wb')
f.write(decryptedImage)
f.close()