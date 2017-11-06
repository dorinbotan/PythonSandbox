import hashlib
import Crypto

hash = hashlib.md5(b"password").hexdigest()
print(hash)

# key

print(b"Hello world")