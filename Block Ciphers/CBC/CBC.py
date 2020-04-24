from padding import padding
from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
print "key:" + key.encode("hex")

IV = urandom(16)
print "iv: " + IV.encode("hex")
# key = raw_input("Enter key ")
# IV = raw_input("Enter iv ")
cipher = AES.new(key, AES.MODE_CBC, IV)
message = raw_input("Enter message ")
message = padding(message)

ciphertext = IV + cipher.encrypt(message)

print ciphertext
print len(ciphertext)
print ciphertext.encode("hex")