from PIL import Image
from scipy import *
import matplotlib.pyplot as plt

from Crypto.Cipher import AES
from Crypto.Hash import MD5
import binascii

# img = Image.open('linux.png')
# plt.imshow(img)
# plt.show()

# -------- Data -------------------------------------------
password = b'Password'
data = b"The quick brown fox jumps over the lazy dog."

key = MD5.new(password).digest()

# -------- Encrypt ----------------------------------------
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
cipheredtext, tag = cipher.encrypt_and_digest(data)
print(cipheredtext)

# -------- Decrypt ----------------------------------------
cipher = AES.new(key, AES.MODE_EAX, nonce)
decryptedtext = cipher.decrypt(cipheredtext)

try:
    cipher.verify(tag)
    print(decryptedtext)
except ValueError:
    print("Key incorrect or message corrupted")